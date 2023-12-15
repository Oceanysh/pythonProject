
from dateutil.relativedelta import relativedelta
from datetime import datetime

def calculate_fznl(csrq, zjqsrq):
    csrq_date = datetime.strptime(csrq, "%Y%m%d")
    zjqsrq_date = datetime.strptime(zjqsrq, "%Y%m%d")
    fznl = relativedelta(zjqsrq_date, csrq_date).months / 12
    return fznl

def calculate_zjjzrq(fznl, l_zjqsrq):
    l_zjqsrq_date = datetime.strptime(l_zjqsrq, "%Y%m%d")
    l_zjyxq = relativedelta(l_zjqsrq_date, relativedelta(years=fznl)).years
    if l_zjyxq < 46:
        if l_zjyxq < 16:
            l_zjyxq = 5
        elif l_zjyxq >= 16 and l_zjyxq < 26:
            l_zjyxq = 10
        elif l_zjyxq >= 26 and l_zjyxq < 46:
            l_zjyxq = 20
    else:
        l_zjyxq = None

    if l_zjyxq:
        zjjzrq = (l_zjqsrq_date + relativedelta(years=l_zjyxq)).strftime("%Y%m%d")
    else:
        zjjzrq = "30001231"

    return zjjzrq

l_csrq = "19940310"
l_zjqsrq = "20200307"
fznl = calculate_fznl(l_csrq, l_zjqsrq)
zjjzrq = calculate_zjjzrq(fznl, l_zjqsrq)

print(f"fznl: {fznl}")
print(f"zjjzrq: {zjjzrq}")