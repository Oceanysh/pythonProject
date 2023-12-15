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

    def person(self, count):
        msg = ""
        for i in range(count):
            num = i + 1
            while True:
                ZJBH = self.fake.ssn()
                age = self.calculate_age(ZJBH)
                if 19 <= age <= 69:
                    break
            KHMC = self.fake.unique.name()
            ZJLB = 0
            msg += f"{KHMC},{ZJLB},{ZJBH}\n"
        return msg


if __name__ == '__main__':
    # Instantiate the FakerDemo object
    f = FakerDemo()
    # Generate information for 1000 persons (ID, Name, Age, ZJLB, ZJBH)
    data = f.person(1000)

    with open("sanyaosu00.csv", 'w') as d:
        # d.write("ID,Name,Age,ZJLB,ZJBH\n")  # Add header for the CSV file
        d.write(data)
