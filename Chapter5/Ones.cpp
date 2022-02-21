#include<stdio.h>
#include <iostream>
using namespace std;
int main() {
    int number = 0;
    int counter;
    while (cin >> number) {
        int m = number;
        counter = 0;
        while(m > 0) {

            while ( m % 10 == 1) {
                m = (int) m / 10;
                counter++;
            }

            if (m > 0) {
                m += number;
            }
        }
        printf("%d\n",counter);

    }
}