CC ?= cc

.PHONY: all unitests clean
all: main rijndael.so 

main: rijndael.o c-aes/main.c
	$(CC) -o main c-aes/main.c rijndael.o

rijndael.o: c-aes/rijndael.c c-aes/rijndael.h
	$(CC) -o rijndael.o -fPIC -c c-aes/rijndael.c

rijndael.so: rijndael.o
	$(CC) -o rijndael.so -shared rijndael.o

unitests:
	python3 unit-tests/aes-tests.py

clean:
	@echo "Cleaning up....."
	rm -f *.o *.so
	rm -f main
	@echo "Cleaned up!"
