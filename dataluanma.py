from dateutil.relativedelta import relativedelta
from faker import Faker
import random
from datetime import datetime
import csv

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
        fznl = (zjqsrq_date - csrq_date).days / 365
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
            # Calculate zjjzrq based on l_zjyxq
            l_zjqsrq = datetime.strptime("20200307", "%Y%m%d")
            zjjzrq = (l_zjqsrq + relativedelta(months=l_zjyxq * 12)).strftime("%Y%m%d")
        else:
            zjjzrq = "30001231"

        return zjjzrq

    def person(self, count):
        rows = []
        for i in range(count):
            num = i + 1
            while True:
                ZJBH = self.fake.ssn()
                age = self.calculate_age(ZJBH)
                if 19 <= age <= 69:
                    break
            csrq = ZJBH[6:14]
            zjqsrq = "20160307"
            fznl = self.calculate_fznl(csrq, zjqsrq)
            zjjzrq = self.calculate_zjjzrq(fznl)

            KHMC = self.fake.unique.name()
            ZJLB = 0
            rows.append([KHMC, ZJLB, ZJBH, zjjzrq])

        return rows


if __name__ == '__main__':
    # Instantiate the FakerDemo object
    f = FakerDemo()
    # Generate information for 1000 persons (ID, Name, Age, ZJLB, ZJBH, fznl, zjjzrq)
    data = f.person(1000)

    with open("sanyaosu03.csv", 'w', newline='', encoding='utf-8-sig') as d:
        writer = csv.writer(d)
        writer.writerow(["KHMC", "ZJLB", "ZJBH", "ZJJZRQ"])  # Add header for the CSV file
        writer.writerows
