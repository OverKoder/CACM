#include <stdio.h>
using namespace std;

int memoization [1000000];

int collatz(int n) {
    int level = 1;
    while (n != 1)  {

        if (n < 1000000 && memoization[n] != 0) {
            return memoization[n] + level - 1;
        }
        if (n % 2 == 0) {
            n = n / 2;
        }
        else
            n = 3*n + 1;
        
        level++;
    }
    return level;
}

int max_cycle_length(int lower, int higher) {
    if (lower > higher) {
        return max_cycle_length(higher,lower);
    }
    int i, cl, max = 0;
    for (i = lower; i <= higher; i++) {

        cl = collatz(i);
        memoization[i] = cl;
        if (cl > max)
            max = cl;

    }

    return max;

}
int main(int argc, char * argv[]) {
    int lower, higher, max;
    while (scanf("%d%d", &lower, &higher) == 2) {
        max = max_cycle_length(lower,higher);
        printf("%d %d %d\n",lower,higher,max);
    }

}