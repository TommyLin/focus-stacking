#include <string>
#include <iostream>
#include <experimental/filesystem>

namespace fs = std::experimental::filesystem;


int main(int argc, char *argv[])
{
    std::string path = "../images/group/";
    std::cout << argc << std::endl;
    if (argc > 1) {
        path = argv[1];
        std::cout << argv[1] << std::endl;
    } else {
        path = "../images/group/";
    }
    for (const auto & entry : fs::directory_iterator(path))
        std::cout << entry.path() << std::endl;

    return 0;
}
