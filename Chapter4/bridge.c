#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_P	1000
#define MAX_S	100

int	times[ MAX_P ];
int people[ MAX_S ];
int tests, n;


void process_number( char *s , int *t) 
{
	char *p;
	while( *s != '\0' ) {
		
		while( *s != '\0'  &&  !isdigit( *s ) ) s++;
		p=s;
		while( *s != '\0'  &&  isdigit( *s ) ) s++;
		*s='\0';
		if ( p < s ) *t = atoi( p );
		s++;
	}
}

void sorted()
{
	int i, j, k;
	for (i = 0; i < n; i++) {
		people[times[i]-1]++;
	}
	k = 0;
	for (i = 0; i < MAX_S; i++) {
		while (people[i] > 0) {
			times[k] = i+1;
			people[i]--;
			k++;
		}
	}
}

void solve(int n)
{
	int total;
	total = times[0];
	while( n > 3 ) {
		if ( 2*times[1] > times[0]+times[n-2] ) {
			total += 2*times[0]+times[n-2]+times[n-1];
		}
		else {
			total += times[0]+2*times[1]+times[n-1];
		}
		n -= 2;
	}
	if ( n == 3 ) {
		total += times[1]+times[2];
	}
	else if ( n == 2 ) {
		total += times[1]-times[0];
	}
	fprintf( stdout, "%d\n", total );
}

void track(int n)
{
	while( n > 3 ) {
		if ( 2*times[1] > times[0]+times[n-2] ) {
			fprintf( stdout, "%d %d\n", times[0], times[n-1] );
			fprintf( stdout, "%d\n", times[0] );
			fprintf( stdout, "%d %d\n", times[0], times[n-2] );
			fprintf( stdout, "%d\n", times[0] );
		}
		else {
			fprintf( stdout, "%d %d\n", times[0], times[1] );
			fprintf( stdout, "%d\n", times[0] );
			fprintf( stdout, "%d %d\n", times[n-2], times[n-1] );
			fprintf( stdout, "%d\n", times[1] );
		}
		n -= 2;
	}
	if ( n == 3 ) {
		fprintf( stdout, "%d %d\n", times[0], times[2] );
		fprintf( stdout, "%d\n", times[0] );
		fprintf( stdout, "%d %d\n", times[0], times[1] );		
	}
	else if ( n == 2 ) {
		fprintf( stdout, "%d %d\n", times[0], times[1] );
	}
	else if ( n == 1 ) {
		fprintf( stdout, "%d\n", times[0] );
	}
}

int main( int arc, char *argv[] )
{
	int i, j;
	char buffer[1024];

	fgets( buffer, 1020, stdin );
	process_number( buffer , &tests );
	for(i = 0; i < tests; i++) {
		fgets( buffer, 1020, stdin );
		fgets( buffer, 1020, stdin );
		process_number( buffer , &n );
		
		for(j = 0; j < n; j++) {
			fgets( buffer, 1020, stdin );
			process_number( buffer, &times[j] );	
		}

		sorted();
		solve(n);
		track(n);
		if ( i != tests-1 )
			fprintf( stdout, "\n" );
	}
	return 0;
}
