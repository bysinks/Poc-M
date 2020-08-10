import os
from termcolor import *

def helps():
    logo='''
    [+]Poc-M
    [+]1.0.1
    [+]基于python3.8
    [+]更多请参照help命令
    [+]show log查看更新日志
    
    '''
    print(colored(logo,'cyan'))


def help():
    logo = '''
********************************************************************************************************************************
    本脚本为管理复杂繁多的exp/poc而作,为平时工作提高效率，考虑到平时工具使用习惯，部分命令与其他工具并无不同，
                 风格我们尽量贴近msf，包含渗透和提权exp/poc 内置脚本默认皆为已公开nday。
                                风格我们尽量贴近msf，包含渗透和提权exp/poc 
                                  cve编号目录名的cve务必大写
                                 
                                 
                                 
    show cve                  查看poc列表 使用时为进入该poc目录
    show shentou              来查看渗透poc模块大致清单 
    show tiquan               查看提权模块大致清单
    show log                  查看更新日志
    exit                      退出
    set                       进入指定类别 set cve 进入poc目录                    
    fcd                       返回上级
    部分poc内有帮助手册，可用在该poc目录下输入help查看。后续可以添加其他命令 
    
    
                                                             渗透poc位于 exp/shentou/xxx/xxx   提权poc位于  exp/tiquan/xxx/xxx 
******************************************************************************************************************************** 
    use <module>
    
    实例：use 2020-1938    直达poc下               
********************************************************************************************************************************
    '''
    print(colored(logo,'cyan'))


def update_log():
    logos='''
********************************************************************************************************************************
                                              更新日志
2020.08.07       
                 1、修复了逻辑性错误和些许bug
                 2、show cve查看cve列表从手动添加改为自动化获取，若无心添加poc详细介绍可按照命名规则分类放入指定目录。 
                 3、加入更新日志 
2020.08.08       
                 1、删除自动获取cve列表产生的多余空格
                 2、use功能上新，可一发入魂，直接抵达poc目录
2020.08.09
                 1、use简化，目录结构重新分类，移除shentou/tiquan 全部cve编号的poc列入cve目录 
                 2、目录结构更改                
******************************************************************************************************************************** 
    '''
    print(colored(logos,'cyan'))


