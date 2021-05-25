/* -*- c++ -*- */
/*
 * Copyright 2021 gr-graphicsink author.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "seniorsink_impl.h"
#include <gnuradio/prefs.h>

#include <volk/volk.h>

#include <cstring>

namespace gr {
  namespace graphicsink {

    seniorsink::sptr
    seniorsink::make(unsigned int vlen,
                                        double x_start,
                                        double x_step,
                                        const std::string& x_axis_label,
                                        const std::string& y_axis_label,
                                        const std::string& name,
                                        int nconnections,
                                        QWidget* parent)

    {
      return gnuradio::get_initial_sptr
        (new seniorsink_impl(
        vlen, x_start, x_step, x_axis_label, y_axis_label, name, nconnections, parent));
    }


    /*
     * The private constructor
     */
    seniorsink_impl::seniorsink_impl(unsigned int vlen,
                                       double x_start,
                                       double x_step,
                                       const std::string& x_axis_label,
                                       const std::string& y_axis_label,
                                       const std::string& name,
                                       int nconnections,
                                       QWidget* parent)
      : gr::sync_block("seniorsink",io_signature::make(1, -1, sizeof(float) * vlen),
                 io_signature::make(0, 0, 0)),
      d_vlen(vlen),
      d_vecavg(1.0),
      d_name(name),
      d_nconnections(nconnections),
      d_port(pmt::mp(MSG_PORT_OUT_XVAL)),
      d_msg(pmt::mp("x")),
      d_parent(parent)
    {
    // setup output message port to post frequency when display is
    // double-clicked
    message_port_register_out(d_port);

    for (int i = 0; i < d_nconnections; i++) {
        d_magbufs.emplace_back(d_vlen);
    }

    initialize(name, x_axis_label, y_axis_label, x_start, x_step);

}

    /*
     * Our virtual destructor.
     */
    seniorsink_impl::~seniorsink_impl()
    {
        if (!d_main_gui->isClosed()) {
        d_main_gui->close();
        }

        bool seniorsink_impl::check_topology(int ninputs, int noutputs)
    {
        return ninputs == d_nconnections;
    }

    void seniorsink_impl::initialize(const std::string& name,
                                        const std::string& x_axis_label,
                                        const std::string& y_axis_label,
                                        double x_start,
                                        double x_step)
    {
        if (qApp != NULL) {
            d_qApplication = qApp;
        } else {
    #if QT_VERSION >= 0x040500 && QT_VERSION < 0x050000
            std::string style = prefs::singleton()->get_string("qtgui", "style", "raster");
            QApplication::setGraphicsSystem(QString(style.c_str()));
    #endif
            d_qApplication = new QApplication(d_argc, &d_argv);
        }

        // If a style sheet is set in the prefs file, enable it here.
        check_set_qss(d_qApplication);

        d_main_gui = new VectorDisplayForm(d_nconnections, d_parent);
        d_main_gui->setVecSize(d_vlen);
        set_x_axis(x_start, x_step);

        if (!name.empty())
            set_title(name);
        set_x_axis_label(x_axis_label);
        set_y_axis_label(y_axis_label);

        // initialize update time to 10 times a second
        set_update_time(0.1);
    }

    void seniorsink_impl::exec_() { d_qApplication->exec(); }

    QWidget* seniorsink_impl::qwidget() { return d_main_gui; }

    #ifdef ENABLE_PYTHON
    PyObject* seniorsink_impl::pyqwidget()
    {
        PyObject* w = PyLong_FromVoidPtr((void*)d_main_gui);
        PyObject* retarg = Py_BuildValue("N", w);
        return retarg;
    }
    #else
    void* seniorsink_impl::pyqwidget() { return NULL; }
    #endif

    unsigned int seniorsink_impl::vlen() const { return d_vlen; }

    void seniorsink_impl::set_vec_average(const float avg)
    {
        if (avg < 0 || avg > 1.0) {
            GR_LOG_ALERT(d_logger,
                         "Invalid average value received in set_vec_average(), must be "
                         "within [0, 1].");
            return;
        }
        d_main_gui->setVecAverage(avg);
        d_vecavg = avg;
    }

    float seniorsink_impl::vec_average() const { return d_vecavg; }

    void seniorsink_impl::set_x_axis(const double start, const double step)
    {
        d_main_gui->setXaxis(start, step);
    }

    void seniorsink_impl::set_y_axis(double min, double max)
    {
        d_main_gui->setYaxis(min, max);
    }

    void seniorsink_impl::set_ref_level(double ref_level)
    {
        d_main_gui->setRefLevel(ref_level);
    }

    void seniorsink_impl::set_x_axis_label(const std::string& label)
    {
        d_main_gui->setXAxisLabel(label.c_str());
    }

    void seniorsink_impl::set_y_axis_label(const std::string& label)
    {
        d_main_gui->setYAxisLabel(label.c_str());
    }

    void seniorsink_impl::set_x_axis_units(const std::string& units)
    {
        d_main_gui->getPlot()->setXAxisUnit(units.c_str());
    }

    void seniorsink_impl::set_y_axis_units(const std::string& units)
    {
        d_main_gui->getPlot()->setYAxisUnit(units.c_str());
    }

    void seniorsink_impl::set_update_time(double t)
    {
        // convert update time to ticks
        gr::high_res_timer_type tps = gr::high_res_timer_tps();
        d_update_time = t * tps;
        d_main_gui->setUpdateTime(t);
        d_last_time = 0;
    }

    void seniorsink_impl::set_title(const std::string& title)
    {
        d_main_gui->setTitle(title.c_str());
    }

    void seniorsink_impl::set_line_label(unsigned int which, const std::string& label)
    {
        d_main_gui->setLineLabel(which, label.c_str());
    }

    void seniorsink_impl::set_line_color(unsigned int which, const std::string& color)
    {
        d_main_gui->setLineColor(which, color.c_str());
    }

    void seniorsink_impl::set_line_width(unsigned int which, int width)
    {
        d_main_gui->setLineWidth(which, width);
    }

    void seniorsink_impl::set_line_style(unsigned int which, int style)
    {
        d_main_gui->setLineStyle(which, (Qt::PenStyle)style);
    }

    void seniorsink_impl::set_line_marker(unsigned int which, int marker)
    {
        d_main_gui->setLineMarker(which, (QwtSymbol::Style)marker);
    }

    void seniorsink_impl::set_line_alpha(unsigned int which, double alpha)
    {
        d_main_gui->setMarkerAlpha(which, (int)(255.0 * alpha));
    }

    void seniorsink_impl::set_size(int width, int height)
    {
        d_main_gui->resize(QSize(width, height));
    }

    std::string seniorsink_impl::title() { return d_main_gui->title().toStdString(); }

    std::string seniorsink_impl::line_label(unsigned int which)
    {
        return d_main_gui->lineLabel(which).toStdString();
    }

    std::string seniorsink_impl::line_color(unsigned int which)
    {
        return d_main_gui->lineColor(which).toStdString();
    }

    int seniorsink_impl::line_width(unsigned int which)
    {
        return d_main_gui->lineWidth(which);
    }

    int seniorsink_impl::line_style(unsigned int which)
    {
        return d_main_gui->lineStyle(which);
    }

    int seniorsink_impl::line_marker(unsigned int which)
    {
        return d_main_gui->lineMarker(which);
    }

    double seniorsink_impl::line_alpha(unsigned int which)
    {
        return (double)(d_main_gui->markerAlpha(which)) / 255.0;
    }

    void seniorsink_impl::enable_menu(bool en) { d_main_gui->enableMenu(en); }

    void seniorsink_impl::enable_grid(bool en) { d_main_gui->setGrid(en); }

    void seniorsink_impl::enable_autoscale(bool en) { d_main_gui->autoScale(en); }

    void seniorsink_impl::clear_max_hold() { d_main_gui->clearMaxHold(); }

    void seniorsink_impl::clear_min_hold() { d_main_gui->clearMinHold(); }

    void seniorsink_impl::reset()
    {
        // nop
    }

    void seniorsink_impl::check_clicked()
    {
        if (d_main_gui->checkClicked()) {
            double xval = d_main_gui->getClickedXVal();
            message_port_pub(d_port, pmt::cons(d_msg, pmt::from_double(xval)));
        }
    }

    int seniorsink_impl::work(int noutput_items,
                                 gr_vector_const_void_star& input_items,
                                 gr_vector_void_star& output_items)
    {
        const float* in = (const float*)input_items[0];

        // See if we generate a message
        check_clicked();

        for (int i = 0; i < noutput_items; i++) {
            if (gr::high_res_timer_now() - d_last_time > d_update_time) {
                for (int n = 0; n < d_nconnections; n++) {
                    in = ((const float*)input_items[n]) + d_vlen;
                    for (unsigned int x = 0; x < d_vlen; x++) {
                        d_magbufs[n][x] =
                            (double)((1.0 - d_vecavg) * d_magbufs[n][x] + (d_vecavg)*in[x]);
                    }
                }
                d_last_time = gr::high_res_timer_now();
                d_qApplication->postEvent(d_main_gui, new FreqUpdateEvent(d_magbufs, d_vlen));
            }
        }

        return noutput_items;
    }

  } /* namespace graphicsink */
} /* namespace gr */

