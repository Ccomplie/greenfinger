#1-等额本息
def AveAmo(amount,rate,month):
    rate=rate/1200
    perMonthAmo=amount*rate*(1+rate)**month/((1+rate)**month-1)
    loanTotalAmount=perMonthAmo*month
    print("每月还款额：{:.4f}\n总还款额：{:.4f}".format(perMonthAmo,loanTotalAmount))
    print("总还款金额:{:.4f}".format(loanTotalAmount))

    
#2-等额本金
def AveAmoAndInter(amount,rate,month):
    rate=rate/1200
    monthAmount=amount/month#平均本金
    loanTotalAmount=0#总还款金额
    perMonthAmo=0#每月还款金额
    for i in range(1,month+1):
        perMonthAmo=(amount-monthAmount*(i-1))*rate+monthAmount
        loanTotalAmount+=perMonthAmo
        print("第{}月应还款额：{:.4f}".format(i,perMonthAmo))
    print("总还款额:{:.4f}".format(loanTotalAmount))

amount=float(input("请输入贷款金额："))
rate=float(input('请输入贷款年利率：'))
month=int(input('请输入贷款还款时长(月):'))
print('还款方式：\n     1-等额本息\n     2-等额本金',)
way_loan=int(input('请选择还款方式：'))
if way_loan==1:
    AveAmo(amount,rate,month)
elif way_loan==2:
    AveAmoAndInter(amount,rate,month)
else:
    print('请输入正确的还款方式')