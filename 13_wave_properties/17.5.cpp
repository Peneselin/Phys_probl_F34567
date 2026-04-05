#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    // Фізичні константи
    const double h = 6.626e-34;        // Стала Планка (Дж*с)
    const double e_charge = 1.602e-19; // Елементарний заряд (Кл)
    const double m_p = 1.672e-27;      // Маса протона (кг)

    double E1_eV = 1.0;
    double E2_keV = 1.0;
    
    // Переведення кінетичної енергії в Джоулі
    double E1_J = E1_eV * e_charge;
    double E2_J = E2_keV * 1000.0 * e_charge;
    
    // Обчислення довжин хвиль за формулою де Бройля
    double lambda1 = h / sqrt(2 * m_p * E1_J);
    double lambda2 = h / sqrt(2 * m_p * E2_J);
    
    cout << "--- Задача 17.5 ---" << endl;
    cout << "Довжина хвилі для 1.00 еВ: " << scientific << lambda1 << " м" << endl;
    cout << "Довжина хвилі для 1.00 кеВ: " << scientific << lambda2 << " м" << endl;
    
    return 0;
}
