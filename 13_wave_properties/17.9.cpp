#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    
    const double h = 6.626e-34;        
    const double e_charge = 1.602e-19; 

    double r = 10.0e-3;            
    double B = 2.0e-3;            
    double q_alpha = 2 * e_charge; 
    
    
    double p = q_alpha * B * r;
    double lambda = h / p;
    
    cout << "Довжина хвилі де Бройля для альфа-частинки: " << scientific << lambda << " ì" << endl;
    
    return 0;
}
