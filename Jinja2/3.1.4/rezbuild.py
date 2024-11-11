# rezbuild.py
import os
import subprocess
import sys

def build(source_path, install_path):
    print("*"*50)
    print(source_path)
    print(source_path)
    print("*"*50)
    print(install_path)
    print(install_path)
    print("*"*50)

    # package.py 내용 생성
    package_py_content = '''# -*- coding: utf-8 -*- 

name = "Jinja2"

version = "3.1.4"

authors = ["Armin Ronacher"]

description = "A modern and designer-friendly templating language for Python."

variants = [['platform-linux', 'arch-x86_64']]

requires = ["python-3.6+"]

def commands():
    # 설치된 Jinja2 경로를 PYTHONPATH에 추가
    env.PYTHONPATH.append("{root}")
'''
    path = install_path.split("platform-linux")[0]    
    package_py_path = os.path.join(path, "package.py")
    print("*"*50)
    print(package_py_path)
    print(package_py_path)
    print("*"*50)
    
    # Jinja2 설치
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Jinja2==3.1.4", "--target", install_path])

    with open(package_py_path, "w") as f:
        f.write(package_py_content)

if __name__ == "__main__":
    build(
        source_path=os.getenv("REZ_BUILD_SOURCE_PATH"),
        install_path=os.getenv("REZ_BUILD_INSTALL_PATH")
    )
