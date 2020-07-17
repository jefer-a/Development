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



def function():
    loop=["圆","正方形","长方形","矩形"]

    #提取路径类型
    for k in loop:
        if k in txtstr:
            flagtype=k
            print("k=",k)
            print(txtstr)

            
    #提取数值
    def lengthfun():
        global length
        if li.count("米")>0:
            length=li[li.index("米")-1]
            print(length)
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
    if flagtype==loop[1]:
        print("flagetype=正方形")
        if "边长" in txtstr:
            if lengthfun():
                vel_cmd()
                print("边长=",length,"米的正方形")
                ttsfun()

    #长方形
    if flagtype==loop[2] or flagtype==loop[3]:
        print("flagetype=长方形")
        if ('长' in li) and ("宽" in li):
            ttsfun()



for i in txt:
    li=jieba.lcut(i,cut_all=True)
    print(li)
    txtstr=i
    function()


            
        
    
