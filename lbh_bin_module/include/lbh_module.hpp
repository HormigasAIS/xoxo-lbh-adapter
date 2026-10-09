#pragma once

#include <string>

namespace lbh {

class Module {
public:
    Module() = default;
    ~Module() = default;

    std::string greet() const {
        return "Hola desde Lenguaje-Binario-HormigasAIS!";
    }
};

} // namespace lbh
