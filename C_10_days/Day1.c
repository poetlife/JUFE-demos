#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// day 01 猜数游戏

// know about the scanf() and the \a
void version1(){
	int no;
	int ans = 7;

	printf("%s\n", "try to guess a number between 0 and 9.");
	scanf("%d", &no);  // here use pointer?!

	if (no > ans){
		printf("\a%s\n", "a litter smaller...");  // \a 表示系统弹出提示音
	}
	else if (no < ans){
		printf("\a%s\n", "a litter bigger...");
	}
	else{
		printf("%s\n", "your answer is totally correct!");
	}
}


// version2
// do loop
void version2(){
	int no;
	int ans = 7;

	printf("%s\n", "try to guess a number between 0 and 9.");

	do {
		printf("%s\n", "enter the number you guess: ");
		scanf("%d", &no);  // here use pointer?!
		if (no > ans){
			printf("\a%s\n", "a litter smaller...");  // \a 表示系统弹出提示音
		}
		else if (no < ans){
			printf("\a%s\n", "a litter bigger...");
		}	
	} while (no != ans);
	printf("%s\n", "your answer is totally correct!");
}


// version 3
// use while to replace do loop in version 2
void version3(){
	int no;
	int ans = 7;

	printf("%s\n", "try to guess a number between 0 and 9.");

	while (1) {
		printf("%s\n", "enter the number you guess: ");
		scanf("%d", &no);  // here use pointer?!
		if (no > ans){
			printf("\a%s\n", "a litter smaller...");  // \a 表示系统弹出提示音
		}
		else if (no < ans){
			printf("\a%s\n", "a litter bigger...");
		}
		else{
			printf("%s\n", "your answer is totally correct!");
			break;
		}
	}
}


// version 4 生成随机数，相应的函数在<stdlib.h>中
// rand()
void version4(){
	int retry;  // once more?
	printf("the system will generate a int random number between 0 and %d.\n", RAND_MAX);  // RAND_MAX was defined in the <stdlib.h>
	do {
		printf("the random number is: %d\n", rand());
		printf("%s\n", "once more? no(0) yes(1)");
		scanf("%d", &retry);
	} while (retry == 1);
}


// version 5
// 随机数种子，使用时间作为随机数的种子，从而避免生成相同的随机序列
// srand() time()
void version5(){
	int retry;
	srand(time(NULL));  // 根据当前时间设置种子值
	printf("the system will generate a int random number between 0 and %d.\n", RAND_MAX);
	do {
		printf("the random number is: %d\n", rand());
		printf("%s\n", "once more? no(0) yes(1)");
		scanf("%d", &retry);
	} while (retry == 1);
}


// restric the times of trying and restric the range of rand()
void version6(){
	int no;
	int ans;

	srand(time(NULL));
	ans = rand() % 21;  // the random number is between 0 and 20
	const int max_stage = 10;
	int remain = max_stage;

	printf("try to guess a number between 0 and %d. and you will have %d chances.\n", 20, max_stage);

	while (remain >= 1) {
		printf("%s\n", "enter the number you guess: ");
		scanf("%d", &no);  // here use pointer?!
		if (no > ans){
			printf("\a%s\n", "a litter smaller...");  // \a 表示系统弹出提示音
		}
		else if (no < ans){
			printf("\a%s\n", "a litter bigger...");
		}
		else{
			printf("%s\n", "your answer is totally correct!");
			break;
		}
		remain -= 1;
		printf("remain/total : %d/%d\n", remain, max_stage);
	}
	if (remain < 1){
		printf("out of chances...\n");
	}
}


// version 7
// 保存输入记录
// array
void version7(){
	int i;
	int stage;  // 已经输入的次数
	int no;
	int ans;
	const int max_stage = 10;
	int num[max_stage];  // array[int]

	srand(time(NULL));
	ans = rand() % 1000;

	printf("猜一个0~999之间的数字\n");

	stage = 0;
	do {
		printf("还剩%d次机会。是多少呢:\n", max_stage - stage);
		scanf("%d", &no);
		num[stage++] = no;

		if (no > ans){
			printf("\a再小一点。\n");
		} else if(no < ans){
			printf("\a再大一点。\n");
		}
	} while (no != ans && stage < max_stage);

	if (no != ans){
		printf("\a很遗憾，正确答案是%d\n", ans);
	}
	else{
		printf("回答正确\n");
		printf("您一共使用了%d次猜中了\n", stage);
	}

	puts("\n--- 输入记录 ---");
	for (i=0; i<stage; i++){
		printf("%2d : %4d %+4d\n", i+1, num[i], num[i]-ans);
	}
}

int main(){
	version7();
	
	return 0;
}
