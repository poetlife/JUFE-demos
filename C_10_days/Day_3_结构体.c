#include<stdio.h>

/*
struct [structure tag]
{
   member definition;
   member definition;
   ...
   member definition;
} [one or more structure variables];
*/

// struct 结构体
struct Books{
	char title[50];
	char author[50];
	char subject[100];
	int book_id;
};

int struct_function(){
	struct Books Book1;
	struct Books Book2;  /* 声明 Book2，类型为Books */

	// Book1详述
	strcpy(Book1.title, "C Programming");
	strcpy(Book1.author, "Nuha Ali");
	strcpy(Book1.subject, "C Programming Tutorial");
	Book1.book_id = 6495407;

	// Book2详述
	strcpy(Book2.title, "Data Structure");
	strcpy(Book2.author, "Yan Weimin");
	strcpy(Book2.subject, "A Tutorial to University CS");
	Book2.book_id = 147510;

	// 输出Book1 信息
	printf("Book 1 title: %s\n", Book1.title);
	printf("Book 1 author: %s\n", Book1.author);
	printf("Book 1 subject: %s\n", Book1.subject);
	printf("Book 1 book_id: %d\n", Book1.book_id);

 	printBook(Book2);
	
}


// 结构作为函数参数
void printBook(struct Books Book){
	printf("Book title: %s\n", Book.title);
	printf("Book author: %s\n", Book.author);
	printf("Book subject: %s\n", Book.subject);
	printf("Book book_id: %d\n", Book.book_id);
}

// 指向结构的指针
void pointer_to_struct(){
	struct Books Book1;
	// Book1详述
	strcpy(Book1.title, "C Programming");
	strcpy(Book1.author, "Nuha Ali");
	strcpy(Book1.subject, "C Programming Tutorial");
	Book1.book_id = 6495407;

	struct Books *struct_pointer;
	struct_pointer = &Book1;

	// 使用指向该结构的指针访问结构的成员，使用->运算符
	printf("the title is: %s\n", struct_pointer->title);
}


// 位域
/*
有些信息在存储时，并不需要占用一个完整的字节，而只需占几个或一个二进制位。例如在存放一个开关量时，只有 0 和 1 两种状态，用 1 位二进位即可。为了节省存储空间，并使处理简便，C 语言又提供了一种数据结构，称为"位域"或"位段"。
所谓"位域"是把一个字节中的二进位划分为几个不同的区域，并说明每个区域的位数。每个域有一个域名，允许在程序中按域名进行操作。这样就可以把几个不同的对象用一个字节的二进制位域来表示。
*/
void domain(){
	struct bs
	{
		unsigned a:1;
		unsigned b:3;
		unsigned c:4;
	} bit, *pbit;

	bit.a = 1;
	bit.b = 7;
	bit.c = 15;  /* 赋值的时候不能超过可以表示的范围 */
	printf("%d,%d,%d\n", bit.a, bit.b, bit.c);
	pbit = &bit;
	pbit -> a = 0;
	pbit->b &= 3;  //  按位与
	pbit->c |= 1;  // 按位或
	printf("%d,%d,%d\n", pbit->a, pbit->b, pbit->c);

}

int main(){

	domain();
    return 0;
}
