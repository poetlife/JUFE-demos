#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>

/*
出题者根据答题者的推测给予提示，循环进行这种对话形式的处理，直到答题者猜对答案为止
*/

void make4digitals(int x[]){
	int i, j, val;

	for (int i = 0; i < 4; i++)
	{
		do {
			val = rand() % 10;
			for (j=0; j<i; j++){
				if (val == x[j]){
					break;
				}
			}
		} while(j < i);
		x[i] = val;
	}
}

/*
atoi 把字符串转换为int型的数字 defined in <stdlib.h>
对应的atol to long
atof to double
*/
void read_value(){
	// 因为直接使用scanf会直接将输入的值转为数字型，比如将0234转换为234，因此我们直接读取字符串
	char temp[20];

	printf("请输入整数: ");
	scanf("%s", temp);
	printf("你输入了%d.\n", atoi(temp));
}

int check(const char s[]){
	int i, j;

	if (strlen(s) != 4){
		return 1;
	}
	for (i=0; i<4; i++){
		if (!isdigit(s[i])){
			return 2;
		}
		for (j=0; j<i; j++){
			if (s[i] == s[j]){
				return 3;
			}
		}
	}
	return 0;
}

void judge(const char s[], const int no[], int *hit, int *blow){
	int i, j;

	*hit = *blow = 0;
	for (i=0; i< 4; i++){
		for (j=0; j<i; j++){
			if (s[i] == '0' + no[j])  // 数字一致
				/*
				这里需要注意一下，因为这里的话是将0作为base去得到target的编码
				*/
				if (i == j)
					(*hit)++;  // 位置也一致
				else
					(*blow)++;
		}
	}
}


// 更深层次的指针的使用
void add(int x, int y, int total){
	total = x + y;
}

void add2(int x, int y, int *total){
	*total = x + y;
}

void print_result(int snum, int spos){
	if (spos == 4)
	{
		printf("回答正确");
	}
	else if(snum == 0){
		printf("    这些数字里没有答案数字\n");
	}
	else{
		printf("    这些数字里面包括%d个答案数字\n", snum);

		if (spos == 0){
			printf("    但是数字的位置都不一致\n");}
		else{
			printf("    其中有%d个数字的位置是一致的\n", spos);
		}
	}
	putchar('\n');
}

int main(){
	// int x[4];
	// make4digitals(x);
	// for (int i=0; i<4; i++){
	// 	printf("%d ", x[i]);
	// }

	// char x[] = "123";
	// printf("%d\n", check(x));

	/*
	int x = 5, y = 6, total = 0;
	add(x, y, total);
	printf("the total is: %d\n", total);
	这样子运行，并不会将total的值改变，这里的话实际上是解释器将x,y,total的副本传递到了函数中去了，所以这里不能这样子使用
	int x = 5, y = 6, total = 0;
	add2(x, y, &total);
	printf("the sum is: %d\n", total); 
	这样子才能正常使用
	*/
	int try_no = 0;
	int chk;
	int hit;
	int blow;
	int no[4];
	char buff[10];
	clock_t start, end;

	srand(time(NULL));

	puts("◆ 来玩珠玑妙算吧。");
	puts("◆ 猜猜4个数字。");
	puts("◆ 其中不包含相同数字。");
	puts("◆ 请像4307这样连续输入数字。");
	puts("◆ 不能输入空格字符。\n");

	make4digitals(no);

	for (int k=0; k<4; k++){
		printf("%d", (no[k]));
	}
	putchar('\n');

	start = clock();

	do{
		do{
			printf("请输入：");
			scanf("%s", buff);

			chk = check(buff);

			switch (chk){
				case 1: puts("\a请确保输入4个字符。"); break;
				case 2: puts("\a请不要输入除了数字以外的字符。"); break;
				case 3: puts("\a请不要输入相同的数字"); break;
			}
		} while (chk != 0);

		try_no++;
		judge(buff, no, &hit, &blow);
		print_result(hit + blow, hit);
	}while(hit < 4);

	end = clock();

	printf("用了%d次。\n用时%1.f秒。\n", try_no, (double)(end - start)/CLOCKS_PER_SEC);
	return 0;
}