#include<iostream>

#include <cmath>
#include <list>

using namespace std;

typedef pair<uint64_t, int> prime_factor;

list<prime_factor> * primeFactorization_v2(uint64_t n)
{
    list<prime_factor> *factors = new list<prime_factor>();
    int i, ii;

    prime_factor pf(2, 0);
    while ((n % 2) == 0) {
        n /= 2;
        pf.second ++;
    }
    if (pf.second > 0) factors->push_back(pf);

    i = 3;
    ii = i * i;
    while (ii <= n) {

        pf.first = i;
        pf.second = 0;

        while ((n % i) == 0) {
            pf.second ++;
            n /= i;
        }
        if (pf.second > 0) factors->push_back(pf);

        ii += (i << 2) + 4;
        i += 2;
    }

    if (n > 1) factors->push_back(prime_factor(n, 1));

    return factors;
}

int main(){
    int n,m,e;
    uint64_t p,aux;
    while ( scanf("%d%d",&n,&m) == 2){

        if (m < 2 || m < n) {
            printf("%d divides %d!\n",m,n);
            continue;
        }
        if (n < 2) {
            printf("%d does not divide %d!\n",m,n);
            continue;
        }




        list<prime_factor> *pf = primeFactorization_v2(m);

        for (auto it = pf->begin(); it != pf->end(); it++) {
            p = it -> first;
            e = it -> second;

            for (uint64_t x = p; x <= n && e > 0; x += p) {
                aux = x;
                while (aux % p == 0  && e > 0) {
                    aux = aux / p;
                    e--;
                }
            }
            if (e > 0) {
                printf("%d does not divide %d!\n",m,n);
                break;
            }
                
            
        }
        if (e == 0)
            printf("%d divides %d!\n",m,n);
            
    } 
} 