#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    
    const double h = 6.626e-34;       
    const double e_charge = 1.602e-19; 
    const double m_e = 9.109e-31;      

    double U = 2000.0;      
    double d = 0.3e-9;       
    
    double lambda = h / sqrt(2 * m_e * e_charge * U);
    
  
    int k_max = floor(d / lambda);
    
    int N = 2 * k_max + 1;
    
    cout << "Довжина хвилі електронів: " << scientific << lambda << " ?" << endl;
    cout << "Максимальний порядок дифракції (k): " << k_max << endl;
    cout << "Загальна кількість дифракційних максимумів: " << N << endl;
    
    return 0;
}
