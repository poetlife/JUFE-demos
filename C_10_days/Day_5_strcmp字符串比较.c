#include <string.h>
#include <stdio.h>

// how to use strcmp() and strncmp()

void one(){
	char x[] = "ab";
	char y[] = "ba";

	int result;

	result = strcmp(x, y);

	printf("the result is %d\n", result);  // -1
}

void two(){
	char x[] = "bb";
	char y[] = "ba";

	int result;

	result = strncmp(x, y, 1);

	printf("the result is %d\n", result);  // 0, means equal
}

int main(){
	one();
	two();
	return 0;
}