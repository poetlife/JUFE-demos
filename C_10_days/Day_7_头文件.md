# C语言头文件设计

## 参考资料

[C头文件——RUNOOB.com](http://www.runoob.com/cprogramming/c-header-files.html)

[明解C语言——中级篇 柴田望洋著](http://www.ituring.com.cn/book/1810)

## 概述

> 头文件是扩展名为 **.h** 的文件，包含了 C 函数声明和宏定义，被多个源文件中引用共享。有两种类型的头文件：程序员编写的头文件和编译器自带的头文件。 
>
> A simple practice in C 或 C++ 程序中，建议把所有的常量、宏、系统全局变量和函数原型写在头文件中，在需要的时候随时引用这些头文件。 

## 引用头文件

```c
#include <stdio.h>
```

这种是引用**系统**头文件，它在系统目录的标准列表中搜索。在编译源代码时，您可以通过 -I 选项把目录前置在该列表前。 

```c
#include "stdio.h"
```

这种是引用**用户**头文件，它在当前文件所在目录中搜索。在编译源代码时，您可以通过 -I 选项把目录前置在该列表前。

## 条件引用

有时需要从多个不同的头文件中选择一个引用到程序中。例如，需要指定在不同的操作系统上使用的配置参数。您可以通过一系列条件来实现这点，如下： 

```c
#if SYSTEM_1
  #include <system1.h>
#elif SYSTEM_2
  #include <system2.h>
#else
  #include <system3.h>
```

## 包含保护头文件的设计
由于某些情况，同一个头文件可能会被包含2、3次，这样子就会产生**重复定义函数**的编译错误。
```C
#ifndef __PENG
#define __PENG
#endif
```
## 替换调用的函数

```c
#define putchar __putchar

int main(){
    putchar('\n');  // in reality is: __putchar('\n');
}
```

## 可变参数

### 可变参数的使用例子

``` c
#include <stdio.h>
#include <stdarg.h>
// 用于访问可变参数的函数

/* 根据第一参数，求后面的参数和 */
double vsum(int sw, ...){
    double sum = 0.0;
    va_list ap;
    
    va_start(ap, sw);  // 开始访问可变部分的参数
    switch (sw){
        case (0): sum += va_arg(ap, int);
        sum += va_arg(ap, int);
        break;
        case (1): sum += va_arg(ap, int);
        sum += va_arg(ap, long);
        break;
    }
    va_end(ap);
    return sum;
}

int main()
{
    printf("10 + 2 = %.2f\n", vsum(0, 10, 2));
    printf("10 + 200000L = %.2f\n", vsum(0, 10, 200000L));

    return 0;
}
```

这段代码输出如下：

```
$gcc -o main *.c
$main
10 + 2 = 12.00
10 + 200000L = 200010.00
```

### 可变参数的声明

> `int printf(const char *format, ...);`       

上面是`printf`函数的声明，该函数的开头是一个`const char *format`类型的参数，第2参数及其以后的参数的类型和个数都是可变的。

“**,...**”是表示接受可变参数的省略符号（ellipsis）

### `va_start`宏：访问可变参数前的准备

`<stdarg.h>`中定义了`va_list`型，这是一个特殊的类型，用于访问调用函数时堆积的参数。

`va_start`格式如下：

```c
void va_start(va_list ap, 最终参数);
```

作为形式参数的最终参数是函数定义过程中位于可变形式参数列表中最右边的形式参数的标识符，也就是省略符号“**,...**”前的标识符。

### `va_arg`宏：取出可变参数

调用完了`va_start`，访问参数的准备就完成了。下面要做的是逐一取出可变部分的参数。因此使用`va_arg`宏。

其格式如下：

```c
type va_arg(va_list ap, type);
```

### `va_end`宏：结束对可变参数的访问

要结束对可变部分的参数的访问，需要调用`va_end`宏。

其定义如下：

```c
void va_end(va_list ap);
```

结束对可变参数列表的处理，使函数正常返回。

## `vprintf`函数/`vfprintf`函数：输出到流

将**可变参数展开整理后输出到流**的标准库函数有两个，分别是将结果输出到标准输出流（控制台画面）的`printf`函数和将结果输出到文件或机器等任意流的`fprintf`函数。

### `vprintf`定义&使用

```c
int vprintf(const char *format, va_list arg);
```

函数等价于用`arg`替换可变实际参数列表的`printf`函数。调用函数前，必须实现用`va_start`宏初始化`arg`。该函数不调用`va_end`(意思是，使用完成后，需要自己调用)。返回写入字符的数量，发生输出错误的时候则返回**负值**。

### `vfprintf`定义&使用

```c
int vfprintf(FILE *stream, const char *format, va_list arg);
```

函数等价于用`arg`替换可变实际参数列表的`fprintf`函数。调用函数前，必须实现用`va_start`宏初始化`arg`。该函数不调用`va_end`(意思是，使用完成后，需要自己调用)。返回写入字符的数量，发生输出错误的时候则返回**负值**。

### `vsprintf`定义&使用

输出到字符串。

```c
int vsprintf(char *s, const char *format, va_list arg);
```

函数等价于用`arg`替换可变实际参数列表的`sprintf`函数。调用函数前，必须实现用`va_start`宏初始化`arg`。该函数不调用`va_end`(意思是，使用完成后，需要自己调用)。返回写入字符的数量，发生输出错误的时候则返回**负值**。
