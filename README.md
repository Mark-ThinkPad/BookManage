# 图书管理系统

## 项目简介

- <数据库原理及应用> 课程设计

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

## 实现方案

- UI设计及实现: Web网页
- Web前端:
    - `Materialize` v1.0.0
    - `jQuery` v3.4.1
    - `js-cookie` v2.2.1
- 后端:
    - `Python Flask` v1.1.1
    - `Microsoft SQL Server` (版本见测试平台)
- ORM方案: `SQLAlchemy` v1.3.11 (先设计数据库再使用 `sqlacodegen` 工具生成 `models.py` )
    
## 项目运行

- 安装需要的Python第三方库
```bash
pip install -r requirements.txt
```

- 初始化数据库
```
执行 /db/ 文件夹中的 init-db.sql 完成数据库及表的创建, 如果需要初始用户数据, 可以执行 test_data.sql
```

- 运行开发服务器
```bash
python manage.py run
```

## 友情提示

- 经实际动手实践, 在 `Linux` + `Python 3.8` 的环境中安装 `pymssql` 时, 如果无法通过官方文档介绍的方法进行安装, 可以将 `pymssql-2.1.4` 的源码包下载并修改其中的两行代码进行手动安装([下载页面](https://github.com/pymssql/pymssql/releases/tag/2.1.4), 如下:

> 请先提前安装 FreeTDS 和 Cython (Arch Linux用户请使用pacman安装, 即sudo pacman -S Cython)

`setup.py` 中的第160行修改为:
```python
# `Linux X86-64` 可以替换成你喜欢的其他字符串
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
