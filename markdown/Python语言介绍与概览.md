# Python语言介绍与概览
## Python语言运行环境
### 操作系统
- Windows
- Linux
- MacOS

### 获取安装包
- Python官方下载页   http://www.python.org/download/
- 不同操作系统下的安装包格式
    - Linux/Unix: Source/release
    - Mac OS X: Mac OS X 64-bit/32-bit
    - Windows: zip/executable/web-based

### 安装Python
- Windows 安装向导-默认的安装模式
- Linux 下载Python源代码压缩文件
- MacOS 与Windows环境类似

### 编程环境
#### IDLE
Python软件包自带的一个集成开发环境（Integrated Development Environment）的可视化界面（GUI）。

#### 集成开发环境 - PyCharm
由JetBrains公司打造的一款IDE，带有一整套可以帮助用户提高效率的工具。

#### 科学计算中的Python - Anaconda
一个针对科学计算设计的多合一安装包：包括Python本体、标准库以及许多使用的第三方库，同时带有conda作为包管理器。

#### 丰富的模块库
- http://docs.python.org/3/library
- http://github.com

#### 其他集成开发环境
Eclipse/Arachno Python/Pythonwin

#### 文本编辑器
Vim/GUN Emacs/Atom/Sublime Text/Notepad++/VS Code

---

## Python程序设计风格
### 优雅、明确、简单
#### 代码强制缩进
- 程序是写给人读的
    - Programs are meant to be read by humans and only incidentally for computers to execute. - Donald Ervin Knuth 
- Python的强制缩进规范完成了关键部分
- 还需要良好的编程规范
    - 变量、函数、类命名
    - 注释和文档
    - 一些编程设计上的良好风格

#### Donald的精彩人生
- 鸿篇巨著《计算机程序设计艺术》
- 为了巨著印刷漂亮，开发了伟大的排版软件TEX
- 字符串款速匹配KMP算法
- 1974年获得图灵奖

#### Python哲学
```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---

## 数据对象与组织
### 什么是数据
数据（data）是信息的表现形式和载体。

对现实世界实体和概念的抽象。

#### 大数据（big data）
Volume、Velocity、Variety、Value、Veracity
- 规模大
- 增长速度快
- 来源广泛
- 价值密度低，待挖掘
- 准确性不定

**Python语言是最热门的大数据分析处理语言**

### 多种多样的数据类型
- 描述事物大小、次序的数值类型
- 描述事物各方面特性的文本字符串类型
- 描述事物时间属性的日期时间类型
- 复杂数据类型（图像、音频、视频等）

### 数据类型归纳
#### 简单类型用来表示值
- 整数int
- 浮点数float
- 复数complex
- 逻辑值bool
- 字符串str

#### 容器类型用来组织这些值
- 列表list
- 元祖tuple
- 集合set
- 字典dict

#### 数据类型之间几乎都可以转换

### 对数据进行组织
对大量数据进行组织的时候，需要建立各种各样的数据组织，以便提高计算效率。

#### 组织方式
- 没有组织
- 标签式组织数据
- 队列、栈、树、图等

---
## 计算和控制流
### 计算与流程
- 对现实世界处理和过程的抽象
- 各种类型的数据对象，可以通过各种运算组织成复杂的表达式

### 运算语句
- 将表达式赋值给变量进行引用
- 赋值语句用来实现处理与暂存
    - 表达式计算
    - 函数调用
    - 赋值

### 控制流语句
控制流语句用来组织语句描述过程
- 顺序结构
- 条件分支
- 循环结构

### 定义语句
定义语句也用来组织语句，把一系列运算语句集合起来给一个名字

描述了一个包含一系列处理过程的计算单元，主要为了源代码的各种复用

- 可以定义函数、类等“代码”对象（def、class）
- 调用函数或者类，也可以得到数据对象，Python里所有可调用的事物称为callable

