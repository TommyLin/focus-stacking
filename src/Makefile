FLAGS ?=

ifdef GCOV
# To build library with gcov profiling information
# $ make GCOV=1
FLAGS = -fprofile-arcs -ftest-coverage
endif


UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)
MKLROOT ?= /opt/intel/mkl
MKLEXT ?= a
CXXFLAGS :=
endif

ifeq ($(UNAME_S),Linux)
MKLROOT ?= ${HOME}/opt/conda
MKLEXT ?= so
CXXFLAGS := -Wl,--no-as-needed
endif

MKLLINKLINE := \
	${MKLROOT}/lib/libmkl_intel_lp64.${MKLEXT} \
	${MKLROOT}/lib/libmkl_sequential.${MKLEXT} \
	${MKLROOT}/lib/libmkl_core.${MKLEXT}

CXX = g++
CXXFLAGS := ${CXXFLAGS} \
	-std=c++17 -O3 -g -m64 \
	-Wall -Wextra -Werror -shared \
	-I${MKLROOT}/include \
	-I../inc \
	-fPIC `python3 -m pybind11 --includes` \
	${FLAGS}

LDFLAGS = -lpthread -lm -ldl -lstdc++fs ${MKLLINKLINE}

TARGET  = focus_stacking
FSLIB   = $(TARGET)$(shell python3-config --extension-suffix)
OUT_DIR = output

SRCS    = focus_stacking.cpp \
		  gaussian_blur.cpp \
		  edge_detect.cpp \
		  scan_dir.cpp

ifeq (, $(shell which lcov))
	$(error "No lcov not found, consider doing: sudo apt-get install lcov")
endif


.DEFAULT_GOAL = all
.PHONY: clean test lcov

all: $(FSLIB)

$(FSLIB): $(SRCS:.cpp=.o)
	$(CXX) $(CXXFLAGS) $? -o $@ $(LDFLAGS)

test: $(FSLIB)
	python3 -m pytest -v -l

lcov:
	make clean
	make GCOV=1
	make test
	lcov --capture --directory . --output-file $(TARGET).info --test-name $(TARGET)
	genhtml $(TARGET).info --output-directory $(OUT_DIR) --title "$(TARGET)" --show-details --legend
	# Then open file ./output/index.html with browser.
	# xdg-open ./$(OUT_DIR)/index.html

clean:
	@rm -rfv $(SRCS:.cpp=.o) $(FSLIB) __pycache__ .pytest_cache .cache
	@rm -rfv default.profraw $(OUT_DIR) $(TARGET).info *.gcov
	@rm -rfv $(SRCS:.cpp=.gcda) $(SRCS:.cpp=.gcno)
