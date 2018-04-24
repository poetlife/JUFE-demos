#include<stdio.h>
#include<string.h>

// 字符串操作
void basic(){
	char s2[7];

	char s1[7] = {'P', 'J', 'X', 'X', 'X', 'X', '\0'};

	// 复制s1到s2里面去strcpy(to, from)
	strcpy(s2, s1);
	printf("%s\n%s\n", s1, s2);

	// 连接两个字符串
	strcat(s1, s2);
	printf("concat s2 to s1:%s\n", s1);

	// 连接后判断字符串长度
	printf("the length of new string is:%d\n", strlen(s1));

	// 比较两个字符串是否相等
	// 如果 s1 和 s2 是相同的，则返回 0；如果 s1<s2 则返回小于 0；如果 s1>s2 则返回大于 0。
	printf("compare s1 and s2: %d\n", strcmp(s1, s2));  // 1: means s1>s2

	// 返回一个指针，指向字符串s1中字符ch第一次出现的位置；
	char *pt = strchr(s1, 'X');
	printf("查找X返回的指针为%p, 而其值为%c\n", pt, *pt);

	// 返回一个指针，指向字符串 s1 中字符串 s2 的第一次出现的位置。
	char *ptr = strstr(s1, s2);
	printf("查找字符串s2返回的指针为%p，value is:%c\n", ptr, *ptr);

	// strlwr: string lowercase

	// strupr: string uppercase
}


int main(){

	basic();
    return 0;
}
