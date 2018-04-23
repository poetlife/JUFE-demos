# include<stdio.h>
# include<time.h>
# include<stdlib.h>
# include<string.h>

// 常用的转义字符

// alert 这里会出现提示音
// \a
void alert(){
	printf("this is a warning!\a\n");
}


// new line \n
// 换行符
void new_line(){
	printf("first line\nsecond line\n");
}

// \f  form feed 换页符，一般输出没用 


// \b backspace 退格符 clock()
/*
clock() 用来求程序开始运行后经过的时间，如果无法获取处理器调用该进程的时间，或无法显示数值，则返回 clock_t -1
此外，由于我们需要把clock()函数返回的值转变为以秒为计量的单位，因此，我们需要用本函数的返回值除以CLOCKS_PER_SEC的值
*/

/*
等待x毫秒
*/
int sleep(unsigned long x){
	clock_t c1 = clock(), c2;
	do {
		if ((c2 = clock()) == (clock_t)-1)  // 错误
			return 0;
	} while (1000.0 * (c2 - c1)/ CLOCKS_PER_SEC < x);
	return 1;
}

void backspace(){
	int i;
	printf("ABCDEFG");

	for (i = 0; i < 7; i++){
		sleep(1000);
		printf("\b \b");
		fflush(stdout);  // 清空缓冲区
		/*
		当程序下达输出命令的时候，若把字符写入画面和文件，输出速度都不会很快，因此大多数编程环境都会要把输出的字符暂时放到“缓冲区”里，在接到输出换行字符的提示或缓存区已经满了等条件下才实际输出这些字符。
		*/
	}
}


// carriage return \r 回车符 回到行首
void carriage_return(){
	printf("我本来是打算说您好的，但是我想先说你好，然后再把你好消除，输出他的名字！\n");
	printf("您好！");
	sleep(1000);
	printf("\r彭纪西");
}

// \v 垂直制表符  \t 制表符
// purchar()  输出字符

// time operation
void countdown(){
	int i;
	clock_t c;

	for (i=10; i>0; i--){
		printf("\r%2d", i);
		fflush(stdout);
		sleep(1000);
	}
	printf("\r\aFIRE!!\n");
	c = clock();
	printf("程序一共运行了%.1f秒\n", (double)c/ CLOCKS_PER_SEC);  // 这里强制类型转化是因为 整数//整数会舍去小数部分
}


// typedef声明
/*
typedef声明用于声明一个新的类型名来代替原有的类型名
*/

// 心算训练
void mental(){
	int a, b, c;
	int x;
	clock_t start, end;
	double req_time;  // 所需时间

	srand(time(NULL));

	a = 100 + rand() % 900;
	b = 100 + rand() % 900;
	c = 100 + rand() % 900;

	printf("%d + %d + %d 等与多少？\n", a, b, c);

	start = clock();  // start to calculate

	while(1){
		scanf("%d", &x);
		if (x == a+b+c){
			break;
		}
		else{
			printf("\a the answer is wrong\n please reenter the answer:");
		}
	}

	end = clock();  // end

	req_time = (double)(end - start) / CLOCKS_PER_SEC;

	printf("计算时间长度为%.2f秒\n", req_time);
}

// strlen() 用来获取字符串的长度
void pengjixi(){
	int i;
	char name[] = "pengjixi";
	int name_len = strlen(name);

	while (1){
		for (i=0; i<name_len; i++){
			putchar(name[i]);
			fflush(stdout);
			sleep(500);
		}

		for (i=0; i<name_len; i++){
			printf("\b \b");
			fflush(stdout);
			sleep(500);
		}
	}
}

// printf  格式输入输出
void asterisk_printf(){
	int i, x;

	printf("要显示多少行：");
	scanf("%d", &x);

	for(i = 1; i<=x; i++){
		printf("%*d\n", i, i%10);
	}
}

int main(){

	alert();
	new_line();
	backspace();  // this opreation can take you previous 7 secs
	carriage_return();
	countdown();  // ten seconds
	mental();
	pengjixi();
	asterisk_printf();
	return 0;
}