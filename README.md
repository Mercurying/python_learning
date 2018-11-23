python 环境搭建：
Windows系统：
步骤：
1.下载官方源码包：
https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe

2.安装提示步骤安装(安装时勾选添加环境变量)

3.检测是否安装成功 windows+R -->cmd窗口
python --显示具体信息
python -v 显示版本信息
pip --python包管理工具

4.安装编辑器
使用sublime text3
安装package controls
配置python编译运行命令：
tools-->Build system-->New build system
添加Python3.sublime-build配置文件

{
    "cmd": ["E:/program files/python/python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.pythona",
    "encoding": "cp936"
}
encoding:指定的值是当前Windows系统cmd 编码方式：简体中文 cp936
5.sublime text3 python 环境常用插件：
packageResourceViewer --修改代码注释颜色
 ctrl+shift+p-->PackageResourceViewer-->Open Resource-->Color Scheme -Default-->Monokai.tmTheme-->搜索comment-->修改成十六进制颜色色值 #0AA344(绿色)
Anaconda--python代码提示;
sublimeCodeIntel--sublime text环境代码提示
SideBarEnhancements--增强侧边菜单


