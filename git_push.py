"""
WHAT
py脚本，git提交的一系列操作。

HOW
subprocess.run()
"""

from subprocess import run
import time

"""
配置信息
"""
configs = {
    'ssh_url': "git@github.com:8wy1742623/for_interview_Blog/tree/Usable",
    'branch': 'Usable'
}


def git_operation():
    time_now = time.strftime("%Y-%m-%d~~%H:%M:%S", time.localtime())
    print("1. git add .")
    run("git add .", shell=True)

    print('2. git commit -m "%s".' % time_now)
    run("git commit -m '%s'" % time_now, shell=True)

    print("3. git remote %s." % configs['ssh_url'])
    run("git remote add origin %s" % configs['ssh_url'], shell=True)

    print("4. git push origin %s" % configs['branch'])
    run("git push origin %s" % configs['branch'], shell=True)


def main():
    git_operation()


if __name__ == '__main__':
    main()
