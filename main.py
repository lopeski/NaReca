import os
from os.path import abspath, isfile, join
import asyncio

soArquivos = [f for f in os.listdir('.') if isfile(join('.', f))]

def filtro(itens):
    fil = ['index.py']

    if(itens in fil):
        return True
    else:
        return False

filtered = filter(filtro, soArquivos)

for item in filtered:
    exec(open(item).read())
