
ifdef GCOV
# To build library with gcov profiling information
# $ make GCOV=1
CXX_EXTRA = -fprofile-arcs -ftest-coverage
endif

CXX       = g++
PY_INC    = $(shell python3 -m pybind11 --includes)
CXXFLAGS  = -O3 -Wall -Wextra -std=c++17 -fPIC $(CXX_EXTRA) $(PY_INC)
TARGET    = focus_stacking
SRCS      = gaussian_blur.cpp edge_detect.cpp
FSLIB     = $(TARGET)$(shell python3-config --extension-suffix)
OUT_DIR   = output

ifeq (, $(shell which lcov))
	$(error "No lcov not found, consider doing: sudo apt-get install lcov")
endif

BINARY    = scan_dir

.DEFAULT_GOAL = all
.PHONY: clean test lcov

all: $(FSLIB) $(BINARY)

$(FSLIB): $(SRCS:.cpp=.o)
	$(CXX) $(CXXFLAGS) -shared $? -o $@

%: %.cpp
	$(CXX) $(CXXFLAGS) $? -o $@

test: $(FSLIB)
	python3 -m pytest -v

lcov:
	make clean
	make GCOV=1
	make test
	lcov --capture --directory . --output-file $(TARGET).info --test-name $(TARGET)
	genhtml $(TARGET).info --output-directory $(OUT_DIR) --title "$(TARGET)" --show-details --legend
	# Then open file ./output/index.html with browser.
	# xdg-open ./$(OUT_DIR)/index.html

clean:
	rm -rf $(SRCS:.cpp=.o) $(FSLIB) __pycache__ .pytest_cache .cache
	rm -rf default.profraw $(OUT_DIR) $(TARGET).info *.gcov
	rm -rf $(SRCS:.cpp=.gcda) $(SRCS:.cpp=.gcno)
	@rm -rfv $(BINARY)
