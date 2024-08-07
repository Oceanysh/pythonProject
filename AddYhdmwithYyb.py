from dateutil.relativedelta import relativedelta
from faker import Faker
import random
from datetime import datetime

class FakerDemo:
    def __init__(self):
        self.fake = Faker("zh-CN")

    def calculate_age(self, zjbh):
        today = datetime.now()
        birth_date = datetime.strptime(zjbh[6:14], "%Y%m%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def calculate_fznl(self, csrq, zjqsrq):
        csrq_date = datetime.strptime(csrq, "%Y%m%d")
        zjqsrq_date = datetime.strptime(zjqsrq, "%Y%m%d")
        delta = relativedelta(zjqsrq_date, csrq_date)
        fznl = delta.years + delta.months / 12
        return fznl

    def calculate_zjjzrq(self, fznl):
        if fznl < 46:
            if fznl < 16:
                l_zjyxq = 5
            elif 16 <= fznl < 26:
                l_zjyxq = 10
            elif 26 <= fznl < 46:
                l_zjyxq = 20
        else:
            l_zjyxq = None

        if l_zjyxq:
            l_zjqsrq = datetime.strptime("20200307", "%Y%m%d")
            zjjzrq = (l_zjqsrq + relativedelta(months=l_zjyxq * 12)).strftime("%Y%m%d")
        else:
            zjjzrq = "30001231"

        return zjjzrq

    def get_yhdm(self, yyb):
        if yyb == 1:
            yhdm = "54001"#57001 交行
        elif yyb == 405:
            yhdm = "74001"#77001 交行
        elif yyb == 7021:
            yhdm = "44001"#47001 交行
        else:
            yhdm = ""
        return yhdm

    def person(self, count):
        msg = ""
        yyb_values = [1, 405, 7021]  # 营业部
        for i in range(count):
            num = i + 1
            while True:
                ZJBH = self.fake.ssn()
                age = self.calculate_age(ZJBH)
                if 19 <= age <= 69:
                    break
            csrq = ZJBH[6:14]
            zjqsrq = "20200307"
            fznl = self.calculate_fznl(csrq, zjqsrq)
            zjjzrq = self.calculate_zjjzrq(fznl)

            KHMC = self.fake.unique.name()
            ZJLB = 0
            yyb = random.choice(yyb_values)  # 从营业部里随机选择一个
            yhdm = self.get_yhdm(yyb)
            msg += f"{KHMC},{ZJLB},{ZJBH},{zjjzrq},{yyb},{yhdm}\n"
        return msg

if __name__ == '__main__':
    f = FakerDemo()
    data = f.person(40000)

    with open("sanyaosu2024072600.csv", 'w') as d:
        d.write(data)