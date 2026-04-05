#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    
    const double h = 6.626e-34;        
    const double e_charge = 1.602e-19; 
    const double m_e = 9.109e-31;      

    double U = 30.0;         
    double d = 50.0e-6;      
    double L = 100.0e-2;     
    
    
    double lambda = h / sqrt(2 * m_e * e_charge * U);
    
    
    double delta_y = (lambda * L) / d;
    
    cout << ": " << scientific << lambda << " ?" << endl;
    cout << ": " << scientific << delta_y << " ?" << endl;
    
    return 0;
}