def logo():
    logo='''
                                                                                                                    
..                                                                                                      ..              
..                                                                                                     .^?l.            
..                                                                                                   .^lZp ^          . 
..                                                                                                ...;Opp, ^            
..                                                                                        ^.. . ,^,Lmdw~^..             
..                                                                                  .  ...:1O!.^nZpww0,.                
..                                                                                ....:,mqj;:xqwqdmL,:;     .           
..                                                                              ...^;dp- (dwbpmdw:^-wv.,                
..                                                                                _\;L0pqwpq0J: ;Jqw,. .                
..                                                                  .         .,:JZdqwZqwp!:^,:1pp?.. ..                
..                                                                   ...  ^;+dmZmwqqwz^;qmpiuZwq;>^^                    
..                                      .                            ..,CqqqqqmqO!^,Zmd>>wqkqr:mm. ^                    
..      ...                                                        .,Cmdppm\!^ :w^.,+pZppw;>ZqZ,,           .           
..      .~^.         ..                                     ...  ,.;ZqpO?::XC,mc_ZZpwwkldmwp1:...                       
..     . .>p;...                                                 .<Zpmw^imZidp<,l[JZmwqmzlQQ,^^                         
..      . .,Zqqi^ ..  .             .                         ..::wpwx>:qwIqbp^OqL(wwmQqd>..                            
..          .,mwwwZl:..            .,     ..                  . iqdw-:1wq\:qqlpbwmmZ>l{0{:.                             
..           ..;pbdqqwqqt!:;.. ^^,,mOI.^.,,:Ou^...           ..<qZp-.|wqd,0bC.LmpwqpOt, .                   .           
..          .  :x:.<mZpOqqppqqwpppqwmqkqb;mmqpz, ^           .{wqbI..^QZ;.:x[X_I,lxZ^  ..                               
..             ..]mp(;^. ,;{Ywqwmut1i;<ZdqOII!}O^.        ..,Owqq+^ ^,,nwdpdmqbwZd:^ .                     .            
..             ....l\mpqwmmpmp;lnOpY?z,.(pnc?~pZbw,^.     .^wqqw:..[mpwqllu{<m0,,^..                                    
..                . . . ,^.,1mpdqL;^}pwU:q\1lZbdiZmw;.^ ^^_0ZZ0:.,Xqqq<_LOppmqZm!,.                                     
..                 ..  .,Xqmqqwqwwqqppmp;q}^0pd-xZZ;,lwmwqqpm;..^dt:^,)ZZ-1mbwi.   .    ....    ..                      
..                     . .. .^.^, ... ,!:X_pdwL^:CZmwwwc?:.,^ .:OppwC;.rqmQ^  ......^. .     .                          
..                           ..       ^ ..^..IZdpI^.^ ^... .  ^^ .fLqqu^_^^^ ....]wmmI.                                 
..                                        ^.;ppXpqmm~. ...  ^ ,-wmqqwO0^ :>Qbiqqwwpw:.                                  
..                                         IQQ:.:IXC,:. +rI,^O_:.}cCmbdZ0Zb0!.^:wdwU^^.                                 
..                                        ^^m>qwt>:(mm;l;lia<.^jmI0mwbZ<wpm;bmwwpO!.                                    
..                                        ...^.^^^zpQlcw+[_pp^1Xw!qpq0iZOY^,;;mmk;^.                                    
..                                       ..^...^)wqUIqmZI^im;(!qOv];_]:0Iwwmmmql...                                     
..                                     .:pZwOY0ZqO,+qU,.:}bz,]Zp;.  ,,cjl.{qmbI.                           .            
..                                    ^.^. .;vC:. ^, :O!l:Zqmwm^ .  .^:Zqpqd;.                                          
..                                          . ..    ..^ ..  ..^.    .. ^bZ:                  .                        . 
..                                                              ..   ..^ ..^.                                           
..                                                                                                                    
    '''
    l = colored(logo, 'cyan')
    return l

def logo1():
    logo = '''
    
      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOKMMOOOOOOOOOOOOOOOOOMMMOOOOOOOLPo
  dOOOOOOOKMMOOOOOOOOOOOOOOOOOMMMOOOPOOOOOx
  lOOOOOOOOKMMOOOOOOOOOOOOOOOOOMMMOOOOOOOOl
  .OOOOOOOOKMMOOOOOOOOOOOOOOOOOMMMOOOOOOOO.
   cOOOOOOOKMMOOOOOOOOOOOOOOOOkMMMOOOOOOOc
    oOOOOOOKMMOOOOOOOOOOOOOOOOOMMMOOOOOOo
     lOOOOOKMKMMOOOOOOOOOOOOOOOOOMOOOOOl
      ;OOOOKMKMMOOOOOOOOOOOOOOOMMMOOOO;
       .dOOoKMMOOOOOOOOOOOOOOOOOMxOOd.
         ,kOlKMMOOOOOOOOOOOOOOOOdOk,
           :kk;.OOOOOOOOOOOOO.;Ok:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .
    '''
    l = colored(logo, 'red')
    return l

