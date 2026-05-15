#include <iostream>
#include <cmath>
#include <iomanip>
#include <locale> 

using namespace std;

int main() {
    setlocale(LC_CTYPE, "ukr");

    // Константи
    double h = 6.626e-34;      // Стала Планка 
    double Me = 9.11e-31;     // Маса електрона 
    double Na = 6.022e23;     // Число Авогадро 
    double Pi = 3.14;
    double eV = 1.602e-19;    // 1 електрон-вольт 

    // Змінні для вводу
    double rho, M;
    
    std::cout << "~~Знаходження макс.енергії електрона, середньої енергії електрона і тиску електронного газу~~\n";

    cout << "Введіть густину металу (кг/м^3): ";
    cin >> rho;
    cout << "Введіть молярну масу (кг/моль): ";
    cin >> M;

    // 1. Розрахунок концентрації електронів n
    double n = (rho * Na) / M;

    // 2. Максимальна енергія електрона (Енергія Фермі) Ef
    double Ef_joules = (pow(h, 2) / (8 * Me)) * pow((3 * n) / Pi, 2.0/3.0);
    double Ef_eV = Ef_joules / eV;

    // 3. Середня енергія електрона <E>
    double E_avg_joules = 0.6 * Ef_joules;
    double E_avg_eV = E_avg_joules / eV;

    // 4. Тиск електронного газу P
    double P = (2.0 / 5.0) * n * Ef_joules;

    // Вивід результатів
    cout << fixed << setprecision(4);
    cout << "\n~~ Результати розрахунків ~~" << endl;
    cout << "1) Максимальна енергія (Енергія Фермі):" << endl;
    cout << "   " << Ef_eV << " еВ" << endl;
    
    cout << "2) Середня енергія електрона:" << endl;
    cout << "   " << E_avg_eV << " еВ" << endl;

    cout << "3) Тиск електронного газу:" << endl;
    cout << "   " << P << " Па" << endl;
    cout << "\n~~ Задачу вирішено! :3 ~~" << endl;

    return 0;
}
