#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    const double pi = 3.141592653589793;
    
    cout << "--- ?????? 17.16 ---" << endl;
    cout << "Аналітичні результати (виведені з умови нормування та максимуму густини ймовірності): " << endl;
    cout << "1) Коефіцієнт A = 1 / (pi^(3/4) * a^(3/2))" << endl;
    cout << "2) Найімовірніша відстань частинки від центру r_max = a\n" << endl;
    
    
    double a;
    cout << "Введіть значення константи 'a' (наприклад, 1e-9 для 1 нм): ";
    cin >> a;
    
    double A = 1.0 / (pow(pi, 0.75) * pow(a, 1.5));
    
    cout << "Для a = " << scientific << a << " ?:" << endl;
    cout << "Значення коефіцієнта A: " << scientific << A << " ?^(-3/2)" << endl;
    cout << "Найімовірніша відстань: " << scientific << a << " ?" << endl;
    
    return 0;
}
