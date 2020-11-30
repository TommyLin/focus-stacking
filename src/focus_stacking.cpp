#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "focus_stacking.hpp"

PYBIND11_MODULE(focus_stacking, m) {
    m.def("scan_dir",      &scan_dir,      "Scan image files in folder");
    m.def("gaussian_blur", &gaussian_blur, "Gaussian blur an image");
}
