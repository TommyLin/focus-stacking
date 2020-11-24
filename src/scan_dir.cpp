#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <experimental/filesystem>

namespace fs = std::experimental::filesystem;


int scan_dir(char *path)
{
#ifdef DEBUG
    std::cout << path << std::endl;
#endif

    if (!fs::exists(path))
        throw std::invalid_argument("Input path not exist!");

    for (const auto & entry : fs::directory_iterator(path))
        std::cout << entry.path() << std::endl;

    return 0;
}

PYBIND11_MODULE(focus_stacking, m) {
    m.def("scan_dir", &scan_dir, "Scan image files in folder");
}
