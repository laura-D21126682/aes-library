CC ?= cc

.PHONY: all
all: main rijndael.so

main: rijndael.o aes/main.c
	$(CC) -o main aes/main.c rijndael.o

rijndael.o: aes/rijndael.c aes/rijndael.h
	$(CC) -o rijndael.o -fPIC -c aes/rijndael.c

rijndael.so: rijndael.o
	$(CC) -o rijndael.so -shared rijndael.o

clean:
	rm -f *.o *.so
	rm -f main
