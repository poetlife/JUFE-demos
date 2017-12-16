# JUFE-demos
关于江西财经大学网站的一些demos

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

1. `pip install requirements.txt` 安装必要的包
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
