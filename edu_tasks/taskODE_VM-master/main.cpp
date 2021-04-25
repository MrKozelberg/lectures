//Runge-Kutta 4th with h = const
#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>
#include <iomanip>

using namespace std;
const double h = 0.0001;
const double y_0 = 0.;
const double v_0 = 1.;

//class of 2D-vectors
class R2
{
public:
    double x = 0.;
    double y = 0.;
    friend const R2 operator+(const R2& left, const R2& right);
    friend const R2 operator*(const double& number, const R2& right);
    friend const R2 operator/(const R2& left, const double& number);
};

const R2 operator+(const R2& left, const R2& right)
{
    R2 sum;
    sum.x = left.x + right.x;
    sum.y = left.y + right.y;
    return sum;
}

const R2 operator*(const double& number, const R2& right)
{
    R2 comp;
    comp.x = number * right.x;
    comp.y = number * right.y;
    return comp;
}

const R2 operator/(const R2& left, const double& number)
{
    R2 acomp;
    acomp.x = left.x / number;
    acomp.y = left.y / number;
    return acomp;
}

R2 function(R2 U)
{
    R2 F;
    F.x = U.y;
    F.y = -sin(U.x);
    return F;
}

int main()
{
    ofstream fout;
    fout.open("/home/mrkozelberg/WORK/task06_ODE_Kozlov/exit.txt");
    fout << "X  " << "Y " <<"Y' " << endl;
    R2 U, k1, k2, k3, k4;
    U.x = y_0; U.y = v_0;
    fout << fixed << setprecision(6) << 0. << "\t" << U.x << "\t" << U.y << endl;
    for (double x = 0; x < 3 * M_PI; x += h)
    {
        k1 = h * function(U);
        k2 = h * function(U + 0.5 * k1);
        k3 = h * function(U + 0.5 * k2);
        k4 = h * function(U + k3);
        U = U + ((k1 + (2 * (k2 + k3))) + k4)/6;//error = O(h^5)
        fout << x + h << "\t" << U.x << "\t" << U.y << endl;
    }
    fout.close();
    return 0;

}
