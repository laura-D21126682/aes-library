CC ?= cc

.PHONY: all
all: main rijndael.so

main: rijndael.o c-aes/main.c
	$(CC) -o main c-aes/main.c rijndael.o

rijndael.o: c-aes/rijndael.c c-aes/rijndael.h
	$(CC) -o rijndael.o -fPIC -c c-aes/rijndael.c

rijndael.so: rijndael.o
	$(CC) -o rijndael.so -shared rijndael.o

clean:
	rm -f *.o *.so
	rm -f main
