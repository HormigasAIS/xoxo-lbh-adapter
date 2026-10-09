#include "lbh_module.hpp"
#include <pybind11/pybind11.h>

namespace py = pybind11;
using namespace lbh;

PYBIND11_MODULE(lbh_module, m) {
    py::class_<Module>(m, "Module")
        .def(py::init<>())
        .def("greet", &Module::greet);
}
