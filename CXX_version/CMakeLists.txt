cmake_minimum_required (VERSION 3.10.1)
project( myFirstHdf5 C CXX )

set (LIB_TYPE STATIC) # or SHARED
string(TOLOWER ${LIB_TYPE} SEARCH_TYPE)

#find_package (HDF5 NAMES hdf5 COMPONENTS C CXX ${SEARCH_TYPE})
#find_package(HDF5 COMPONENTS CXX HL REQUIRED)
find_package(HDF5 COMPONENTS C CXX HL REQUIRED)

link_directories( ${HDF5_LIBRARY_DIRS} )

include_directories (${HDF5_INCLUDE_DIR})
set (LINK_LIBS ${LINK_LIBS} ${HDF5_C_${LIB_TYPE}_LIBRARY})


#########below use a LIB: OPENMP
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb -DDEBUG")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

FIND_PACKAGE( OpenMP REQUIRED) #find omp
if(OPENMP_FOUND)
    message("OPENMP FOUND")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set(CMAKE_EXE_LINKER_FLAGS"${CMAKE_EXE_LINKER_FLAGS}${OpenMP_EXE_LINKER_FLAGS}")
endif()
#########OPENMP

#set (example hdfcompile)
aux_source_directory(src SRC_LIST)

add_executable(main ${SRC_LIST})

target_link_libraries (main ${HDF5_CXX_LIBRARIES})

set (EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
