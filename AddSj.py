from faker import Faker


class FakerDemo:
    def __init__(self):
        # 实例化时，如果要生成中国的数据信息，参数内要加上"zh-CN"
        self.fake = Faker("zh-CN")

    def generate_phone(self):
        # 生成11位手机号
        return self.fake.phone_number()

    def person(self, count):
        msg = ""
        for i in range(count):
            num = i + 1
            KHMC = self.fake.unique.name()
            ZJLB = 0
            ZJBH = self.fake.ssn()
            SJ = self.generate_phone()
            msg += f"{KHMC},{ZJLB},{ZJBH},{SJ}\n"
        return msg


if __name__ == '__main__':
    # 实例化FakerDemo对象
    f = FakerDemo()
    # 生成1000个人的信息(姓名,证件类别,证件号码,手机号)
    data = f.person(40000)
    # print(data)

    with open("sanyaosu2024080500.csv", 'w', encoding='utf-8') as d:
        d.write(data)