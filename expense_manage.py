def add_output():               #读取文件，在文件末尾加上信息
    list_all=read_all()
    list_detial=read_detail()
    
    print('支出类型：1-日常餐饮支出   2-学习用品   3-娱乐消费   4-其它支出')
    while 1: #如输入信息有误，重新输入
        try:
            cost_type=int(input("请选择支出类型："))
        except ValueError:
            print('输入错误，未输入有效信息')
            cost_type=5
        if cost_type<5 and cost_type>0:
            break
        else:
            print('请输入正确选项')
    while 1:
        s=input('请依次输入支出具体项目，金额和日期（用逗号分隔）：').split(',')
        if len(s)<4:
            print('未输入正确信息,请检查输入格式')
        else:
            break
            
    
    list_all.append(s)
    list_catgery=list_detial[cost_type-1] #读取对应项支出
    total_amount= float (list_catgery[1])+float(s.split(',')[1]) 
    list_detial[cost_type-1][1]=str(total_amount)
    with open('project\expense_manage\expense.txt','w') as infor_file:
        for i in list_all:
            print(i)
            infor_file.write(i[0]+','+i[1]+','+i[2]+'\n')
    with open('project\expense_manage\category_datail.txt','w') as infor_file:
        for i in list_detial:
            infor_file.write(i[0]+','+i[1]+'\n')
    

def print_output():             #读取文件，打印列表信息
    list_a= read_all()
    if len(list_a==0):
        print('支出金额：0')
        return 0
    print('\n'*2)
    for i in list_a:
        print("--"*50)
        print('项目：{:<10}金额：{:<10}日期：{}'.format(i[0],i[1],i[2]))
    print("--"*50)


def seach_output():             #读取文件，打印特定信息
    list_a=read_detail()
    print('1-日常餐饮支出   2-学习用品   3-娱乐消费   4-其它支出')
    a=int( input('请输入要查询的项目： '))
    print("该项目支出为：{}".format(list_a[a-1][1]))




def statistic_output():          #读取文件，打印加总信息
    list_a=read_detail()
    total=0
    for i in range(4):
        total+=float(list_a[i][1])
    print('总支出：{}'.format(total))


def read_all():              #读取文件expense.txt中明细，以二维列表返回
    list_infor=[]
    with open('project\expense_manage\expense.txt') as infor_file:
        list_infor=[i.rstrip('\n').split(',') for i in infor_file]
    return list_infor


def read_detail():
    list_infor=[]
    with open('project\expense_manage\category_datail.txt') as infor_file:
        list_infor=[i.rstrip('\n').split(',') for i in infor_file]

    return list_infor



#通过文件expense.txt 和 category_detail.txt 存储信息，读取文件进行相关操作
#文件格式示例：espense.txt
# 具体项目，金额，日期

#category_detail.txt
# 种类代号，金额

import os
expense_flie_name='expense.txt'  #文件中以逗号分隔
category_name='category_detail.txt'  
while 1:
    print('='*50)
    print('1-新增支出\n2-打印支出\n3-查询支出\n4查看统计-\n0-退出系统')
    print("="*50)
    fuc_choice=int(input("请输入操作:"))
    if fuc_choice==1:
        add_output()
    elif fuc_choice==2:
        print_output()
    elif fuc_choice==3:
        seach_output()
    elif fuc_choice==4:
        statistic_output()
    elif fuc_choice==0:
        break
    else:
        print('请输入正确的选项')