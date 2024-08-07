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
        delta = relativedelta(zjqsrq_date, csrq_date)

        # Adjust the fznl logic
        years = delta.years
        if (zjqsrq_date.month, zjqsrq_date.day) < (csrq_date.month, csrq_date.day):
            years -= 1
        if years == 70 and (zjqsrq_date.month, zjqsrq_date.day) == (csrq_date.month, csrq_date.day):
            years = 70  # Special case for 70 years old
        fznl = years
        return fznl

    def calculate_zjjzrq(self, fznl):
        if fznl >= 46:
            return "30001231"
        elif fznl < 16:
            l_zjyxq = 5
        elif 16 <= fznl < 26:
            l_zjyxq = 10
        elif 26 <= fznl < 46:
            l_zjyxq = 20
        else:
            l_zjyxq = None

        if l_zjyxq:
            l_zjqsrq = datetime.strptime("20200307", "%Y%m%d")
            zjjzrq = (l_zjqsrq + relativedelta(years=l_zjyxq)).strftime("%Y%m%d")
        else:
            zjjzrq = "30001231"

        return zjjzrq

    def get_yhdm(self, yyb):
        if yyb == 1:
            yhdm = "57001"
        elif yyb == 405:
            yhdm = "77001"
        elif yyb == 7021:
            yhdm = "47001"
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

    with open("sanyaosu2024062801.csv", 'w') as d:
        d.write(data)

        # Test cases to verify the logic
        test_data = [
            {"csrq": "19731028", "zjqsrq": "20200307", "expected_zjjzrq": "30001231"},
            {"csrq": "20030726", "zjqsrq": "20200307", "expected_zjjzrq": "20300307"},
            {"csrq": "19931115", "zjqsrq": "20200307", "expected_zjjzrq": "20400307"},
        ]

        f = FakerDemo()

        for data in test_data:
            fznl = f.calculate_fznl(data["csrq"], data["zjqsrq"])
            zjjzrq = f.calculate_zjjzrq(fznl)
            print(
                f"csrq: {data['csrq']}, zjqsrq: {data['zjqsrq']}, fznl: {fznl}, zjjzrq: {zjjzrq}, expected_zjjzrq: {data['expected_zjjzrq']}")
            assert zjjzrq == data["expected_zjjzrq"], f"Test failed for csrq: {data['csrq']}"

        print("All tests passed.")