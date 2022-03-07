
#include<iostream>
#include<stdio.h>
using namespace std;
/*
    Euclides algorithm for computing gcd(a,b) and x,y such that a*x + b*y = gcd(a, b)
*/

#include <cstdio>
#include <cmath>

int gcd(int a, int b, int *x, int *y)
{
    int g, x1, y1;
    if (b > a) return gcd(b, a, y, x);
    
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }

    g = gcd(b, a%b, &x1, &y1);

    *x = y1;
    *y = (x1 - std::floor(a / b) * y1);

    return g;
}

int main() {
    int a ,b;
    int g, x, y;
    while ( scanf("%d%d",&a,&b) == 2){
        g = gcd(a,b,&x,&y);
        printf("%d %d %d\n",x,y,g);
    }
}