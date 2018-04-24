#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <ctype.h>


/*
	本章，我们要编写一个提供两位玩家对战的“猜拳游戏”
*/
void jyanken1(){
	// version1
	int human;
	int comp;
	int judge;
	int retry;

	srand(time(NULL));
	printf("猜拳游戏开始！\n");
	do {
		comp = rand() % 3;
		do{
			printf("请决定要出的手势：(0)石头,(1)剪刀,(2)步\n");
			scanf("%d", &human);
		}while (human>2 || human<0);
		printf("我出");
		switch (comp){
			case 0: 
				printf("石头\n");
				break;
			case 1:
				printf("剪刀\n");
				break;
			case 2:
				printf("布\n");
				break;
		}
		judge = (human - comp + 3) % 3;
		switch (judge){
			case 0: 
				printf("平局\n");
				break;
			case 1:
				printf("你输了\n");
				break;
			case 2:
				printf("你赢了\n");
				break;
		}

		printf("是否再来一次？(0)否, (1)是\n");
		scanf("%d", &retry);
	}while (retry == 1);
}

// 显示所有的字符
void code(){
	int i;

	for (int i = 0; i < CHAR_MAX; i++)  // CHAR_MAX定义在<limits.h>中，表示char最大能表示的数
	{
		switch(i){
			case '\a':
				printf("\\a");
				break;
			case '\b':
				printf("\\b");
				break;
			case '\f':
				printf("\\f");
				break;
			case '\n':
				printf("\\n");
				break;
			case '\\r':
				printf("\\r");
				break;
			case 't':
				printf("\\t");
				break;
			case 'v':
				printf("\\v");
				break;
			default:
				printf(" %c", isprint(i) ? i:' ' );  // isprint 在<ctype.h>中定义，判断编码i的字符能否显示，若不能，则返回0
			}
			printf("%02x\n", i);
		
	}
}

void strdump(const char *s){
	/* 字符串内部，使用十六进制和二进制去显示 */
	while (*s){
		int i;
		unsigned char x = (unsigned char)*s;  // 强制类型转换

		printf("%c  ", isprint(x) ? x: ' ');  // character
		printf("%0*x  ", (CHAR_BIT + 3)/4, x);  // hex
		/*
			CHAR_BIT定义在<limits.h>中，表示一个字节的位数。
		*/
		for (i=CHAR_BIT-1; i>=0; i--){
			putchar(((x >> i) & 1u) ? '1': '0');
			/*
			如果x为1011 1011
			易知1u为0000 0001
			x & 1u 为 0000 0001
			所以知道x的第8个字节为1
			*/
		}
		putchar('\n');
		s++;
	}
}

// 使用指向指针的数组来实现改写猜拳游戏
void jyanken3(){
	// version3
	int i;
	int human;
	int comp;
	int judge;
	int retry;
	char *hd[] = {"石头", "剪刀", "布"};

	srand(time(NULL));
	printf("猜拳游戏开始！\n");
	do {
		comp = rand() % 3;
		do{
			printf("\a石头剪刀布...");
			for (i=0; i<3; i++){
				printf("  (%d)%s", i, hd[i]);
			}
			printf(":");
			scanf("%d", &human);
		}while (human>2 || human<0);
		printf("我出");
		switch (comp){
			case 0: 
				printf("石头\n");
				break;
			case 1:
				printf("剪刀\n");
				break;
			case 2:
				printf("布\n");
				break;
		}
		judge = (human - comp + 3) % 3;
		switch (judge){
			case 0: 
				printf("平局\n");
				break;
			case 1:
				printf("你输了\n");
				break;
			case 2:
				printf("你赢了\n");
				break;
		}

		printf("是否再来一次？(0)否, (1)是\n");
		scanf("%d", &retry);
	}while (retry == 1);
}


int main(){
	jyanken3();
	return 0;
}