def logo2():
    logo = '''                    
                                                                  |       ||C ||   )+          /                        
                                                                   C          ||| -~o                                   
                                                                         C      *+f    tC                               
                                                         ||  |L   CCLC<     da]LvL   o8                                 
                                            (           C|||||C  C    JJ p(Xo hW   q M     t                            
                                                     | CC| | |CCL|Y(Q[00zZdkjt~*L**    wbc&Zj1  Wut                     
                                                   |  ||| | |  LbkdOZYZmLn|-b_YL%a*MMkMBMMWM Z/                         
                                                    | |     |Ydpqqpppmqm0-zmk&x|| J  W@ 88                              
                                                    C||    upbmZmqmuOqwCXUQZ   z  k                                     
                                                   ||C   hmwZZO00qpwZZmmJL0X C   r     @       @                        
                                         C  CC J  C    OpmZOOnmmwqm+Zp/UCZQ 1( C      L                                 
                                              L ||   ]pqmwmZm0QZqdddpqp   ) j-C  |   L                                  
                                     | ||  C ||||   pmwqZZmOZddkbqbk&8Q   Cki   Y                                       
                                       || C |C||xm |pqwqqwkkqpdddqbO       CC C                                         
                                           ||||| vnmwwwwqq***bdamqqb   C                                                
                                            C| |C mZL|Zmmbhhoo*OkoW C |  || |C                                          
                                               | 0UOLQmZppak**            |                                             
                                              CCCCXL_0mZpbboak     \   | ||                                             
                                                 Ul0L0ZZbhbax           | C                                             
                                                ^;Cv]QLJbqZq\k|\        | |                                             
                                ||QY0LmmzOQ)~<l_!JJ0JJCUZk0qqw|\|Q |    C||                                             
                               000QqLOCOO0qZ[X+CULQJLC1nUhQbZmmw     L  LCC|                                            
                           CmZCCLCQO0Q00p0qpm?-` MZJOUUYQ\YvuCmmZqdpk      C|                                           
                           L0JvzYJCJ0C0XZZOb(v [mpO0O0QLX_(Z?jZUCJC0)      CCC                                          
                   |   0Q0n0JrruYUQOZZmwmmZmhjJq dpqQCQm0qOxO)ZmCmOOZOmq0tnQZ                                           
            CC    C   YJLJJYuJv0CQ0q0wZmpqmmbbpmw #pCYL+|CO)UCpOQJOLOOY    C(YCnvv  Q                                   
             | |C CCOvUXCJJvOXQLZm0m0mZbqbdZm\b  h| ZJjZzwCm0ZOZZmOZUZ(            mCzj|                                
              || CC QX!\CJcxYLCJmZmmbZZadoaao   C | \ pqmJLvZw0wOmZZpqqQu Q \ Q           L                             
                @||C J)COJvJULxZCwdwqmbmhh            phZwOUQZ[OwOwQZ0 pdbbq                                            
                   O ucuqzLLvJdqakhLhQ                wpqmwZpQQw0mmwZU0|      bC|                                       
                 JUZ wxbL0Q0LZp   ||C#C              addQqduOOmLZYQjpmmUQ|    | C|||                                    
                x     \jQ)mmm0       m\              hbbbpqdmm0Z0ZwZOZmqq0mm  QL|||                                     
               %zbr  O __xZ  \C      bw                a\q*kmOCZUJ0C00O00OdwnQ  \ ||C                                   
               dQ   0 <_*~           J                   qkd|0q(OJOCLCLC0ZOmqmZLO | C                                   
                r   k                                    bbb pZq Z0JLLOCuZZOJXCJQxc \                                   
                   ;%                                     kk  qqwmO0QOL0ZxZq|    C  b                                   
             bh  ] Z                                       a \wwmwZZOC0O0OCJw  Q\   Q \                                 
               %&O                                             mh|qmwZ0U00ZmZm                                          
           UbO &                                                 C|qwwqww0mmwm0qQ        |    m                         
          X m                                               0   \wh  ||\  0ZqqqmqQ                                      
           Z                                                    kQULQbkkkkk\cZpqbQ\                  /                  
                                                                 Q|xX0       amJkkQ                                     
                                                                    Y||        oQUkh                                    
                                                                   \ u\          |qCqbh                                 
                                                                    |\p/           pcZckh0                              
                                                                     Q\ok             mQmpk0\                           
                                                                         b               adbCh                          
                                                                        \ L                  ah                                                                                                                           
    '''
    l = colored(logo, 'cyan')
    return l

