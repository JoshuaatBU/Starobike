# Install script for directory: /home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/willSink" TYPE FILE FILES
    "/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/python/__init__.py"
    "/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/python/willSink.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/willSink" TYPE FILE FILES
    "/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/build/python/__init__.pyc"
    "/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/build/python/willSink.pyc"
    "/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/build/python/__init__.pyo"
    "/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-willSink/build/python/willSink.pyo"
    )
endif()

