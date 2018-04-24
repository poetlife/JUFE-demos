#include<stdio.h>

void func1(){
    // how to use pointer
    
    int var1;
    int var2[10];
    
    printf("变量1的地址是:%p\n", &var1);
    printf("变量2的地址是:%p\n", &var2);
}

void func2(){
    int var = 20;  // 实际变量的声明
    int *ip;  // 指针变量的声明
    
    ip = &var;  // 在指针变量中存储var的地址
    
    printf("address of var variable: %p\n", &var);
    
    // 在指针变量中储存的地址
    printf("address stored in ip variable: %p\n", ip);
    
    // 使用指针访问值
    printf("value of *ip variable is %d\n", *ip);
}

void func3(){
    // 良好的编程习惯，在指针初始化的时候，赋值给NULL
    int *ptr = NULL;
    
    printf("ptr的值是：%d", ptr); // ptr的值是：0
}

// C指针的算术运算
void plusplus(){
    // 指针做 ++ 运算
    const int MAX = 3;
    int var[] = {12, 13, 14};
    int i, *ptr;
    
    /* 指针中的数组地址*/
    ptr = var;
    for (i=0; i<MAX; i++){
        printf("存储地址为var[%d]=%x\n", i, ptr);
        printf("存储值为var[%d]=%d\n", i, *ptr);
        
        // 移动到下一个位置
        ptr++;  // 由于是整数型的指针，因此下移一个是+4
    }
}

void subtractsubtract(){
    // 指针做 -- 运算
    const int MAX = 3;
    int var[] = {12, 13, 14};
    int i, *ptr;
    
    /* 指针中的数组地址*/
    ptr = &var[MAX-1];
    for (i=MAX; i>0; i--){
        printf("存储地址为var[%d]=%x\n", i, ptr);
        printf("存储值为var[%d]=%d\n", i, *ptr);
        
        // 移动到上一个位置
        ptr--;  // 由于是整数型的指针，因此下移一个是-4
    }
}


// 指针数组
void pointer_array(){
    const int MAX = 3;
    int var[] = {12, 13, 14};
    int i, *ptr[MAX];
    
    for (i=0; i<MAX; i++){
        ptr[i] = &var[i];  // 赋值为整数的地址
    }
    for (i=0; i<MAX; i++){
        printf("存储值为var[%d]=%d\n", i, *ptr[i]);
    }
}

#include <stdio.h>
#include <time.h>

void pointer_to_pointer(){
    // 这里使用指针指向指针
    int var;
    int *pt;
    int **ptr;  // 指向指针的指针
    
    var = 300;
    
    // 给指针赋值
    pt = &var;
    ptr = &pt;
    
    printf("the value of var is %d\n", var);
    printf("the value of pt is %d\n", *pt);
    printf("the value of ptr %d\n", **ptr);

}

void get_seconds(unsigned long *par);

void pointer_in_function(){
    unsigned long sec;
    
    get_seconds(&sec);
    
    // 输出实际值
    printf("the value of second is: %ld", sec);
}

void get_seconds(unsigned long *par){
    /*获取当前的秒数*/
    *par = time(NULL);
    return;
}

// 能接受指针作为参数的函数，也能接受数组作为参数
void get_average(int *arr, int size);

// 从函数返回指针、
int * myfunction();

/*
函数指针与回调函数
*/
int max(int x, int y){
    return x>y ? x : y;
}

void function_pointer(){
    /* p是函数指针 */
    int (*p)(int, int) = &max;  // &可以省略
    int a, b, c, d;
    
    printf("请输入3个数字：\n");
    scanf("%d %d %d", &a, &b, &c);
    d = p(p(a, b), c);
    
    printf("最大的数字为：%d", d);
}

// callback function 回调函数，即函数作为参数传递到另一个函数中
void populate_array(int *array, size_t arraySize, int (*getNextValue)(void)){
	for (size_t i=0; i<arraySize; i++){
		array[i] = getNextValue();
	}
}

// 返回随机值
int getNextRandomValue(void){
	return rand();
}

void callback(){
	int myArray[10];
	populate_array(myArray, 10, getNextRandomValue);
	for (int i=0; i<10; i++){
		printf("%d ", myArray[i]);
	}
}

int main(){
    
    pointer_array();
    return 0;
}
