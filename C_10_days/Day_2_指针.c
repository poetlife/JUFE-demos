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
    const MAX = 3;
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
    const MAX = 3;
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

int main(){
    
    subtractsubtract();
    return 0;
}
