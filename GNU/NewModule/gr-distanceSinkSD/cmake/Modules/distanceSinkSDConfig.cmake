INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DISTANCESINKSD distanceSinkSD)

FIND_PATH(
    DISTANCESINKSD_INCLUDE_DIRS
    NAMES distanceSinkSD/api.h
    HINTS $ENV{DISTANCESINKSD_DIR}/include
        ${PC_DISTANCESINKSD_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DISTANCESINKSD_LIBRARIES
    NAMES gnuradio-distanceSinkSD
    HINTS $ENV{DISTANCESINKSD_DIR}/lib
        ${PC_DISTANCESINKSD_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/distanceSinkSDTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DISTANCESINKSD DEFAULT_MSG DISTANCESINKSD_LIBRARIES DISTANCESINKSD_INCLUDE_DIRS)
MARK_AS_ADVANCED(DISTANCESINKSD_LIBRARIES DISTANCESINKSD_INCLUDE_DIRS)