CC=gcc 
CFLAGS= -fPIC -shared -Wall
LIBPATH := lib
SRCPATH := src

${SRCPATH}/libserial.so: ${SRCPATH}/serial.c 
	gcc ${CFLAGS} -o ${LIBPATH}/libserial.so ${SRCPATH}/serial.c 


