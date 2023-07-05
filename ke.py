
def bt(a):
    a=a*0.01
    return a


def monthly_payment_1(loan_amount,monthly_rete,loan_term): #每月月供参考
    monthly_payment=loan_amount * (monthly_rete * ((1 + monthly_rete) ** (loan_term * 12))) / (((1 +monthly_rete) ** (loan_term * 12)) - 1)
    return monthly_payment

def total_payment_1(monthly_payment,loan_term): #还款总额 
    total_payment=monthly_payment * loan_term * 12 
    return total_payment

rep={
    '商业贷款' :{
        'max': bt(4.90),
        'min': bt(4.75)
        },
    '公积金贷款':{
        'max': bt(3.25),
        'min': bt(2.75)
        },
}

loan_type=''
while True:
    print('1.商业贷款\n2.公积金贷款\n3.组合贷款')
    type = eval(input('请输入选择贷款类型:'))
    match type:
        case 1:
            loan_type='商业贷款'
            break
        case 2:
            loan_type ='公积金贷款'
            break
        case 3:
            loan_type = '组合贷款'
            break
        case _:
            print("无效贷款请重新选择")
            
loan_term=eval(input('请输入贷款年限:'))
if loan_term<=5:
    yar='min'
else:
    yar='max'
    
sun={}
chen=[loan_type]
if type==3:
    chen=['商业贷款','公积金贷款']
for i in chen:
    loan_amount=eval(input(f'请输入{i}金额(万元):')) * 10000
    
    monthly_rete=rep[i][yar]/12 #月利率
    monthly_payment=monthly_payment_1(loan_amount,monthly_rete,loan_term)
    total_payment=total_payment_1(monthly_payment,loan_term)#还款总额 
    interest_payment=total_payment-loan_amount  #支付利息 
    sun[i]=[monthly_payment,total_payment,interest_payment]
    
if len(chen)!=1:
    
    monthly_payment=sun[chen[0]][0]+sun[chen[1]][0]
    total_payment=sun[chen[0]][1]+sun[chen[1]][1]
    interest_payment=sun[chen[0]][2]+sun[chen[1]][2]

print("每月月供参考：{:.2f}".format(monthly_payment))
print("还款总额：{:.2f}".format(total_payment))
print("支付利息：{:.2f}".format(interest_payment))