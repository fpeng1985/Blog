Title: designer-mod项目进展
Date: 2016-12-15 12:33
Modified: 2016-12-16 11:06
Category: Research
Tags: python, qca
Slug: qca-research-status
Authors: 彭斐
Summary: designer-mod 项目进展，问题及解决方案

## 程序流程 ##
1. 读取命令行参数，找到输入的structure文件，并初始化输出目录。
2. 根据structure中定义的电路结构，生成所有需要仿真的衍生structure。
3. 利用`Python`库`multiprocessing`的`map`机制，并行仿真每一个structure。单个structure的仿真流程如下：
	- 在`C`程序中调用QCADesigner的相关API，针对structure定义的QCA电路进行仿真，并将结果输出到.qca和.sim文件中。
	- 在`C++`程序中用`Boost.spirit`库解析生成的.sim文件，并将12800个采样点转换为真值表，存储在`vector<vector<int>>`数据结构中。
	- 在`Python`程序中，根据真值表计算逻辑表达式，并保存所有相关结果到`dict`数据结构中。
	- 等待所有并行任务处理完后，生成的结构保存在`dict`组成的列表中。创建`sqlite3`数据库，并将每一个`dict`数据结构作为一行插入到`SimResult`表中。
	- 在统计函数中访问`SimResult`表，并将所需的统计信息写入.statistics文件。

1. 利用majority_gate_1.txt这个benchmark，在`PROCESS_NUM`设为20的情况下，运行时间大概是10秒钟。


## 运行速度过慢的原因  ##

1. QCADesigner默认采用bistable仿真引擎，每次仿真有12800个采样点，也就是说每次都计算了12800次。但我们在三输入情况下，实际上只需要运算8次即可。
2. 仿真结果只能输入为文件保存在硬盘上，磁盘读写导致速度低下。
3. 为了解析Simulation结果，需要编写解析程序，如果采用内存数据结构则无需解析的过程。

## 解决方案 ##

1. 将QCADesigner仿真引擎的代码移植过来，使其纳入我们的计算框架。
2. 利用Bayesian Network模型，重新设计一个QCA仿真器。

## 其他优化 ##
1. 编译源代码时采用release模式
`cmake -DCMAKE_BUILD_TYPE=Release ..`
1. 程序原型完成后，将代码用`C/C++`重构。需要注意的是：
	- `Python`的并行只能采用进程，但`C++`更倾向于使用线程。
	- 目前没有找到现成的逻辑化简库库。