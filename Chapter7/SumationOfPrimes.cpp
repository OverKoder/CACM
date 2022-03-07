
#include<iostream>
#include<cstring>
using namespace std;

#define N 7500000

bool prime[N];
void SieveOfEratosthenes(int n)
{

    memset(prime, true, sizeof(prime));
 
    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true)
        {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }

    return;
}
 
int main()
{
    SieveOfEratosthenes(N);

    int n, aux;
    int p1,p2,p3,p4;
    while (scanf("%d",&n) == 1) {

        if (n < 8) {
            printf("Impossible.\n");
            continue;
        }

        p1 = n / 4;
        while (!prime[p1])
            p1--;

        aux = n - p1;

        if (aux % 2 == 0)
            p2 = 2;

        else
            p2 = 3;

        aux -= p2;

        p3 = 2; p4 = aux - 2;
        while (! (prime[p3] && prime[p4]) ) {
            p3++; p4--;
        }

        printf("%d %d %d %d\n",p1,p2,p3,p4);
         


    }
    return 0;
}