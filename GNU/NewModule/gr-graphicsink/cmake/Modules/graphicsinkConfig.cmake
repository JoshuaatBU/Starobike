INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GRAPHICSINK graphicsink)

FIND_PATH(
    GRAPHICSINK_INCLUDE_DIRS
    NAMES graphicsink/api.h
    HINTS $ENV{GRAPHICSINK_DIR}/include
        ${PC_GRAPHICSINK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GRAPHICSINK_LIBRARIES
    NAMES gnuradio-graphicsink
    HINTS $ENV{GRAPHICSINK_DIR}/lib
        ${PC_GRAPHICSINK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/graphicsinkTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GRAPHICSINK DEFAULT_MSG GRAPHICSINK_LIBRARIES GRAPHICSINK_INCLUDE_DIRS)
MARK_AS_ADVANCED(GRAPHICSINK_LIBRARIES GRAPHICSINK_INCLUDE_DIRS)
