/*These are the functions needed to communicate via 
 * the UART on windows 
 * Data modified : 25/06/2020 
 * Author: Olasoji Makiwna 
 */

#include <Windows.h>
#include <stdio.h>
HANDLE hComm;
DCB dcbSerialParams = {0};
COMMTIMEOUTS timeouts = {0};
/*Open the com port */
WINAPI int open_port(char * port_name){
	hComm = CreateFile(port_name,
			   GENERIC_READ | GENERIC_WRITE, 
			   0,
			   NULL,
			   OPEN_EXISTING, 
			   0, 
			   NULL) ;
	if(hComm == INVALID_HANDLE_VALUE){
		return -1; 
	}else{
		SetCommMask(hComm,EV_RXCHAR);
		return  0; 
	}
	
}
/*Set the UART settings */
WINAPI int conf_port(unsigned int baud_rate, 
		     unsigned char byte_size,
		     unsigned char stop_bit,
		     unsigned char parity){
	/*Configure the uart with basic settings 
	 * The reset aren't really important  */ 
	dcbSerialParams.DCBlength = sizeof (dcbSerialParams);
	dcbSerialParams.BaudRate = baud_rate;
	dcbSerialParams.ByteSize = byte_size; 
	dcbSerialParams.StopBits = stop_bit;
	dcbSerialParams.Parity   = parity;

	/* Load the configuration */
	SetCommState(hComm,&dcbSerialParams);
	return 0 ;	
}

WINAPI int set_timeouts(){
	/* Timeouts in milliseconds */
	timeouts.ReadIntervalTimeout         = 50; 
	timeouts.ReadTotalTimeoutConstant    = 50; 
	timeouts.ReadTotalTimeoutMultiplier  = 10; 
	timeouts.WriteTotalTimeoutConstant   = 50; 
	timeouts.WriteTotalTimeoutMultiplier = 10; 
	SetCommTimeouts(hComm,&timeouts);
    	return 0; 
}

/*Write N-Bits via the UART */
WINAPI int write_port(char * data){
	unsigned long num_bytes = sizeof(data);
	unsigned long num_bytes_sent;
	WriteFile(hComm,data,num_bytes,&num_bytes_sent,NULL);
	return 0;
}


DWORD event;
int status;
char serial_buffer[255];
char rx;
int i = 0; 
/*Load buffer with data and return how many characters 
 * were sent */
WINAPI int read_port(char * buffer,size_t size){
		
	DWORD num_bytes;	
	ReadFile(hComm, buffer, size, &num_bytes, NULL);
	return num_bytes;
}
/*Close the com port */
WINAPI int close_port(){
	return CloseHandle(hComm);
}
