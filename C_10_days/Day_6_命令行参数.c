#include <stdio.h>

int main(int argc, char *argv[]){
	// argc argument count
	// argv argument vector 接受程序名和程序形式参数
	for (int i=0; i<argc; i++){
		printf("i[%d]=%s\n", i, argv[i]);
	}
	return 0;
}