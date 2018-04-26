#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

# define MAX_STAGE 10  // 关卡数
# define MIN_LEVEL 3
# define MAX_LEVEL 20  // 最大关卡数

/*
今天的任务是用于锻炼记忆力的“单纯记忆训练”和“加一记忆训练”等程序
*/

int sleep(unsigned long x){
	// 使系统停止x毫秒
	clock_t c1 = clock(), c2;

	do {
		if ((c2 = clock()) == (clock_t)-1){  // error
			return 0;
		}
	}while (1000.0 * (c2 - c1) / CLOCKS_PER_SEC < x);
	return 1;
}

void memory1(){
	int stage;
	int success = 0;
	clock_t start, end;

	srand(time(NULL));

	printf("来记忆一个4位数的数值吧。\n");

	start = clock();
	for (stage=0; stage<MAX_STAGE; stage++){
		int x;
		int no = rand() % 10000;

		printf("%d", no);
		fflush(stdout);
		sleep(500);

		printf("\r请输入：");
		fflush(stdout);
		scanf("%d", &x);

		if (x != no){
			printf("\athe answer is wrong\n");
		}else{
			printf("the answer is right!!\n");
			success++;
		}
	}
	end = clock();

	printf("%d次共答对了%d次，用时为%.2f秒。\n", MAX_STAGE, success, (double)(end - start)/CLOCKS_PER_SEC);
}

// 这的话需要注意到，rand() 返回的是整形，也就是16bit,最大能表示的数是2^16/2 -1 = 32767
// 当我们需要更大的数字时候，需要自己拼接起来
void memory2(){
	int stage;
	int level;
	int success = 0;
	clock_t start, end;

	srand(time(NULL));

	printf("来记忆一个4位数的数值吧。\n");

	do{
		printf("要挑战的等级(%d~%d):", MIN_LEVEL, MAX_LEVEL);
		scanf("%d", &level);
	} while(level > MAX_LEVEL || level < MIN_LEVEL);

	start = clock();
	for (stage=0; stage<MAX_STAGE; stage++){
		char no[MAX_LEVEL + 1];
		char x[MAX_LEVEL * 2];

		no[0] = '1' + rand() % 9;
		for (int i=1; i<level; i++){
			no[i] = '0' + rand() % 10;
		}
		no[level] = '\0';

		printf("%s", no);
		fflush(stdout);
		sleep(125 * level);

		printf("\r请输入：");
		fflush(stdout);
		scanf("%s", &x);

		if (strcmp(no, x) != 0){
			printf("\athe answer is wrong\n");
		}else{
			printf("the answer is right!!\n");
			success++;
		}
	}
	end = clock();

	printf("%d次共答对了%d次，用时为%.2f秒。\n", MAX_STAGE, success, (double)(end - start)/CLOCKS_PER_SEC);
}

// 单纯记忆训练，使用大小写英文字母
void memory3(){
	int stage;
	int level;
	int success = 0;
	clock_t start, end;
	const char ltr[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
					   "abcdefghijklmnopqrstuvwxyz";

	srand(time(NULL));

	printf("来记忆一个4位数的数值吧。\n");

	do{
		printf("要挑战的等级(%d~%d):", MIN_LEVEL, MAX_LEVEL);
		scanf("%d", &level);
	} while(level > MAX_LEVEL || level < MIN_LEVEL);

	start = clock();
	for (stage=0; stage<MAX_STAGE; stage++){
		char mstr[MAX_LEVEL + 1];
		char x[MAX_LEVEL * 2];

		for (int i=0; i<level; i++){
			mstr[i] = ltr[rand() % strlen(ltr)];
		}
		mstr[level] = '\0';

		printf("%s", mstr);
		fflush(stdout);
		sleep(125 * level);

		printf("\r%*s\r请输入：", level, "");
		fflush(stdout);
		scanf("%s", &x);

		if (strcmp(mstr, x) != 0){
			printf("\athe answer is wrong\n");
		}else{
			printf("the answer is right!!\n");
			success++;
		}
	}
	end = clock();

	printf("%d次共答对了%d次，用时为%.2f秒。\n", MAX_STAGE, success, (double)(end - start)/CLOCKS_PER_SEC);

}

// 储存空间的动态分配与释放


int main(){
	memory3();

	return 0;
}