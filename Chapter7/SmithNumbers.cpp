#include<iostream>
#include<cstring>
#include <cmath>
#include <list>

using namespace std;

int digitSum (int n) {

    int sum = 0;
    while (n >= 10) {
        sum += n % 10;
        n = n / 10;
    }

    sum += n;
    return sum;
}

list<int> * primeFactorization(int n)
{
    list<int> *factors = new list<int>();
    int i, ii;

    while ((n % 2) == 0) {
        factors->push_back(2);
        n /= 2;
    }

    i = 3;
    ii = i * i;
    while (ii <= n) {

        if ((n % i) == 0) {
            factors->push_back(i);
            n /= i;
        } else {
            ii += (i << 2) + 4;
            i += 2;
        }
    }

    if (n > 1) factors->push_back(n);

    return factors;
}

int main() {
    int cases, n,aux, digitsum;
    list<int> *factors;
    scanf("%d",&cases);

    for (int i = 0; i < cases; i++) {
        scanf("%d",&n);


        do {
            n++; digitsum = 0;
            factors = primeFactorization(n);
            for (auto it = factors->begin(); it != factors->end(); it++) {
                aux = *it;
                if (aux == n)
                    continue;

                digitsum += digitSum(aux);
            }
           
        } while (digitSum(n) != digitsum);

        printf("%d\n",n);

    }
}