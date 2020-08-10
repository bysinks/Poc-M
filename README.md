# Poc-M
python3 main.py 
适用于linux和windows  目前macos可能会有点bug

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
                                                             
    use <module>
    
    实例：use 2020-1938    直达poc下 
    
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
