#include <stdio.h>

double power_float(double x, double k, int recursion);
double dichotomie(double x, double k, int recursion);
double power_int(double x, int n);

double my_abs(double x){
    if(x < 0) return - x;
    else return x;
}

double power_int(double x, int n){
    double total = 1;
    for(int i = 0; i < n; i++){
        total *= x;
    }
    return total;
}

double dichotomie(double x, double k, int recursion){
    double max_val;
    if(x < 1) max_val = 1;
    else max_val = x;
    double min_val = 0;
    double mid;
    while(1){
        mid = (max_val + min_val) / 2;
        double f = power_float(mid, k, recursion);
        if(my_abs(x - f) < 0.0000001) return mid;
        else if(f > x) max_val = mid;
        else min_val = mid;
    }
}

double power_float(double x, double k, int recursion){
    int n = (int)k;
    double l = k - n;
    if(recursion == 0){
        return power_int(x, n);
    }
    else if(l <= 0.001){
        return power_int(x, n);
    }
    else if(l >= 0.99){
        return power_int(x, n + 1);
    }
    else{
        return power_int(x, n) * dichotomie(x, 1/l, recursion - 1);
    }
}

int main(){
    double x = 2;
    double k = 0.56659;
    double result = power_float(x, k, 6);
    printf("%lf", result);
    return 0;
}
