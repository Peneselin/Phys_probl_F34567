#include <iostream>
#include <cmath>
#include <iomanip>
#include <locale>

using namespace std;

int main() {
    // підключення української локалізації
    setlocale(LC_CTYPE, "ukr");

    std::cout << std::fixed << std::setprecision(6);

    double e, m, h_bar, epsilon_0;

    std::cout << "~~Розрахунок еквівалентного струму електрона~~\n";
    
    // Введення констант
    std::cout << "(Примітка: вводьте числа правильно, інакше, код не спрацює; приклад:1.602e-19 )\n";
    
    std::cout << "Введіть заряд електрона e (Кл): ";
    std::cin >> e;
    
    std::cout << "Введіть масу електрона m (кг): ";
    std::cin >> m;
    
    std::cout << "Введіть зведену сталу Планка h_bar (Дж*с): ";
    std::cin >> h_bar;
    
    std::cout << "Введіть електричну сталу (Ф/м): ";
    std::cin >> epsilon_0;

    // 1. Розрахунок радіуса першої орбіти (r1)
    double r1 = (4 * M_PI * epsilon_0 * std::pow(h_bar, 2)) / (m * std::pow(e, 2));
    
    // 2. Розрахунок швидкості на першій орбіті (v1)за постулатом Бора  (mvr = h_bar)
    double v1 = h_bar / (m * r1);
    
    // 3. Розрахунок еквівалентного струму I = e / T, де T = 2*PI*r / v
    // Отже, I = (e * v1) / (2 * PI * r1)
    double current = (e * v1) / (2 * M_PI * r1);

    std::cout << "\n~~~Результати розрахунку~~~\n";
    std::cout << "Радіус першої орбіти (r1): " << r1 << " м\n";
    std::cout << "Швидкість електрона (v1):  " << v1 << " м/с\n";
    std::cout << " Еквівалентний струм(I):   " << current << " А\n";
     std::cout << "\nЗадачу вирішено! ^_^\n";
    return 0;
}
