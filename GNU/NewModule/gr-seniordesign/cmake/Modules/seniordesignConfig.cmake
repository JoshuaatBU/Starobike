INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SENIORDESIGN seniordesign)

FIND_PATH(
    SENIORDESIGN_INCLUDE_DIRS
    NAMES seniordesign/api.h
    HINTS $ENV{SENIORDESIGN_DIR}/include
        ${PC_SENIORDESIGN_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SENIORDESIGN_LIBRARIES
    NAMES gnuradio-seniordesign
    HINTS $ENV{SENIORDESIGN_DIR}/lib
        ${PC_SENIORDESIGN_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/seniordesignTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SENIORDESIGN DEFAULT_MSG SENIORDESIGN_LIBRARIES SENIORDESIGN_INCLUDE_DIRS)
MARK_AS_ADVANCED(SENIORDESIGN_LIBRARIES SENIORDESIGN_INCLUDE_DIRS)
