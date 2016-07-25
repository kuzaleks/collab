# Collab

Unittests based on **CxxTest**. The goal is to facilitate automatic grading of students labs.

## Prerequisite

Installed **Python** and **ply** package.

## Installation

1. Download and unpack CxxTest.

2. Setup env veriables:

*export CXXTEST="path/to/unpacked/cxxtest/folder/"*
*export CPATH="$CXXTEST:$CPATH"*

(e.g.
*export CXXTEST="/home/aliaksei-kuzmin2/Projects/utils/cxxtest-4.3/"*
*export CPATH="$CXXTEST:$CPATH"*
)


## Get Started

1. Make bin directory:

*mkdir bin*

2. Generate test .cpp:

*$CXXTEST/bin/cxxtestgen --error-printer -o bin/runner.cpp src/example_test.h*

3. Compile:

*g++ -o bin/runner bin/runner.cpp*

4. Run the compiled test:

*./bin/runner*

## Resources

Please follow instruction on the following resources
* https://habrahabr.ru/post/69160/
* http://cxxtest.com/guide.html#gettingStarted
