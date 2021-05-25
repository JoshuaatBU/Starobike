INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RADARSINK radarSink)

FIND_PATH(
    RADARSINK_INCLUDE_DIRS
    NAMES radarSink/api.h
    HINTS $ENV{RADARSINK_DIR}/include
        ${PC_RADARSINK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RADARSINK_LIBRARIES
    NAMES gnuradio-radarSink
    HINTS $ENV{RADARSINK_DIR}/lib
        ${PC_RADARSINK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/radarSinkTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RADARSINK DEFAULT_MSG RADARSINK_LIBRARIES RADARSINK_INCLUDE_DIRS)
MARK_AS_ADVANCED(RADARSINK_LIBRARIES RADARSINK_INCLUDE_DIRS)