def logo3():
    logo='''
                                ...                                                  
                                                                   c''.                                                 
                                                                 .^o*B' ..                                              
                                                      .         ..B"%aaB'.        .                                     
                                                . %@#*8' ^     ..?ob*hr '.                                              
                                                ..8bMa.d@ '    .'ao.<Mab.'                                              
                                          .       'ok/Mb'h ...'.oh*k#W.<".        .                                     
                                                  .8kak.hk_ . 'ok#. *#ah .                                              
                                                   Xah#}o.&. .okkhobh%.d.'                                              
                                                    kakh<dh !ahkhz }*b#'.                .                              
                                                   .khhh#* Mdhkhhboa& `'                 .                              
                                                   .hkhah.%khhhhka'..                                                   
                                                   .&hkha.#kahhhhk^   .                                                 
                                                   ''-ahW%ahahhhhhu.                                                    
                                                   .'^Mk#hhhhhhhhh&.                                                    
                                                  .'.&khhhhhhhhahh8.                                                    
                                                 .'Wahhhhhhhhhb#....                                                    
                                               ..iMqahkkkkhhhhok@..                                                     
                                               ..o88.' .Bbhhhab"..                                                      
                                                 ,.  '.'. 1khhMj``.                                                     
                                                .....0>'~#.p&oph8'`                                                     
                                                   .  .0`&B%^&W.a8&l..                                                  
                                                  . B . Mh*.b.*U*&|o}`                                                  
                                                  .f$ M . '.  @8 } .                                                    
                                                  .. .o..     .'...                                                     
                                                  .    .      .    .....'.                                              
                                              0a  < '   -W "wj   x.'m `. Lc                                             
<<++<><>~+<><<<<<<<<<<<<<<><<<<<<<<<<<<<<<<<<+fw>-<Zi<<)<><+__OCpm<0-{<}n<<<<<<<<<<<<<<<<<<<<<<<<<+>>>~>~><<~~<<~<~~<<<<
<<,'>.l.l'.'"<<<l+i~>+>+i~ <i ~>~>i~><<<<<<<<<<<<<~<<<~~<<~<<<<~~~~<~<~~~~<<<<<<<<<<<<<<<<<<<<<<<<<~+.<,. i .l'<  >  '<<
<<.^!'I'.^"!+<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                         
                                  .    ...                                    .       ..                                
    '''
    l = colored(logo, 'cyan')
    return l

def logo4():
    logo='''
         .,/#%%%%%%(%#%%%%%%%(                                          
                         *#%&(   .,***,,,,,,,...       (&&&&&&%%((              
   //,                    *(%#*         ......    .             #&/.*(%%(/,.    
   %&&(                 ,/           . ...      *%%%%#/*    @/%%%,              
     ,#&(((          ...         .......      ...&@@@@%&&&%%%(*(@&*.            
     ,(*&&,   .%%&&%%.    .........      ....&@@@@@@&&%((/#%&(@%(               
     ,(*@##%((((%/.%&%.. .......  .,*.  .&%%%&%&.      #,%#%########(((/.       
    ,%/#&@&%&&&&@@#*@* . .         ,**, ./##%&%%%%%(/,,.,*##%%&%#/,.            
     /#/@&@&%,    *#/**,..             .,#@@@,(&@@@,(#&%&&@&@(@&*               
      #/@%##%(      .%%%#(#((/***,   ..(@@@@&/&@((#&%&%/(@%@*(&(                
      */%&&(       /%%#(,*((#(***,.*/((#%%@(@@%###(((@#*#@(%/#/                 
      ##@@%&.         %%/,,(%#((%**,#(##%%%,       ./#@#/%@(%(%                 
        (&@#,           *(####/*/#%***%%%#           *%@#(@@#,                  
         #@&                   .,*///*##             *%@(#@@.                   
                                                    /%&(%@@@/                   
                                                     *&&@@&/                    
                                                       &@&&*                    
                                                      %#@@@,                    
                                                      *%@@%                     
                                                        *.                                                                           
    '''
    l = colored(logo, 'yellow')
    return l

