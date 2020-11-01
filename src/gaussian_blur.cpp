#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <stdexcept>
#include <cmath>

namespace py = pybind11;

float angle(std::array<float, 2> vec1, std::array<float, 2> vec2) {
    float len1 = vec1[0] * vec1[0] + vec1[1] * vec1[1];
    float len2 = vec2[0] * vec2[0] + vec2[1] * vec2[1];

    if (len1 == 0 || len2 == 0)
        throw std::invalid_argument("Vector length should not be zero");

    float dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1];
    float value = dot_product / sqrt(len1 * len2);

    return acos(value);
}

PYBIND11_MODULE(focus_stacking, m) {
    m.def("angle", &angle, "Calculate the angle (in radians) between two "
                           "vectors in the 2-D Cartesian coordinate system.");
}
