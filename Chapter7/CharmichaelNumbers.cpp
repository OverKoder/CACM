#include<iostream>
#include<cstring>
using namespace std;

/*
For some reason, this code gets time limit exceeded. And considering there only a few Charmichael numbers less
than 65000, we're just going to approach this in a bolder way
#define N 65000

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
int expmod (int a , int n , int m ) { 
    int i = n ;
    int r = 1;
    int x = a ;

    while ( i > 0) {

        if ( i %2 == 1) 
            r = ( r * x) %m ;

        x = ( x * x) %m ;
        i /= 2;
    }
    
    return r ;
}




int main() {
    int n;
    bool pass_Fermat = true;
    SieveOfEratosthenes(N);


    while ( scanf("%d",&n) == 1 && n != 0) {
        pass_Fermat = true;
        for (int a = 2; a < n && pass_Fermat; a++) {
            pass_Fermat = expmod(a, n, n) == a;
        } 
        // Some special cases are added
        if ( (pass_Fermat and !prime[n]) || n == 46657 || n == 52633 || n == 62745 || n == 63973)
            printf("The number %d is a Carmichael number.\n",n);
        else
            printf("%d is normal.\n",n);
    }
}
*/

int main() {
    // Yes, precomputed charmichael numbers, where is your god now?
    int charmichael [15] = {561, 1105 ,1729 ,2465 ,2821 ,6601 ,8911 ,10585 ,15841 ,29341 ,41041 ,46657 ,52633 ,62745 ,63973 };
    int n, i;

    while ( scanf("%d",&n) == 1 && n != 0) {

        for (i = 0; i < 15 && charmichael[i] != n; i++);

        if (i < 15)
            printf("The number %d is a Carmichael number.\n",n);
        else
            printf("%d is normal.\n",n);

        
    }
}