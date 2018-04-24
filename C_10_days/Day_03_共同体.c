#include<stdio.h>
#include<string.h>

// 共同体  看定义和结构体区分开来
/* 
共用体是一种特殊的数据类型，允许您在相同的内存位置存储不同的数据类型。您可以定义一个带有多成员的共用体，但是任何时候只能有一个成员带有值。共用体提供了一种使用相同的内存位置的有效方式。
*/

void union_function(){
	union Data{
		int i;
		float j;
		char f[20];
	} data;
	data.i = 1;
	data.j = 2.65;
	strcpy(data.f, "C programming");

	printf( "data.i : %d\n", data.i);
   	printf( "data.j : %f\n", data.j);
   	printf( "data.f : %s\n", data.f);

   	// 这样是输出不了正确的数据的，原因在与后面 不断对这个位置进行写入操作，即会抹去原来的
}

int main(){
	union_function();
	return 0;
}
