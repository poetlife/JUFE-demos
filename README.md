# JUFE-demos
关于江西财经大学信息门户网站的一些demos

## 江西财经大学自动评教系统
引用[xNathan](https://github.com/xNathan/TeachEvaluation)项目中的代码，并加以修改。
### 版本说明
**增加**的地方如下：
1. 增加了新版本门户网的登录加密方法
2. 增加了命令行参数的支持

**修改**的地方如下：
1. 将原来默认的分数范围调整至\[86, 95]
2. 将代码迁移至Python3
3. 重构了代码，使代码更易阅读

### 使用说明
> 老司机请优雅的上车---[如何下载github上的单个文件](https://www.cnblogs.com/zhaoqingqing/p/5534827.html)

1. `pip install -r < requirements.txt` 安装必要的包
2. `python AutoEvaluateTeach.py -u 220150**** -p pjd***` 输入相关的信息
3. 愉快的自动评教了，但是要记住自己登陆上去点击结束评教的按钮

### 操作示例
![1](https://github.com/poetlife/JUFE-demos/blob/master/pics/1.png)
![2](https://github.com/poetlife/JUFE-demos/blob/master/pics/2.png)
![3](https://github.com/poetlife/JUFE-demos/blob/master/pics/3.png)

### 免责声明
[原作者免责声明](https://github.com/xNathan/TeachEvaluation#免责声明)
1. 本次修改已经邮件和原作者[@xNathan](https://github.com/xNathan)取得了联系，同样希望大家在使用的时候本着客观公正的态度去给每个老师进行评价。
2. 系统给分是随机，所以希望大家认真对待给每个老师的评分。

## 江西财经大学学生课程容量信息爬虫
`自动获取课程容量信息/CourseInfo.py`

### 版本说明
**增加**的地方如下：
1. 增加了新版本门户网的登录加密方法
2. 增加了命令行参数的支持
3. 增加了列表获取课程信息函数
4. 使用了`pandas`库的支持

### 使用说明
这是第二个关于江西财经大学信息门户网站的小demo，然后本demo本着非Python爱好者用不了的态度，所以用了一些高级的原生的不带的package，目的是为了减少代码量，此外，本人也非CS专业，只是抱着学习的态度在做这些，因此，这个版本一旦写好，以后门户网更新了应该不会再进行相应的更新。
1. 需要的package：`pandas/rsa/beautifulsoup`
2. 依然采用了命令行输入的方式`Python /自动获取课程容量信息/CourseInfo.py -u <username> -p <password> -p1 <path1> -p2 <path2>`
3. `path1`是指存放课程代码的列表的txt文件，`path2`是指生成的xlsx文件的导出位置。
4. Example: `Python /自动获取课程容量信息/CourseInfo.py -u 220150**** -p ***** -p1 E:/1.txt -p2 E:/result.xlsx`

### 存放课程代码txt文件实例
1. Example中的`E:/1.txt`文件格式如下图所示。
![1.txt样式](https://github.com/poetlife/JUFE-demos/blob/master/pics/4.png)
每个代码之间用`\n`隔开。
2. 导出文件样式
![result.xlsx](https://github.com/poetlife/JUFE-demos/blob/master/pics/5.png)
3. 操作示例
![instance_for_maniplation](https://github.com/poetlife/JUFE-demos/blob/master/pics/6.png)

### 免责声明
1. 由于这个程序是用学生账号对学校服务器进行**爬虫操作**，因此如果过于爬取频率过大被学校查处，使用者自行解决。
2. 由于**爬虫**会使用较大服务器带宽，不建议使用者在学生集中选课时使用，为此造成信息门户系统访问速度变慢是作者非常不提倡的。
3. 希望使用者能**充分利用**爬取的文件，不要重复爬取一些无意义的数据。

