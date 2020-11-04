#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <stdexcept>
#include <cmath>

namespace py = pybind11;

void gaussian_blur(void) {

}



PYBIND11_MODULE(focus_stacking, m) {
    m.def("gaussian_blur", &gaussian_blur,
            "Gaussian blur an image");
}