def logo5():
    logo='''
                                                                                                                           
                                                     . co##W'                                                           
                                                    haaa' aMom                                                          
                                                   -' Ir##&aW#M1                                                        
                                ,  wMW#Q                oM*###M*W. .          ''OMM*0                                   
                               >ho*###ooW&b^          .zM*########<          bMW######o#+. .                            
                             I#W#########o##p '       ,W#########Maa .     k#############&^                             
                         . U*a##*ooW./######M#M'      MW############h1`"'W#M*###W*t`Mo###oM#c                           
                         #######*q   (#########o#"   .#*############WWo%#M#######M1' .h#*###o#M                         
                     `"Wo*W###@[ . Ua&###M*o####*#o` .^MM*W###############o&a#M*###kY   ?W*####M&.                      
                    j#aa####o`^' o*####&8o`  *######o(..`?################o. '*M######W`...8######*x                    
               `. k*####W&8   .*###o#M*#  '.Mo#######M& '.`JaW############Ma '. Ma#####*8. ..oM*#####*                  
            .   ########j.  /M######8` . vao####o/W*k###&p..  *%o####Mqo*o###oC` "l#oM###oMt ^ tW######8'               
              o###*MMML '"-MMW##&M*.  'x*####W&U`  "o#a*###\   ^#&*&}^ .O&*Mo###/  '`Ma#o###h~` 'Xa*###oMW              
           _######Mo; . ZW*###M*W'   M###ooM*{.       #####W#m `'^,'      ]#M######  ' b##M*###p.  !#&&###oM}           
            !a#**M.`' M*###M*#v.  ,###&MW#&.            h*&###M#.. '         o#*####ol   c***oM###....MMMo*l.           
            ^  '  . oW#*###a".. 0*M###*#&               '.M###*#MM '         ^ *###MoM*0   '#*####*#..  . `             
                  .jo###*k    *####o#p              #o8%..' >o###ooh"        . '' k###*W*# ' .&###o#j'.                 
                        .:..**C_.  ..          .  bb*###&#'..'X*####&W              ..` >ch* `   `                      
                                                .x###*W*^ 'I" `.1M###Ma                                                 
                                               '. .how   I&&**_   >MW '                                                 
                                                  '. ` _#o####M*\ '   .                                                 
                                                     .`  a&#o*k''                                                       
                                                          .;I                                                           
                                                                              
    '''
    l = colored(logo, 'magenta')
    return l

def logo6():
    logo='''
   _______      _________    
  / ____\ \    / /  ____| 
 | |     \ \  / /| |__ 
 | |      \ \/ / |  __|
 | |____   \  /  | |____ 
  \_____|   \/   |______|
    '''
    l = colored(logo, 'white')
    return l

def logo7():
    logo='''
                                   .,,.                  .
                                .\$$$$$L..,,==aaccaacc%#s$b.       d8,    d8P
                     d8P        #$$$$$$$$$$$$$$$$$$$$$$$$$$$b.    `BP  d888888p
                  d888888P      '7$$$$\""""''^^`` .7$$$|D*"'```         ?88'
  d8bd8b.d8p d8888b ?88' d888b8b            _.os#$|8*"`   d8P       ?8b  88P
  88P`?P'?P d8b_,dP 88P d8P' ?88       .oaS###S*"`       d8P d8888b $whi?88b 88b
 d88  d8 ?8 88b     88b 88b  ,88b .osS$$$$*" ?88,.d88b, d88 d8P' ?88 88P `?8b
d88' d88b 8b`?8888P'`?8b`?88P'.aS$$$$Q*"`    `?88'  ?88 ?88 88b  d88 d88
                          .a#$$$$$$"`          88b  d8P  88b`?8888P'
                       ,s$$$$$$$"`             888888P'   88n      _.,,,ass;:
                    .a$$$$$$$P`               d88P'    .,.ass%#S$$$$$$$$$$$$$$'
                 .a$###$$$P`           _.,,-aqsc#SS$$$$$$$$$$$$$$$$$$$$$$$$$$'
              ,a$$###$$P`  _.,-ass#S$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$####SSSS'
           .a$$$$$$$$$$SSS$$$$$$$$$$$$$$$$$$$$$$$$$$$$SS##==--""''^^/$$$$$$'
_______________________________________________________________   ,&$$$$$$'_____

    '''
    l = colored(logo, 'cyan')
    return l


def jihe():
    n = 1999
    while n<=2020:
        try:
            b = 'exp/cve' + '/' + str(n)
            q = os.listdir(b)
            if len(q) != 0:
                s = str(q).replace("'", "").replace('[', '').replace(']', '').replace(',', '')
                tg = colored(s, 'cyan')
                print(tg)
            n += 1
        except:
            break

