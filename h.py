import os
import sys
import random
import platform
import explists


def console():
    logo=[explists.logo(),explists.logo2(),explists.logo3(),explists.logo4(),explists.logo5(),explists.logo6(),explists.logo7()]
    print(random.choice(logo))
    explists.helps()
    zd={'set cve':set_cve,'show cve':explists.jihe,'show shentou':explists.shentou,'show tiquan':explists.tiquan,'help':explists.help,'show log':explists.update_log}
    if get_os() == 'Linux':
        h=Linux_hj()
        while True:
            sys.stdout.write('Manage>>>>')
            sys.stdout.flush()
            xuan = sys.stdin.readline().strip()
            if xuan in zd:
                print(xuan)
                zd[xuan]()
            elif xuan == 'exit':
                print(xuan)
                break
            else:
                os.system(h+' && '+xuan)

    elif get_os() == 'Windows':
        h=Windows_hj()
        os.putenv('Path',h)
        while True:
            sys.stdout.write('Manage>>>>')
            sys.stdout.flush()
            xuan = sys.stdin.readline().strip()
            if xuan in zd:
                print(xuan)
                zd[xuan]()
            elif xuan == 'exit':
                print(xuan)
                break
            else:
                os.system(xuan)


def get_os():
    return platform.system()


def get_path():
    path = os.getcwd()
    return path

def Linux_hj():
    path=get_path()
    h = 'export PATH=' + path + '/env:$PATH'
    os.system('chmod +x env/*')
    return h


def Windows_hj():
    path=get_path()
    h=path+'\\env'
    hs = os.environ['PATH']
    huanjing=hs+';'+h
    return huanjing

def set_cve():
    try:
        os.chdir('exp/cve')
        while True:
            sys.stdout.write('Manage>>>>')
            sys.stdout.flush()
            rce = sys.stdin.readline().strip()
            if rce == 'fcd':
                os.chdir('../..')
                break
            elif rce == 'exit':
                sys.exit(0)
            elif 'use ' in rce:
                try:
                    os.chdir(rce[4:8] + '/CVE-' + rce[4:])
                    while True:
                        sys.stdout.write('CVE-' + rce[4:] + '>>>')
                        sys.stdout.flush()
                        x = sys.stdin.readline().strip()
                        if x == 'fcd':
                            os.chdir('..')
                            break
                        elif x == 'exit':
                            sys.exit(0)
                        else:
                            os.system(x)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
            elif rce == int:
                print('重新检查命令')
            elif 'cd ' in rce:
                try:
                    os.chdir(rce[3:])
                    while True:
                        sys.stdout.write('Manage>>>>')
                        sys.stdout.flush()
                        a = sys.stdin.readline().strip()
                        if a == 'fcd':
                            os.chdir('..')
                            break
                        elif a == 'exit':
                            sys.exit(0)
                        elif 'use ' in rce:
                            try:
                                os.chdir('CVE-' + rce[4:])
                                while True:
                                    sys.stdout.write('CVE-' + rce[4:] + '>>>>')
                                    sys.stdout.flush()
                                    a = sys.stdin.readline().strip()
                                    if a == 'fcd':
                                        os.chdir('..')
                                        break
                                    elif a == 'exit':
                                        sys.exit(0)
                                    else:
                                        os.system(a)
                            except:
                                print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
                        elif 'cd ' in a:
                            try:
                                os.chdir(a[3:])
                                while True:
                                    sys.stdout.write('Manage>>>>')
                                    sys.stdout.flush()
                                    a = sys.stdin.readline().strip()
                                    if a == 'fcd':
                                        os.chdir('..')
                                        break
                                    elif a == 'exit':
                                        sys.exit(0)
                                    elif 'use ' in rce:
                                        try:
                                            os.chdir('CVE-' + rce[4:])
                                            while True:
                                                sys.stdout.write('CVE-' + rce[4:] + '>>>>')
                                                sys.stdout.flush()
                                                a = sys.stdin.readline().strip()
                                                if a == 'fcd':
                                                    os.chdir('..')
                                                    break
                                                elif a == 'exit':
                                                    sys.exit(0)
                                                else:
                                                    os.system(a)
                                        except:
                                            print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
                                    elif 'cd ' in a:
                                        try:
                                            os.chdir(a[3:])
                                            while True:
                                                sys.stdout.write('Manage>>>>')
                                                sys.stdout.flush()
                                                a = sys.stdin.readline().strip()
                                                if a == 'fcd':
                                                    os.chdir('..')
                                                    break
                                                elif a == 'exit':
                                                    sys.exit(0)
                                                elif 'use ' in rce:
                                                    try:
                                                        os.chdir('CVE-' + rce[4:])
                                                        while True:
                                                            sys.stdout.write('CVE-' + rce[4:] + '>>>>')
                                                            sys.stdout.flush()
                                                            a = sys.stdin.readline().strip()
                                                            if a == 'fcd':
                                                                os.chdir('..')
                                                                break
                                                            elif a == 'exit':
                                                                sys.exit(0)
                                                            else:
                                                                os.system(a)
                                                    except:
                                                        print('?????????????当我打出？时，不是我有问题，是我觉得你有问题')
                                                elif 'cd ' in a:
                                                    try:
                                                        os.chdir(rce[3:])
                                                        while True:
                                                            sys.stdout.write('Manage>>>>')
                                                            sys.stdout.flush()
                                                            a = sys.stdin.readline().strip()
                                                            if a == 'fcd':
                                                                os.chdir('..')
                                                                break
                                                            elif a == 'exit':
                                                                sys.exit(0)
                                                            else:
                                                                os.system(a)
                                                    except:
                                                        print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
                                                else:
                                                    os.system(a)
                                        except:
                                            print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
                                    else:
                                        os.system(a)
                            except:
                                print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
                        else:
                            os.system(a)
                except:
                    print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
            else:
                os.system(rce)
    except:
        print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')

