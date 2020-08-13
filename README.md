# Poc-M
python3 main.py 
适用于linux和windows  目前macos可能会有点bug
    本脚本为管理复杂繁多的exp/poc而作,为平时工作提高效率，考虑到平时工具使用习惯，部分命令与其他工具尽量相同，风格我们尽量贴近msf，
包含渗透和提权exp/poc 内置脚本默认皆为已公开nday。风格我们尽量贴近msf，包含渗透和提权exp/poc，目前按照cve 、组件、cms、os分类，并
且cve编号目录名的cve务必大写，OA、下载等系统可按照cms分类。所有目录下分类优先按照CVE编号分类，若无，则退而求其次。
                                 
                                 
                                 
    show cve                  查看poc列表 使用时为进入该poc目录
    show shentou              来查看渗透poc模块大致清单 
    show tiquan               查看提权模块大致清单
    show log                  查看更新日志
    exit                      退出
    set                       进入指定类别 set cve 进入poc目录                    
    fcd                       返回上级
    部分poc内有帮助手册，可用在该poc目录下输入help查看。后续可以添加其他命令 
    
******************************************************************************************************************************** 
    use <module>
    -h/--help             
    -v/--cve                      进入指定cve路径
    -c/--cms                      进入指定cms路径
    -p/--plugin                   进入指定组件路径
    -w/--windows -l/--linux       进入指定系统路径
                                  
    实例：   use -v 2020-1938 
            use -c cms
            use -p nginx
            use --linux centos5.5              直达poc下                

env下适用于windows的模块上传至网盘或者自行编译，访问github太慢，就懒得放了。
链接: https://pan.baidu.com/s/1Xm2Ti47MCwt1KeHdpbpQQQ  密码: rew9
