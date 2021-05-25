/* -*- c++ -*- */

#define GRAPHICSINK_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "graphicsink_swig_doc.i"

%{
#include "graphicsink/seniorsink.h"
#include "graphicsink/vector_sink.h"
%}

%include "graphicsink/seniorsink.h"
GR_SWIG_BLOCK_MAGIC2(graphicsink, seniorsink);
%include "graphicsink/vector_sink.h"
GR_SWIG_BLOCK_MAGIC2(graphicsink, vector_sink);
