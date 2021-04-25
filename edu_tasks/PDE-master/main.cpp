//PDE:  u_t = u_xx + delta(x)
//Popykina, Kozlov

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

const unsigned N = 35;
      double delta_x = 2. / (N - 1); // [-1, 1] dividing by N points; x_n = -1 + n * delta_x, n runs from 0 to N - 1
const double delta_t = 0.001;
const double T = 1; //T_max
      double q = delta_t / (delta_x * delta_x);

//approximation of delta-function: delta(x) ~ f(x)
double f(double x){
    double k = 1 / (delta_x);
    if (x < delta_x and x > -delta_x){
            return k;
        } else {
            return 0;
        }
}

void SOLUTION(){
    double OLD[N], NEW[N];
    ofstream fout;
    fout.open("/home/mrkozelberg/WORK/task08_PDE_Kozlov/data.txt");
    //fout << "PDE";
    fout << "T  X   U";
    for (unsigned j = 0; j < N; ++j){
        OLD[j] = 0;
        //fout << "   " << - 1 + j * delta_x;
    }
    unsigned sch = 0;
    for (double t = 0; t <= T; t += delta_t){
        //fout << "\n" << t;
      ++sch;
        for (unsigned i = 0; i < N; ++i){
            if (sch % 5 == 1){
                fout << "\n" << t << "   " << -1 + i * delta_x << "   " << OLD[i];
            }
            if (i < N - 1 and i > 0){
                NEW[i] = OLD[i] + q * (OLD[i + 1] - 2 * OLD[i] + OLD[i - 1]) + delta_t * f(-1 + i * delta_x) - 0 * delta_t; //ATTENTION!
            } if (i == 0){
                NEW[0] = OLD[0] + 2 * q * (OLD[1] - OLD[0]);
            } if (i == N - 1) {
                NEW[N - 1] = OLD[N - 1] + 2 * q * (OLD[N - 2] - OLD[N - 1]);
            }
        }
        for (unsigned j = 0; j < N; ++j){
            OLD[j] = NEW[j];
        }
        fout << endl;
    }
    fout.close();
}

int main(){
    cout << "q = " << q << endl;
    if (q < 0.5){
        SOLUTION();
        return 0;
    } else {
        return 1;
    }
}
