#-*- coding:utf-8 -*-

name = "Jinja2"

version = "3.1.4"

authors = ["Armin Ronacher"]

description = "A modern and designer-friendly templating language for Python."

variants = [['platform-linux', 'arch-x86_64']]

requires = ["python-3.6+"]

# build_command가 {root}/rezbuild.py를 정확히 호출하는지 확인
build_command = 'python3.7 {root}/rezbuild.py {install}'

def commands():
    # 설치된 Jinja2 경로를 PYTHONPATH에 추가
    env.PYTHONPATH.append("{root}")