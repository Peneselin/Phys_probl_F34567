// Author:Mykola Kuryliv
#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <windows.h> 

int main() {
    SetConsoleOutputCP(CP_UTF8);
    std::cout << std::fixed;

    // Constants
    const double R = 1.097373e7;          // Rydberg constant, m⁻¹
    const double lambda_min = 400e-9;     // 400 nm
    const double lambda_max = 760e-9;     // 760 nm
    const int m = 2;                      // Balmer series
    const double inv_m_sq = 1.0 / (m * m);

    std::cout << "     Balmer Series (m = " << m << ")    \n";
    std::cout << "Visible spectrum range: 400 — 760 nm\n\n";

    // Calculate k bounds
    double denom_max = inv_m_sq - (1.0 / (R * lambda_max));
    double denom_min = inv_m_sq - (1.0 / (R * lambda_min));

    int k_start = 3;
    if (denom_max > 0) {
        // Додаємо мікропохибку 1e-9 перед ceil, щоб уникнути 3.0000001 -> 4
        k_start = std::ceil(std::sqrt(1.0 / denom_max) - 1e-9);
    }
    
    // Додаємо мікропохибку 1e-9 перед floor, щоб уникнути 5.9999999 -> 5
    int k_end = std::floor(std::sqrt(1.0 / denom_min) + 1e-9);

    std::cout << "Searching transitions k = " << k_start
              << " ... " << k_end << "\n\n";

    struct SpectralLine {
        int k;
        double wavelength_nm;
    };

    std::vector<SpectralLine> lines;

    for (int k = k_start; k <= k_end; ++k) {
        double inv_lambda = R * (inv_m_sq - 1.0 / (k * k));
        double lambda_nm = 1.0 / inv_lambda * 1e9;

        if (lambda_nm >= 400.0 && lambda_nm <= 760.0) {
            lines.push_back({k, lambda_nm});
            std::cout << std::setprecision(1)
                      << "k = " << k
                      << " → λ = " << lambda_nm
                      << " nm (visible)\n";
        }
    }

    std::cout << "\n     Result      \n";
    std::cout << "Number of Balmer series lines in visible region: " 
              << lines.size() << "\n\n";

    if (!lines.empty()) {
        std::cout << "List of lines:\n";
        for (const auto& line : lines) {
            std::cout << std::setprecision(1)
                      << " • Transition " << m << " ← " << line.k
                      << " (" << line.wavelength_nm << " nm)\n";
        }
    }

    return 0;
}