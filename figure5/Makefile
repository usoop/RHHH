CC=gcc -O2 -Wall -DMEMORY_STATS
all: ancestry2 full2 check2 process
ancestry2: ancestry2.c main2.c dim2.h prng.h alloc.h alloc.c Makefile
	$(CC) -DDIMENSION2 ancestry2.c main2.c prng.c alloc.c -o ancestry2 -lm
full2: ancestry2.c main2.c dim2.h prng.h alloc.h alloc.c Makefile
	$(CC) -DDIMENSION2 -DFULL_ANCESTRY ancestry2.c main2.c prng.c alloc.c -o full2 -lm
check2: check2.cpp Makefile
	g++ -ansi -Wall -O2 check2.cpp -o check2
process: process.c Makefile
	gcc -ansi -Wall -O2 process.c -o process

