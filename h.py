import explists
import pocset
import os
import random
import sys


def console():
    logo=[explists.logo(),explists.logo2(),explists.logo3(),explists.logo4(),explists.logo5(),explists.logo6(),explists.logo7()]
    print(random.choice(logo))
    explists.helps()
    zd={'set shentou':set_shentou,'set tiquan':set_tiquan,'show cve':pocset.jihe,'show shentou':pocset.shentou,'show tiquan':pocset.tiquan,'help':explists.help,'show log':explists.update_log}
    while True:
        xuan = input('Manage>>>>')
        if 'use' + sys.argv[0]:
            print('exp/cve/' + xuan[4:8] + '/CVE-' + xuan[4:])
            use(xuan)
        elif xuan == 'exit':
            break
        elif xuan in zd:
            zd[xuan]()

        else:
            print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')


def set_shentou():
    try:
        os.chdir('exp/shentou')
        while True:
            rce = input('Manage>>>>')
            if rce == 'fcd':
                os.chdir('../..')
                break
            elif rce=='exit':
                sys.exit(0)
            elif 'use ' in rce:
                try:
                    os.chdir(rce[4:8] + '/CVE-' + rce[4:])
                    while True:
                        x = input('CVE-' + rce[4:] + '>>>')
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
                        a = input('Manage>>>>')
                        if a == 'fcd':
                            os.chdir('..')
                            break
                        elif a == 'exit':
                            sys.exit(0)
                        elif 'use ' in rce:
                            try:
                                os.chdir('CVE-' + rce[4:])
                                while True:
                                    a = input('CVE-' + rce[4:] + '>>>>')
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
                                    a = input('Manage>>>>')
                                    if a == 'fcd':
                                        os.chdir('..')
                                        break
                                    elif a == 'exit':
                                        sys.exit(0)
                                    elif 'use ' in rce:
                                        try:
                                            os.chdir('CVE-' + rce[4:])
                                            while True:
                                                a = input('CVE-' + rce[4:] + '>>>>')
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
                                                a = input('Manage>>>>')
                                                if a == 'fcd':
                                                    os.chdir('..')
                                                    break
                                                elif a == 'exit':
                                                    sys.exit(0)
                                                elif 'use ' in rce:
                                                    try:
                                                        os.chdir('CVE-' + rce[4:])
                                                        while True:
                                                            a = input('CVE-' + rce[4:] + '>>>>')
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
                                                            a = input('Manage>>>>')
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


def set_tiquan():
    try:
        os.chdir('exp/tiquan')
        while True:
            rce = input('Manage>>>>')
            if rce == 'fcd':
                os.chdir('../..')
                break
            elif rce == 'exit':
                sys.exit(0)
            elif 'use ' in rce:
                try:
                    os.chdir(rce[4:8] + '/CVE-' + rce[4:])
                    while True:
                        x = input('CVE-' + rce[4:] + '>>>')
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
                        a = input('Manage>>>>')
                        if a == 'fcd':
                            os.chdir('..')
                            break
                        elif a == 'exit':
                            sys.exit(0)
                        elif 'use ' in rce:
                            try:
                                os.chdir('CVE-' + rce[4:])
                                while True:
                                    a = input('CVE-' + rce[4:] + '>>>>')
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
                                    a = input('Manage>>>>')
                                    if a == 'fcd':
                                        os.chdir('..')
                                        break
                                    elif a == 'exit':
                                        sys.exit(0)
                                    elif 'use ' in rce:
                                        try:
                                            os.chdir('CVE-' + rce[4:])
                                            while True:
                                                a = input('CVE-' + rce[4:] + '>>>>')
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
                                                a = input('Manage>>>>')
                                                if a == 'fcd':
                                                    os.chdir('..')
                                                    break
                                                elif a == 'exit':
                                                    sys.exit(0)
                                                elif 'use ' in rce:
                                                    try:
                                                        os.chdir('CVE-' + rce[4:])
                                                        while True:
                                                            a = input('CVE-' + rce[4:] + '>>>>')
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
                                                            a = input('Manage>>>>')
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

def use(xuan):
    try:
        os.chdir('exp/cve/' + xuan[4:8] + '/CVE-' + xuan[4:])
        while True:
            try:
                rce = input('CVE-' + xuan[4:] + '_Manage>>>>')
                if rce == 'fcd':
                    os.chdir('../../../../')
                    break
                elif rce == 'exit':
                    sys.exit(0)
                else:
                    os.system(rce)
            except:
                print('??????????????当我打出？时，不是我有问题，是我觉得你有问题')
    except:
        pass

def search(xuan):
    v = xuan
    for i, j, n in os.walk('./exp'):
        p = str(i).replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace("'", '').replace(',',
                                                                                                                ' ')
        a = p.rfind(v)
        if v in p:
            print(p[:a] + p[a:])