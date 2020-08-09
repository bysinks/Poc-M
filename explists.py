from termcolor import *

def helps():
    logo='''
    [+]Poc-M
    [+]0.0.1
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
    set                       进入指定类别 set shentou/set tiquan 进入渗透/提权poc目录                    
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


