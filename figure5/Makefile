CC=gcc -O2 -Wall -DMEMORY_STATS
all: ancestry2 full2 check2 process RandHHH2D 10RandHHH2D
ancestry2: ancestry2.c main2.c dim2.h prng.h alloc.h alloc.c Makefile
	$(CC) -DDIMENSION2 ancestry2.c main2.c prng.c alloc.c -o ancestry2 -lm
full2: ancestry2.c main2.c dim2.h prng.h alloc.h alloc.c Makefile
	$(CC) -DDIMENSION2 -DFULL_ANCESTRY ancestry2.c main2.c prng.c alloc.c -o full2 -lm
RandHHH2D: randhhh2D.c main2.c randhhh2D.h ulossycount.c ulossycount.h prng.h prng.c Makefile
	$(CC) -DRANDHHH -DDIMENSION2 randhhh2D.c ulossycount.c prng.c main2.c -o RandHHH2D -lm
10RandHHH2D: randhhh2D.c main2.c randhhh2D.h ulossycount.c ulossycount.h prng.h prng.c Makefile
	$(CC) -DRANDHHH -DVMULT=10 -DDIMENSION2 randhhh2D.c ulossycount.c prng.c main2.c -o 10RandHHH2D -lm
check2: check2.cpp Makefile
	g++ -ansi -Wall -O2 check2.cpp -o check2
process: process.c Makefile
	gcc -ansi -Wall -O2 process.c -o process

