import jieba

#语言合成文本函数
def ttsfun():
    print("successfully")

#轨迹移动函数
def vel_cmd():
    print("移动成功")

txt=['','','']

txt[0]="前进345米。"
txt[1]="走一个直径为46米的圆形。"
txt[2]="走一个长为5米宽为2米的长方形。"
txt.append("走一个边长为36米的正方形。")
length=0
wide=0



def function():
    loop=["圆","正方形","长方形","矩形","前进","向前"]
    flagtype="空"
    flagin=0

    #提取路径类型
    for k in loop:
        if k in txtstr:
            flagtype=k
            flagin=1
            print("k=",k)
            print(txtstr)
    if flagin==0:
        return print("非移动命令语句")

            
    #提取数值
    def lengthfun():
        global length,wide
        length=0
        wide=0
        count=li.count("米")
        print("count=",count)
        if count==1:
            length=li[li.index("米")-1]
            print(length)
        elif count==2:
            length=li[li.index("米")-1]
            li.reverse()
            wide=li[li.index("米")+1]
            print("wide=",wide)
        else:
            print("!!!没有移动距离单位")
        return length

    #提取距离类型
    #圆形
    if flagtype==loop[0]:
        print("flagtype=圆形")
        if "半径" in li:
            flagdr="半径"
            if lengthfun():
                vel_cmd()
                print("半径=",length,"米的圆")
                ttsfun()
        elif "直径" in li:
            flagdr="直径"
            if lengthfun():
                vel_cmd()
                print("直径=",length,"米的圆")
                ttsfun()

            
    #正方形
    elif flagtype==loop[1]:
        print("flagetype=正方形")
        if "边长" in txtstr:
            if lengthfun():
                vel_cmd()
                print("边长=",length,"米的正方形")
                ttsfun()

    #长方形
    elif flagtype==loop[2] or flagtype==loop[3]:
        print("flagetype=长方形")
        if ('长' in li) and ("宽" in li):
            if lengthfun():
                vel_cmd()
                print("长=",length,"米宽=",wide,"米的长方形")
                ttsfun()
    #直线
    elif flagtype==loop[4] or flagtype==loop[5]:
        print("flagtupe=直线")
        if lengthfun():
            vel_cmd
            print("前进=",length,"米")
            ttsfun()



for i in txt:
    li=jieba.lcut(i,cut_all=True)
    print('*'*60)
    print(li)
    txtstr=i
    function()
    print("length=",length,"\twide=",wide)
    print('*'*60)

            
        
    
