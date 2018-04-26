#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "string.h"

/*
我们再来编写一个程序，能让玩家在游戏开始时自行决定训练次数，同时储存所有答对的数量。
*/

/*
变量的声明必须在语句面前，包括数组的声明
所以嘛，才出现了calloc()函数malloc()和realloc()嘛
这两个函数能从专门留出的空间中分配储存空间，这些空闲空间一般称为heap(堆)
free()释放空间
*/

// void *calloc(size_t nmemb size_t size) 为nmemb个大小为size字节的对象分配储存空间，该空间内的所有位都会初始化为0
void use_calloc(){
	double *x;
	x = calloc(1, sizeof(double));
	/*
	calloc, malloc返回的指针都是指向void型的指针，这是一种特殊的指针，可以指向任意类型的对象，
	*/
	free(x);
}

void dynamic1(){
	int *x;
	x = calloc(1, sizeof(int));

	if (x == NULL)
		puts("存储空间分配失败。");
	else{
		*x = 57;
		printf("*x = %d\n", *x);
		free(x);
	}	
}

void dynamic2(){
	int *x;
	// x = calloc(1, sizeof(int));  // 这里发生了隐式类型转换，而这我们也可以使用强制类型转换,c++中强制使用
	x = (int *)calloc(1, sizeof(int));  // C艹这样做是为了，加快速度
	// 但这几个函数会自动将地址转换为能被8整除的，因此，不需要强制类型转换

	if (x == NULL)
		puts("存储空间分配失败。");
	else{
		printf("输入一个一位的数字：");
		scanf("%d", x);
		printf("*x = %d\n", *x);
		free(x);
	}	
}

void dynamicary(){
	/*
	为整数数组动态分配储存空间
	*/
	int *x;
	int n;

	printf("要分配元素个数为：");
	scanf("%d", &n);

	x = calloc(n, sizeof(int));

	if (x == NULL)
		puts("存储空间分配失败。");
	else{
		int i;
		for(i=0; i<n; i++){
			x[i] = i;
		}
		for (i=0; i<n; i++){
			printf("x[%2d]=%2d\n", i, x[i]);
		}
		free(x);
	}	
}


int main(){
	dynamicary();
	return 0;
}
