# pdf2docx

```
# 文档转码工具包
pip install pdf2docx
# python脚本转exe执行文件,如果只运行代码不打包exe程序可不安装这个包
pip install cx_freeze
```


# 将程序打包成exe可执行文件
```
# 强烈建议使用conda新建一个虚拟环境，里面仅安装pdf2docx和cx_freeze包，这样打包出来的程序大概180M
# 这180M主要是因为pdf2docx引用了opencv大概占用100M，numpy占用40M
cxfreeze main.py -O -c --base-name=Win32GUI --icon pdf.ico --target-dir out --target-name=pdf2docx --include-files pdf.png --exclude-modules=asyncio,concurrent,ctypes,curses,distutils,fire,importlib_metadata,lib2to3,msilib,PIL,pkg_resources,pydoc_data,pytz,setuptools,test,xml,xmlrpc,email,html,http,numpy_mkl,unittest
```
