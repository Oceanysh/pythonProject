from faker import Faker


class FakerDemo:
    def __init__(self):
        # 实例化时，如果要生成中国的数据信息，参数内要加上"zh-CN"
        self.fake = Faker("zh-CN")

    def person(self, count):
        msg = ""
        for i in range(count):
            num = i + 1
            KHMC = self.fake.unique.name()
            ZJLB=0
            ZJBH= self.fake.ssn()
            msg += f"{KHMC},{ZJLB},{ZJBH}\n"
        return msg


if __name__ == '__main__':
    #实例化FakeDemor对象
    f = FakerDemo()
    #生成1000个人的信息(姓名,身份证号)
    data = f.person(1000)
    #print(data)

    with open("sanyaosu.csv",'w') as d:
        d.write(data)