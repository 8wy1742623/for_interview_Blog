"""
自动运行app.py，一旦 *.py 文件修改，自动重启app.py

监视器使用
# 在powershell中输入下面命令：
./pymonitor app.py

"""

import os
import sys
import time
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log_print(s):
    print('[Monitor] %s' % s)


class MyFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, fn):
        super(MyFileSystemEventHandler, self).__init__()
        self.restart = fn

    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            log_print('Python source file changed: %s' % event.src_path)
            self.restart()


command = ['echo', 'ok']
process = None


def kill_process():
    global process
    if process:
        log_print('Kill process [%s]...' % process.pid)
        process.kill()
        process.wait()
        log_print('Process ended with code %s.' % process.returncode)
        process = None


def start_process():
    global process, command
    log_print('Start process %s...' % ' '.join(command))
    process = subprocess.Popen(
        command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)


def restart_process():
    kill_process()
    start_process()


def start_watch(path, callback):
    observer = Observer()
    observer.schedule(
        MyFileSystemEventHandler(restart_process), path, recursive=True)
    observer.start()
    log_print('Watching directory %s...' % path)
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print('Usage: ./pymonitor your-script.py')
        exit(0)
    if argv[0] != 'ipython':
        argv.insert(0, 'ipython')
    command = argv
    path = os.path.abspath('.')
    start_watch(path, None)
