# 图书管理系统

## 开发平台

- 系统环境: `Arch Linux`
- Python版本: `3.8.0`
- 数据库:  `Microsoft SQL Server 2019 (RTM)` Developer Edition (64-bit) on Linux (通过AUR安装)



## 测试平台

- 测试平台一: 即开发平台
- 测试平台二: (Window)
    - 系统环境: `Windows 7 SP1 64-bit`
    - Python版本: `3.6.7`
    - 数据库: `Microsoft SQL Server 2014 (X64 SP3)`

## 友情提示

- 经实际动手实践, 在 `Linux` + `Python 3.8` 的环境中安装 `pymssql` 时, 如果无法通过官方文档介绍的方法进行安装, 可以将 `pymssql-2.1.4` 的源码包下载并修改其中的两行代码进行手动安装([下载页面](https://github.com/pymssql/pymssql/releases)), 如下:

> 请先提前安装 FreeTDS 和 Cython (Arch Linux用户请使用pacman安装, 即sudo pacman -S Cython)

`setup.py` 中的第160行修改为:
```python
## `Linux X86-64` 可以替换成你喜欢的其他字符串
print("setup.py: platform.linux_distribution() => %r" % ('Linux X86_64',))
```

`src/_mssql.pyx` 中的第48行修改为:
```python
from collections.abc import Iterable
```

在 `pymssql-2.1.4` 的主目录中打开终端执行:
```bash
sudo python setup.py install
```

## To-Do List

- 项目完成后生成 `requirements.txt`