def shentou():
    cve2011 = '''
CVE-2011-0762 vsftpd拒绝服务漏洞
    '''
    cve2012 = '''
    '''
    cve2013 = '''
    '''
    cve2014 = '''
CVE-2014-0160>>openssl心脏出血漏洞

CVE-2014-4878、CVE-2014-4879、CVE-2014-4880>>>海康威视（Hikvision）安防监控录像机曝远程代码执行漏洞在RTSP（TCP/IP协议体系中的双向实时流传输协议）的请求body、   
                                               请求头以 及基础认证处理中，通过某种手法实现缓冲区溢出。接下来即使不经过认证，黑客也能实现远程任意。

CVE-2014-4878>>RTSP请求处理机制使用了一个固定大小为2014字节的缓冲区，来填充http请求body。如果你发送一个更大的body会导致缓冲区溢出。
               这个漏洞可以被利用来进行代码执行。 但Rapid7公司认为这个漏洞实为拒绝服务攻击。   
    '''
    cve2015 = '''

    '''
    cve2016 = '''

    '''
    cve2017 = '''

Nginx整数溢出漏洞 CVE-2017-7529>> 当使用nginx标准模块时，攻击者可以通过发送包含恶意构造 range 域的 header 请求，来获取响应中的缓存文件头部信息。在某些配置中，
                                 缓存文件头可能包含后端服务器的IP地址或其它敏感信息，从而导致信息泄露。

CVE-2017-0143>>永恒之蓝（ms17_010）

CVE-2017-7269>>IIS 6.0RCE漏洞，IIS 6.0默认不开启WebDAV,一旦开启了WebDAV,安装了IIS6.0的服务器将可能受到该漏洞的威胁

CVE-2017-11882>>隐藏17年之久的Office远程代码执行漏洞（CVE-2017-11882），该漏洞影响目前所有流行的Office软件。360核心安全高级威胁应对团队持续跟踪和关注该漏洞的进展，
                并于北京时间11月21日18点45分全球首次截获到了该漏洞的真实攻击！攻击者可以利用该漏洞向中招用户电脑中植入远控木马或后门程序等恶意程序

CVE-2017-5753>>intel漏洞 

CVE-2017-13156>>Janus签名漏洞可以让攻击者绕过安卓系统的signature scheme V1签名机制，进而直接对App进行篡改。
                而且由于安卓系统的其他安全机制也是建立在签名和校验基础之上，该漏洞相当于绕过了安卓系统的整个安全机制

 '''
    cve2018 = '''
CVE-2018-4878>>利用flash的漏洞来进行攻击，如果受害者的flash版本在28.0.0.137及其之前，那么攻击者可以通过诱使受害者点击链接访问特定网页来控制受害者的电脑
               **cve-2018-4878.py**为exploit生成脚本，shellcode用metasploit生成，默认的为**Windows弹计算器的payload**。

CVE-2018-4407>>该漏洞使得攻击者只要接入同一Wi-Fi网络，即可向其他毫不知情的用户发送恶意数据包来触发任何Mac或iOS设备的崩溃和重启。
               由于该漏洞存在于系统网络核心代码，因此任何反病毒软件均无法防御。

CVE-2018-6389>>漏洞点位于load-scripts.php处，该文件是为WordPress管理员设计的，允许将多个JavaScript文件加载到一个请求中，
               但研究人员注意到可以在登录之前调用该函数来允许任何人调用它，即任何人都可以调用它。通过构造特殊的payload可导致服务器执行181个I/O操作，
               并发请求的情况下即可达到Dos的效果

CVE-2018-8174>>针对IE浏览器的一个远程代码执行漏洞，是Windows VBScript Engine 代码执行漏洞，由于VBScript脚本执行引擎（vbscript.dll）存在代码执行漏洞，
               攻击者可以将恶意的VBScript嵌入到office文件或者网站中，一旦用户不小心点击，远程攻击者可以获取当前用户权限执行脚本中的恶意代码

CVE-2018-8373>>VBScript引擎处理内存中对象的方式中存在一个远程执行代码漏洞。该漏洞可能以一种攻击者可以在当前用户的上下文中执行任意代码的方式来破坏内存

CVE-2018-8420>>Msxml 解析器漏洞

CVE-2018-9206>>Apache jQuery-File-Upload未经身份验证的任意文件上传漏洞

CVE-2018-9341>>Google Android中的Media framework组件存在远程代码执行漏洞。远程攻击者可利用该漏洞执行代码。

CVE-2018-15982>> Adobe Flash Player任意代码执行

CVE-2018-19518>>PHP imap_open函数任意命令执行漏洞

CVE-2018-20250>>WinRAR目录穿越漏洞
    '''
    cve2019 = '''
CVE-2019-5475>> Nexus Repository Manager2.x远程命令执行漏洞  Nexus Repository Manager 2.X存在远程命令执行漏洞，该漏洞默认存在部署权限账号，
                         成功登录后可使      用“createrepo”或“mergerepo”自定义配置，可触发远程命令执行

CVE-2019-7238>> Nexus Repository Manager3远程命令执行漏洞  Nexus Repository Manager 2.X存在远程命令执行漏洞，该漏洞默认存在部署权限账号，
                         成功登录后可使      用“createrepo”或“mergerepo”自定义配置，可触发远程命令执行

CVE-2019-0538>>针对Win7-Win10的Windows JET引擎Msrd3x40 dll中的一个代码执行漏洞构造精心的mdb文件可在解析mdb文件时释放无效的堆地址会发生堆损坏，导致代码执行漏洞

CVE-2019-0708>>3389RCE 火过就不用介绍了吧

    '''
    cve2020 = '''
CVE-2020-0022>> 安卓蓝牙漏洞487/5000 这个poc在android 8.1.0上应该是稳定的，一旦它遇到截断数据包，崩溃。但它的云是非常不稳定的，在三星s9 plus肯定不稳定。
                -在raspberry pi 3B上运行poc测试成功。-在thinkpad x1c 2018上在windows 10上运行vmware的ubuntu/arch，或者在mac os x上运行pd的ubuntu不能运行截断代码，不知道为什么。

CVE-2020-0618>> mssql/sqlseverRCE 

CVE-2020-1938>> tomcat文件包含及RCE ghostcat       

CVE-2020-0796>>微软smbRCE部分

CVE-2020-1350>> Windows DNS Server蠕虫级远程代码执行

CVE-2020-2555>>WebLogic RCE漏洞

CVE-2020-5254>>NetHack是一款角色扮演类单人游戏。 NetHack 3.6.6之前版本中存在缓冲区错误漏洞。攻击者可利用该漏洞提升权限

CVE-2020-8597>>LINUX系统PPPD远程代码执行漏洞

CVE-2020-9380>> 基于Web的电视播放器IPTV Smarters WEB TV PLAYER命令执行

CVE-2020-14645>>WebLogic 反序列化洞 通过T3协议进行利用，攻击者可以实现远程代码执行

CVE-2020-15778>> openSSH鸡肋命令注入
    '''
    print(cve2011, cve2012, cve2013, cve2014, cve2015, cve2015, cve2016, cve2017, cve2018, cve2019, cve2020)


