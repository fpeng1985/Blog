Title: 如何编译QCADesigner
Date: 2016-12-02 23:42
Modified: 2016-12-16 11:12
Category: Programming
Tags: c, qca
Slug: how-to-compile-QCADesigner
Authors: 彭斐
Summary: QCADesigner在Windows环境下的编译过程

编译环境为Windows10 64位，msys2

1. 设置环境变量GTK_SOURES到/c/msys2/usr
2. 运行`./autogen.sh`
3. 替换 config.sub 和 config.guess 到最新版本
	- `wget -O /tmp/config.sub "git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD"`
	- `wget -O /tmp/config.guess "git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD"`
 
1. 运行 `./configure`
2. 修改po目录下的Makefile，将**MSGFMT_OPTS**设置为空
3. 运行`make -j4`