from dateutil.relativedelta import relativedelta
from faker import Faker
import random
from datetime import datetime

class FakerDemo:
    def __init__(self):
        # Instantiate the Faker object with "zh-CN" for generating Chinese data
        self.fake = Faker("zh-CN")

    def calculate_age(self, zjbh):
        today = datetime.now()
        birth_date = datetime.strptime(zjbh[6:14], "%Y%m%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def calculate_fznl(self, csrq, zjqsrq):
        csrq_date = datetime.strptime(csrq, "%Y%m%d")
        zjqsrq_date = datetime.strptime(zjqsrq, "%Y%m%d")
        # fznl = relativedelta(zjqsrq_date, csrq_date).months / 12
        # fznl = (zjqsrq_date - csrq_date).days / 365
        delta = relativedelta(zjqsrq_date, csrq_date)
        fznl = delta.years + delta.months / 12
        # delta_months = (zjqsrq_date.year - csrq_date.year) * 12 + (zjqsrq_date.month - csrq_date.month)
        # print(f"csrq: {csrq}",f"zjqsrq: {zjqsrq}",f"delta_months: {delta_months}")
        # fznl = delta_months / 12
        return fznl

    def calculate_zjjzrq(self, fznl):
        if fznl < 46:
            if fznl < 16:
                l_zjyxq = 5
            elif fznl >= 16 and fznl < 26:
                l_zjyxq = 10
            elif fznl >= 26 and fznl < 46:
                l_zjyxq = 20
        else:
            l_zjyxq = None

        if l_zjyxq:
            l_zjqsrq = datetime.strptime("20200307", "%Y%m%d")
            zjjzrq = (l_zjqsrq + relativedelta(months=l_zjyxq * 12)).strftime("%Y%m%d")
        else:
            zjjzrq = "30001231"

        return zjjzrq

    def person(self, count):
        msg = ""
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
            msg += f"{KHMC},{ZJLB},{ZJBH},{zjjzrq}\n"
        return msg


if __name__ == '__main__':
    f = FakerDemo()
    data = f.person(1000)

    with open("sanyaosu06.csv", 'w') as d:
        # d.write("ID,Name,Age,ZJLB,ZJBH,FZNL,ZJJZRQ\n")
        d.write(data)
