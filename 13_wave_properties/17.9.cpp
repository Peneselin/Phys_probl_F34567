#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    // Фізичні константи
    const double h = 6.626e-34;        // Стала Планка (Дж*с)
    const double e_charge = 1.602e-19; // Елементарний заряд (Кл)

    double r = 10.0e-3;            // Радіус у метрах (10 мм)
    double B = 2.0e-3;             // Магнітна індукція у Теслах (2 мТл)
    double q_alpha = 2 * e_charge; // Заряд альфа-частинки (2 елементарні заряди)
    
    // Обчислення імпульсу (p = qBr) та довжини хвилі (lambda = h/p)
    double p = q_alpha * B * r;
    double lambda = h / p;
    
    cout << "--- Задача 17.9 ---" << endl;
    cout << "Довжина хвилі де Бройля для альфа-частинки: " << scientific << lambda << " м" << endl;
    
    return 0;
}
