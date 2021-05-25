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

#ifndef INCLUDED_GRAPHICSINK_SENIORSINK_H
#define INCLUDED_GRAPHICSINK_SENIORSINK_H

#include <graphicsink/api.h>
#include <gnuradio/sync_block.h>
#include <gnuradio/qtgui/api.h>
#include <gnuradio/sync_block.h>



namespace gr {
  namespace graphicsink {

    /*!
     * \brief <+description of block+>
     * \ingroup graphicsink
     *
     */
    class GRAPHICSINK_API seniorsink : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<seniorsink> sptr;

      /*!
 * \brief A graphical sink to display multiple vector-based signals.
 * \ingroup instrumentation_blk
 * \ingroup qtgui_blk
 *
 * \details
 * This is a QT-based graphical sink that plots vectors of data as-is.
 * Each signal is plotted with a different color, and the set_title()
 * and set_color() functions can be used to change the label and color
 * for a given input number.
 *
 * To specify units for the x- and y-axes, use the set_x_axis_units()
 * and set_y_axis_units() functions. This does not change the x- and
 * y-labels, which are either specified during construction, or by
 * calling the set_x_axis_label() and set_y_axis_label() methods.
 */
class QTGUI_API seniorsink : virtual public sync_block
{
public:
    // gr::qtgui::seniorsink::sptr
    typedef std::shared_ptr<seniorsink> sptr;

        /*!
         * \brief Build a vector plotting sink.
         *
         * \param vlen Vector length at input. This cannot be changed during operations.
         * \param x_start The x-Axis value of the first vector element
         * \param x_step The step with which x-Axis values increment
         * \param x_axis_label The X-Axis label
         * \param y_axis_label The Y-Axis label
         * \param name title for the plot
         * \param nconnections number of signals connected to sink
         * \param parent a QWidget parent object, if any
         */
        static sptr make(unsigned int vlen,
                         double x_start,
                         double x_step,
                         const std::string& x_axis_label,
                         const std::string& y_axis_label,
                         const std::string& name,
                         int nconnections = 1,
                         QWidget* parent = NULL);

        virtual void exec_() = 0;
        virtual QWidget* qwidget() = 0;

    #ifdef ENABLE_PYTHON
        virtual PyObject* pyqwidget() = 0;
    #else
        virtual void* pyqwidget() = 0;
    #endif

        virtual unsigned int vlen() const = 0;
        virtual void set_vec_average(const float avg) = 0;
        virtual float vec_average() const = 0;

        //! Update the values on the x-Axis.
        //
        // \param start The value for the first vector element.
        // \param step Increments per x-Axis value
        virtual void set_x_axis(const double start, const double step) = 0;
        virtual void set_y_axis(double min, double max) = 0;
        //! The ref level is a reference line
        virtual void set_ref_level(double ref_level) = 0;

        virtual void set_x_axis_label(const std::string& label) = 0;
        virtual void set_y_axis_label(const std::string& label) = 0;

        //! Change the units string on the x-Axis (e.g. 'm' if x-Axis label was 'Distance')
        virtual void set_x_axis_units(const std::string& units) = 0;
        //! Change the units string on the y-Axis (e.g. 'V' if x-Axis label was 'Amplitude')
        virtual void set_y_axis_units(const std::string& units) = 0;

        virtual void set_update_time(double t) = 0;
        virtual void set_title(const std::string& title) = 0;
        virtual void set_line_label(unsigned int which, const std::string& label) = 0;
        virtual void set_line_color(unsigned int which, const std::string& color) = 0;
        virtual void set_line_width(unsigned int which, int width) = 0;
        virtual void set_line_style(unsigned int which, int style) = 0;
        virtual void set_line_marker(unsigned int which, int marker) = 0;
        virtual void set_line_alpha(unsigned int which, double alpha) = 0;

        virtual std::string title() = 0;
        virtual std::string line_label(unsigned int which) = 0;
        virtual std::string line_color(unsigned int which) = 0;
        virtual int line_width(unsigned int which) = 0;
        virtual int line_style(unsigned int which) = 0;
        virtual int line_marker(unsigned int which) = 0;
        virtual double line_alpha(unsigned int which) = 0;

        virtual void set_size(int width, int height) = 0;

        virtual void enable_menu(bool en = true) = 0;
        virtual void enable_grid(bool en = true) = 0;
        virtual void enable_autoscale(bool en = true) = 0;
        virtual void clear_max_hold() = 0;
        virtual void clear_min_hold() = 0;
        virtual void reset() = 0;

        QApplication* d_qApplication;
      static sptr make();
    };

  } // namespace graphicsink
} // namespace gr

#endif /* INCLUDED_GRAPHICSINK_SENIORSINK_H */
