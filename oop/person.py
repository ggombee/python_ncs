class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'안녕하세요. 제 이름은 {self.name}이고,' 
              f' 나이는 {self.age}살이고,' 
              f' {self.name} 에서 거주합니다.')

    @staticmethod
    def main():
        eunbee = Person('은비',24,'서울')
        eunbee.greeting()
        minjae = Person('민재',27,'경기')
        minjae.greeting()

if __name__ == '__main__':
    Person.main()