# -*- coding:utf-8 -*-


import os
import time
from htmloutput.htmloutput import HtmlOutput
from nose import run

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    outfile = os.path.join(path, 'demo.py')
    run(argv=['nosetests', '-v', '--with-html-output', '--html-out-file=result' + now + '.html', outfile],
        plugins=[HtmlOutput()])

