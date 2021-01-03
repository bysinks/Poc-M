import os
import sys
import random
import platform
import explists


def console():
    logo = [explists.logo(), explists.logo2(), explists.logo3(), explists.logo4(), explists.logo5(), explists.logo6(),
            explists.logo7()]
    print(random.choice(logo))
    print('\t\t\t\t\t\t一个exp货架罢了。。。')

    explists.helps()
    while True:
        sys.stdout.write('Manage>>>>')
        sys.stdout.flush()
        xuan = sys.stdin.readline().strip().split(' ')
        if xuan[0] in options.mode:
            if xuan[0] == 'help':
                explists.help()
            elif xuan[0] == 'exit' and xuan[0] == 'quit':
                break
            elif xuan[0] == 'search':
                search(xuan[1])
            elif xuan[0] == 'show' and xuan[1] in options.show_options:
                if xuan[1] == 'cve':
                    explists.jihe()
                elif xuan[1] == 'qingdan':
                    explists.qingdan()
                elif xuan[1] == 'log':
                    explists.update_log()
                else:
                    print("invalid syntax!")
            elif xuan[0] == 'use' and xuan[1] in options.use_options:
                if xuan[1] == '-h' or xuan[1] == '--help':
                    argvs.helps()
                elif xuan[1] == '-v' or xuan[1] == '--cve':
                    argvs.cve(xuan[2])
                elif xuan[1] == '-c' or xuan[1] == '--cms':
                    argvs.cms(xuan[2])
                elif xuan[1] == '-p' or xuan[1] == '--plugin':
                    argvs.plugins(xuan[2])
                elif xuan[1] == '-w' or xuan[1] == '--windows':
                    argvs.w(xuan[2])
                elif xuan[1] == '-l' or xuan[1] == '--linux':
                    argvs.l(xuan[2])
                else:
                    print("invalid syntax!")
        else:
            try:
                if get_os() == 'Linux':
                    os.system(Linux_hj() + "&&" + xuan[0])

                elif get_os() == 'Windows':
                    os.putenv('Path', Windows_hj())
                    os.system(xuan[0])

                elif get_os() == 'Darwin':
                    os.system(Darwin_hj() + "&&" + xuan[0])
                else:
                    print("invalid syntax!")
            except:
                print("invalid syntax!")

def get_os():
    return platform.system()


def get_path():
    path = os.getcwd()
    return path


def Linux_hj():
    path = get_path()
    h = 'export PATH=' + path + '/env:$PATH'
    os.system('chmod +x env/*')
    return h


def Darwin_hj():
    path = get_path()
    h = 'export PATH=$PATH:' + path
    return h


def Windows_hj():
    path = get_path()
    h = path + '\\env'
    hs = os.environ['PATH']
    huanjing = hs + ';' + h
    return huanjing


def search(ml):
    v = ml[0:]
    for i, j, n in os.walk('exp'):
        p = str(i).replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace("'", '').replace(',',
                                                                                                                ' ')
        a = p.rfind(v)
        if v in p:
            print(p[:a] + p[a:])



class argvs(object):
    def cve(ml):
        try:
            os.chdir('exp/cve/' + ml[0:4] + '/CVE-' + ml[0:])
            while True:
                try:
                    sys.stdout.write('CVE-' + ml[0:] + '_Manage>>>>')
                    sys.stdout.flush()
                    rce = sys.stdin.readline().strip()
                    if rce == 'fcd':
                        os.chdir('../../../../')
                        break
                    elif rce == 'exit':
                        sys.exit(0)
                    elif rce == 'help':
                        if platform.system() == 'Linux':
                            os.system('cat help.txt')
                        elif platform.system() == 'Windows':
                            os.system('type help.txt')
                    else:
                        os.system(rce)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
        except:
            pass

    def cms(cms):
        try:
            os.chdir('exp/cms/' + cms + '_cms')
            while True:
                try:
                    sys.stdout.write(cms + '_Manage>>>>')
                    sys.stdout.flush()
                    rce = sys.stdin.readline().strip()
                    if rce == 'fcd':
                        os.chdir('../../../')
                        break
                    elif rce == 'exit':
                        sys.exit()
                    elif rce == 'help':
                        if platform.system() == 'Linux':
                            os.system('cat help.txt')
                        elif platform.system() == 'Windows':
                            os.system('type help.txt')
                    else:
                        os.system(rce)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
        except:
            pass

    def plugins(plugin):
        try:
            os.chdir('exp/plugins/' + plugin)
            while True:
                try:
                    sys.stdout.write(plugin + '_Manage>>>>')
                    sys.stdout.flush()
                    rce = sys.stdin.readline().strip()
                    if rce == 'fcd':
                        os.chdir('../../../')
                        break
                    elif rce == 'exit':
                        sys.exit()
                    elif rce == 'help':
                        if platform.system() == 'Linux':
                            os.system('cat help.txt')
                        elif platform.system() == 'Windows':
                            os.system('type help.txt')
                    else:
                        os.system(rce)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
        except:
            pass

    def w(ve):
        try:
            os.chdir('exp/OS/windows/' + ve)
            while True:
                try:
                    sys.stdout.write(ve + '_Manage>>>>')
                    sys.stdout.flush()
                    rce = sys.stdin.readline().strip()
                    if rce == 'fcd':
                        os.chdir('../../../../')
                        break
                    elif rce == 'exit':
                        sys.exit()
                    elif rce == 'help':
                        if platform.system() == 'Linux':
                            os.system('cat help.txt')
                        elif platform.system() == 'Windows':
                            os.system('type help.txt')
                    else:
                        os.system(rce)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
        except:
            pass

    def l(version):
        try:
            os.chdir('exp/OS/linux/' + version)
            while True:
                try:
                    sys.stdout.write(version + '_Manage>>>>')
                    sys.stdout.flush()
                    rce = sys.stdin.readline().strip()
                    if rce == 'fcd':
                        os.chdir('../../../../')
                        break
                    elif rce == 'exit':
                        sys.exit()
                    elif rce == 'help':
                        if platform.system() == 'Linux':
                            os.system('cat help.txt')
                        elif platform.system() == 'Windows':
                            os.system('type help.txt')
                    else:
                        os.system(rce)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
        except:
            pass

    def helps():
        help = '''
    use <module>
    -h/--help             
    -v/--cve                      进入指定cve路径
    -c/--cms                      进入指定cms路径
    -p/--plugin                   进入指定组件路径
    -w/--windows -l/--linux       进入指定系统路径              
        '''
        print(help)


class options:
    mode = (
        'help',
        'use',
        'show',
        'exit',
        'quit',
        'search',
    )

    use_options = (
        '-v',
        '--cve',
        '-c',
        '--cms',
        '-p',
        '--plugin',
        '-w',
        '-l',
        '--linux',
        '-h',
        '--help',
    )

    show_options = (
        'cve',
        'qingdan',
        'log',
    )
