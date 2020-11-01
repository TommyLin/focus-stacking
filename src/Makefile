CXX = g++
ifdef GCOV
# To build library with gcov profiling information
# $ make GCOV=1
CXX_EXTRA = -fprofile-arcs -ftest-coverage
endif
CXX_FLAGS = -O3 -Wall -Wextra -shared -std=c++11 -fPIC $(CXX_EXTRA)
PY_INC = `python3 -m pybind11 --includes`
# Focus Stacking Library
TARGET = focus_stacking
SRCS = gaussian_blur.cpp
LIBRARY = $(TARGET)$(shell python3-config --extension-suffix)

.PHONY: clean test lcov
default: $(LIBRARY)

$(LIBRARY): $(SRCS)
	$(CXX) $(CXX_FLAGS) $(PY_INC) $? -o $@

test: $(LIBRARY)
	python3 -m pytest -v

# For ubuntu, please install lcov first.
# $ sudo apt install lcov
# Steps to produce code coverage report
# $ make GCOV=1 test
# $ make lcov
# Then open file ./output/index.html with browser.
lcov:
	lcov --capture --directory . --output-file $(TARGET).info --test-name $(TARGET)
	genhtml $(TARGET).info --output-directory output --title "$(TARGET)" --show-details --legend

clean:
	rm -Rf $(LIBRARY) __pycache__ .pytest_cache .cache
	rm -Rf default.profraw output $(TARGET).info $(TARGET).gcda $(TARGET).gcno *.gcov