def tiquan():
    cve2011 = '''  
    '''
    cve2012 = '''   
    '''
    cve2013 = '''
    '''
    cve2014 = '''
CVE-2014-4113>>本地提权 Microsoft Windows下的 win32k.sys是Windows子系统的内核部分，是一个内核模式设备驱动程序，它包含有窗口管理器、后者控制窗口显示和管理屏幕输出等。
               如果Windows内核模式驱动程序不正确地处理内存中的对象，则存在一个特权提升漏洞。成功利用此漏洞的攻击者可以运行内核模式中的任意代码。
               攻击者随后可安装程序；查看、更改或删除数据；或者创建拥有完全管理权限的新帐户

    '''
    cve2015 = '''
    '''
    cve2016 = '''
    '''
    cve2017 = '''
    '''
    cve2018 = '''
CVE-2018-8120>>Server 2008 R2 以下的内核提权漏洞
    '''
    cve2019 = '''
    '''
    cve2020 = '''     
CVE-2020-3950>> 存在于VMware Fusion，VMRC for Mac 和Horizon Client for Mac中的权限提升漏洞（CVE-2020-3950），由于VMware错误的使用了setuid，攻击者利用此漏洞可将目标系              统中的普通用户权限提升至管理员权限             

CVE-2020-0683>>Windows MSI“安装程序服务”特权提升

CVE-2020-0796>>微软smb提权部分
    '''
    print(cve2011, cve2012, cve2013, cve2014, cve2015, cve2015, cve2016, cve2017, cve2018, cve2019, cve2020)




