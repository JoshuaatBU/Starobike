INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_WILLSINK willSink)

FIND_PATH(
    WILLSINK_INCLUDE_DIRS
    NAMES willSink/api.h
    HINTS $ENV{WILLSINK_DIR}/include
        ${PC_WILLSINK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    WILLSINK_LIBRARIES
    NAMES gnuradio-willSink
    HINTS $ENV{WILLSINK_DIR}/lib
        ${PC_WILLSINK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/willSinkTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WILLSINK DEFAULT_MSG WILLSINK_LIBRARIES WILLSINK_INCLUDE_DIRS)
MARK_AS_ADVANCED(WILLSINK_LIBRARIES WILLSINK_INCLUDE_DIRS)
