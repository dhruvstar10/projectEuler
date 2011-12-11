/**************************************************************
 *
 *	tutor.c
 *
 *	Tutoring program to explain usage for various
 * 	giants.[ch] functions.
 *
 *	Updates:
 *    20 Apr 03 REC (fixed comments, thanks to J.J.Nielsen)
 *		26 Apr 97 REC (Creation)	
 *
 *	c. 1997 Perfectly Scientific, Inc.
 *	All Rights Reserved.
 *
 *	Compile and run with, e.g.:
 *
 *	% cc -O tutor.c giants.c
 *	% a.out
 *
 * 	and type in various giant integers as prompted.
 *
 **************************************************************/


/* include files */

#include <stdio.h>
#include <stdlib.h>
#include "giants.h"


/* compiler options */

#ifdef _WIN32
#pragma warning( disable : 4127 ) /* disable conditional is constant warning */
#endif


/* function prototypes */

void 		grammarmulg(giant a, giant b);


/**************************************************************
 *
 *	Main Function
 *
 **************************************************************/

void
main(
	void
)
{
	giant 		x = newgiant(INFINITY), y = newgiant(INFINITY),
				p = newgiant(INFINITY), r = newgiant(100);
	int 		j;

   	printf("Give two integers x, y on separate lines:\n");
   	gin(x); 
   	gin(y); 

   	gtog(y, p);  /* p := y */
   	mulg(x, p);
   	printf("y * x = "); 
   	gout(p);

  	gtog(y, p);
   	subg(x, p);
   	printf("y - x = "); 
   	gout(p);

   	gtog(y, p);
   	addg(x, p);
   	printf("y + x = "); 
   	gout(p);

   	gtog(y, p);
   	divg(x, p);
   	printf("y div x = "); 
   	gout(p);

   	gtog(y, p);
   	modg(x, p);
   	printf("y mod x = "); 
   	gout(p);

   	gtog(y, p);
   	gcdg(x, p);
   	printf("GCD(x, y) = "); 
   	gout(p);
 
	/* Next, test which of x, y is greater. */
   	if (gcompg(x, y) < 0 ) 
   		printf("y is greater\n");
	else if (gcompg(x,y) == 0) 
		printf("x, y equal\n");
	else 
		printf("x is greater\n");

	/* Next, we see how a giant struct is comprised.
   	 * We make a random, bipolar number of about 100 
   	 * digits in base 65536. 
   	 */
	for (j=0; j < 100; j++) 
	{  /* Fill 100 digits randomly. */
		r->n[j] = (unsigned short)rand();
   	}
   	r->sign = 100 * (1 - 2*(rand()%2));

	/* Next, don't forget to check for leading zero digits,
     * even though such are unlikely. 
     */
   	j = abs(r->sign) - 1;
   	while ((r->n[j] == 0) && (j > 0)) 
   	{
   		--j;
   	}
   	r->sign = (j+1) * ((r->sign > 0) ? 1: -1);
   	printf("The random number: "); gout(r);

	/* Next, compare a large-FFT multiply with a standard,
     * grammar-school multiply. 
     */
   	itog(1, x); 
   	gshiftleft(65536, x); 
   	iaddg(1, x);
   	itog(5, y); 
   	gshiftleft(30000, y); 
   	itog(1, p); 
   	subg(p, y); 
	/* Now we multiply (2^65536 + 1)*(5*(2^30000) - 1). */
   	gtog(y, p);
   	mulg(x, p);  /* Actually invokes FFT method because
					bit lengths of x, y are sufficiently large. */
   	printf("High digit of (2^65536 + 1)*(5*(2^30000) - 1) via FFT mul: %d\n", (int) p->n[abs(p->sign)-1]);
   	fflush(stdout);
   	gtog(y, p);
   	grammarmulg(x, p);  /* Grammar-school method. */
   	printf("High digit via grammar-school mul: %d\n", (int) p->n[abs(p->sign)-1]);
   	fflush(stdout);

	/* Next, perform Fermat test for pseudoprimality. */
   	printf("Give prime candidate p:\n");
   	gin(p); 
   	gtog(p, y);
   	itog(1, x); subg(x, y);
   	itog(2, x);
   	powermodg(x, y, p);
   	if (isone(x)) 
   		printf("p is probably prime.\n");
	else 
		printf("p is composite.\n");
}

