from datetime import date
from abc import ABC, abstractmethod
from healthUtil import Inbody, ActivityLevel, Workout

' 貨幣是由金額與幣值所決定的 '


class Currency:
    ''' 封裝金額與幣值，提供錢幣的處理 

    Attributes
      - amount: 金額
      - symbol: 貨幣
    '''
    NTD_RATE = 30

    def __init__(self, amount, symbol='NTD'):
        ' 預設是台幣 '
        self.amount = amount
        self.symbol = symbol

    def __add__(self, other):
        ''' 兩金額相加，注意要換匯率 '''

        if (self.symbol != other.symbol):
            new_amount = self.amount + \
                Currency._convert(other.symbol, self.symbol, other.amount)
        else:
            new_amount = self.amount + other.amount

        return Currency(new_amount, self.symbol)

    def __sub__(self, other):
        ''' 兩金額相減，注意要換匯率 '''

        if (self.symbol != other.symbol):
            new_amount = self.amount - \
                Currency._convert(other.symbol, self.symbol, other.amount)
        else:
            new_amount = self.amount - other.amount

        return Currency(new_amount, self.symbol)

    def __le__(self, other):
        ''' less equal 比較是否比 other 小 '''

        diff = (self - other)
        return True if diff.amount <= 0 else False

    def __ge__(self, other):
        ''' greater equal; 比較是否大於小於 other '''

        diff = (self - other)
        return True if diff.amount >= 0 else False

    def __eq__(self, other):
        ''' 比較兩個金額是否相同 '''

        diff = (self - other)
        return True if diff.amount == 0 else False

    def _convert(sy1, sy2, amount):
        ''' 匯率的轉換，目前僅支援台幣美金的轉換 '''

        rate = {('USD', 'NTD'): Currency.NTD_RATE,
                ('NTD', 'USD'): 1/Currency.NTD_RATE}
        if (sy1, sy2) in rate:
            return rate[(sy1, sy2)] * amount
        else:
            raise Exception('No such currency')

    def __str__(self):
        return f'{self.symbol}{self.amount:,.0f}'

'''
    BankAccount 封裝一個人的銀行帳戶資訊與功能。
    可能存款提款等。
    金錢的單位是 Currency。
'''
class BankAccount:
    """銀行帳戶

    Attributes:
    ----------
    title: str 
        開戶者的名稱
    balance : Currency
        存款
    """
    def __init__(self, title, balance: Currency):
        self._title = title
        self._balance = balance

    def deposit(self, amount: Currency):
        ''' 存款 '''
        self._balance = self._balance + amount

    def withdraw(self, amount: Currency):
        ''' 提款 '''
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise Exception(f"餘額不足")

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"{self._title}的帳戶目前有 {self._balance}"


class Person:
    """ 封裝一個人的資訊。

    著重在一個人的健康資訊、參與的社團與公司，以及銀行帳戶

    Attributes
    ----------
    name : str
        name of the person
    height : float
        身高，單位公尺
    weight : float
        體重，單位公斤
    bodyFat : float
        體脂肪率，不可大於 1 的 float; 越高表示脂肪越高
    inbody : Inbody
        身體質量狀態, Inbody.OVERWEIGHTED, ... 等    
    age : int
        年齡
    bankAccount : BankAccount
        銀行帳號，必須透過 apply() 來設定; 初始為 None
    gym : Gym
        所參與的健身房; 初始為 None
    group : HGroup
        所參與的健康社群; 初始為 []        
    """

    def __init__(self, name, height, weight, bodyFat=None, age=None):
        ''' 依據姓名身高體重等資訊生成 Person 物件 '''
        self._name = name
        self._height = height
        self._weight = weight
        self._bodyFat = bodyFat
        self._age = age
        self.__bankAccount = None
        self._gym = None
        self._groups = []
        self._company = None
        self._salary = None
        self.updateInbody(height, weight, bodyFat)

    @property
    def name(self):
        return self._name

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def bodyFat(self):
        return self._bodyFat

    @property
    def age(self):
        return self._age

    @property
    def inbody(self):
        return self._inbody

    @property
    def BMI(self):
        return self._BMI

    def updateInbody(self, height=None, weight=None, bodyFat=None):
        ''' 更新身高質量，包含身高體重體脂肪。更新後，也會重新計算 BMI 及 inbody 的狀態。
        '''

        self._height = round(height, 2) if height is not None else self._height
        self._weight = round(weight, 2) if weight is not None else self._weight
        self._bodyFat = round(
            bodyFat, 2) if bodyFat is not None else self._bodyFat
        self._BMI = Inbody.bmi(self._height, self._weight)
        self._setInbody()

    def _setInbody(self):
        ''' 設定 inbody, 太輕、太重或是健康 '''

        if (self._BMI < 18):
            self._inbody = Inbody.TOO_LIGHT
        elif (self._BMI > 24):
            self._inbody = Inbody.OVER_WEIGHTED
        else:
            self._inbody = Inbody.FIT

    def getInbodyInfo(self):
        ''' 回傳細部的身體指數，包含身高體重, BMI, 體脂肪率及 inbody 的狀態 '''

        return f'👤{self._name} Inbody: {self._height}m, {self._weight}kg, BMI={self._BMI}, bodyFat={self._bodyFat}, inbody={self._inbody}'

    def join(self, group) -> None:
        ''' 參與一個社群; 同時會呼叫 group.add() 成為雙邊關係 '''

        if (group not in self._groups):
            self._groups.append(group)
            group.add(self)

    def workFor(self, company) -> None:
        ''' 加入公司工作; 同時會呼叫 company.hire() 建立雙邊關係 '''

        if (self._company is not None):
            if self._company != company:
                # work for new company
                self._company = company
                company.hire(self)
        else:
            # first job
            self._company = company
            company.hire(self)

    def getBalance(self) -> Currency:
        ''' 回傳所連結的銀行帳戶的餘款 '''

        return self.__bankAccount.balance

    def getBalanceInfo(self) -> str:
        ''' 回傳帳務資訊的字串 '''

        return f'👤{self._name}存款：{self.__bankAccount.balance}'

    @property
    def bankAccount(self) -> BankAccount:
        return self.__bankAccount

    @bankAccount.setter
    def bankAccount(self, bankAccount) -> None:
        ''' 連接帳戶，當帳戶名稱與本人名字不同時則無法成功 '''

        if bankAccount._title != self._name:
            raise Exception('Error bank account setting')
        self.__bankAccount = bankAccount

    def showBalance(self) -> None:
        ''' 印出姓名與帳戶存款 '''

        print(f"Balance of 👤{self._name}: {self.getBalance()}")

    def registerGym(self, gym):
        ''' 報名健身房; 同時呼叫 gym.add() 建立雙邊關係 '''

        if gym != self._gym:
            self._gym = gym
            gym.add(self)

    def workout(self, workout, duration=60, date=None, times=60):
        ''' 健身後可以減重，進而變更 BMI, 同時產生健身紀錄

        - 必須先檢查是否已經加入健身房，若無則拋出例外
        - 呼叫 workout 物件來取得可減重的重量
        - 呼叫 setInbody 來重設 inbody 數值

        Parameters:
            duration(int) 健身時長，單位分鐘
            date(str) 健身日期
            times(int) 從健身日期起的連續的次數

        Return: None

        Exception: 
            Exception(未加入健身房)
        '''

        if self._gym is None:
            raise Exception("還沒有加入任何健身房")

        # 減重
        loss = workout.weightLoss(self._weight, duration, times)
        self.updateInbody(weight=self._weight - loss)

    def getLifeInfo(self) -> str:
        ''' 回傳此人的一般生活資訊, 包含參與的社團，公司，健身房與帳戶存款 '''

        if len(self._groups) != 0:
            g = f"參與{','.join(list(map(str, self._groups)))}等群組"
        else:
            g = '未參加任何群組'
        if self._company is not None:
            w = f"在{self._company}工作"
            if self._salary is not None:
                w += '(薪水{self._salary}k)'
        else:
            w = '目前沒有工作'
        if self._gym is not None:
            gym = f"在{self._gym.title}健身"
        else:
            gym = '目前沒有參加健身房'
        if self.__bankAccount is not None:
            balance = f"有{self.__bankAccount.balance}存款"
        else:
            balance = '目前沒有銀行帳戶'

        return f'👤{self._name}: ' + ';'.join([g, w, gym, balance])

    def __str__(self):
        ''' 回傳 inbody 和 life 相關的資訊 '''

        body = self.getInbodyInfo()
        life = self.getLifeInfo()

        return '\n'.join([body, life])


class Student(Person):
    """ Student 有一個主額外的資訊：主修科目，其餘與 Person 同 """

    def __init__(self, name, height, weight, bodyFat=None, age=None, major=None):
        super().__init__(name, height, weight, bodyFat, age)
        self.major = major

class HGroup(ABC):
    """抽象的健康群組
    
    HGroup (Health Group) 是一個抽象的類別, 
    封裝一個重視健康的群組應有的功能，
    包含回傳一個群體的平均 BMI, 以了解群組的健康度
    包含可以查詢回傳某一個健康狀態（例如過重）的子群
    """

    def __init__(self, title):
        ''' 
            建立一個健康為主題的群組， title 為群組的名稱，
            同時會初始化 members 列表，以儲存群組的會員。
        '''

        self._title = title
        self._members = []

    @property
    def title(self):
        return self._title

    def add(self, person):
        ''' 將某人加入此群組，會同時呼叫 person.add 建立雙邊關係 '''

        if (person not in self._members):
            self._members.append(person)
            person.join(self)

    def isMember(self, person):
        ''' 回傳是否為會員 '''
        return person in self._members

    def avgBMI(self) -> float:
        ''' 回傳此群組的平均 BMI '''

        tot = 0
        for p in self._members:
            tot += p.BMI
        return round(tot/len(self._members), 2)

    def getBmiAvgInfo(self) -> str:
        ''' 回傳此群組的平均 BMI 的字串訊息 '''

        s = f'🎇{self._title}的成員平均 BMI 為{self.avgBMI()}'
        return s

    def getMembers(self) -> str:
        ''' 回傳此群組的所有成員所形成的字串，以 , 連結 '''

        return ','.join(list(map(str, self._members)))

    def queryByInbody(self, status) -> list():
        ''' 回傳符合某一健康狀態 (inbody) 的所有人所形成的 list
        Parameters:
            status : Inbody
                過重, 過輕或體態合宜

        Return: list
            滿足所有 status 狀態的人    

        Exception: 查無此體態
        '''

        if status not in Inbody:
            raise Exception('查無此體態')
        r = set()
        for p in self._members:
            if p._inbody == status:
                r.add(p)
        return r if len(r) != 0 else None

    @abstractmethod
    def show(self):
        ''' 抽象方法，不同群體的目的不同，所以描述的方式也不同 
        
        印出群組的描述。
        '''
        pass

    def __str__(self) -> str:
        return self._title




class HighShoolClub(HGroup):
    """ 高中社團是一種 HGroup，所以必須實踐 show()

    Attributes
        school : str 
            校名
    """

    def setSchool(self, school):
        ''' 設定此社團所屬的高中校名 '''

        self.school = school

    def show(self):
        content = f'🎇{self.title} 是學校合法成立高中社團，定期近期促進健康的講演'
        if len(self._members) > 0:
            member_names = [m.name for m in self._members]
            content += "我們的成員有 " + ", ".join(member_names)
            content += '。'
        return (content)




class Company:
    """ 公司有公司名稱、資產及員工等屬性。

    Attributes
        title : str
            公司名稱
        asset : Currency
            公司資產    
    """

    def __init__(self, title, asset=None):
        ''' 建立一個公司，包含名稱及資產的屬性
        Parameter
            title(str): 公司的名稱
            asset(Currency): 公司的初始資產金額
        '''
        self._title = title
        self._asset = asset
        self._employees = []

    def paySalary(self, employee, currency):
        ''' 付薪水，該員工的戶頭會增加錢，公司的資本減少 

        Parameter
            employee(People): 受薪的員工
            currency(Currency): 薪水
        Return
            None
        Exception
            - 發薪給未僱用的人                        
            - 受薪者還沒有設定帳戶
        '''

        if (not self.isHired(employee)):
            raise Exception('You have to hire before paying salary')
        if employee.bankAccount is None:
            raise Exception(f'{employee.name}要先申請帳號才能給薪水')
        employee._salary = currency
        employee.bankAccount.deposit(currency)
        self._asset = self._asset - currency

    def earnMoney(self, currency):
        ''' 公司營收，資本增加 '''

        self._asset = self._asset + currency

    def hire(self, person):
        ''' 雇用員工

        employee 的 list 會加入此 person
        要先檢查是否已經聘用了, 因為可能透過員工.workFor() 加入公司
        '''

        if (not self.isHired(person)):
            self._employees.append(person)
            person.workFor(self)

    def isHired(self, person):
        ''' 回傳是否已經受聘於此公司 '''

        return True if person in self._employees else False

    def subsidize(self, person: Person, amount):
        ''' 補助員工參與健身等活動 

        - 補助前先檢查是否為公司員工
        - 錢會直接匯到該員工的帳戶
        - 公司的資產會因此減少

        Exception:
            受補助的人並不是公司員工
        '''

        if (self.isHired(person)):
            person.bankAccount.deposit(amount)
            self._asset = self._asset - amount
        else:
            raise Exception("Can't subsidize a unempolyed person")

    @property
    def asset(self):
        return self._asset

    def __str__(self):
        return self._title

    def show(self):
        content = f'🏢{self._title}是合法登記的公司，目前資產有{self._asset}'
        print(content)


class Gym(Company, HGroup):
    """健身房

    - 健身房是一個公司，也是一個提倡健康的群組。
    - 多重繼承 Company 與 HGroup 
    """
    def __init__(self, title, asset, memberFee=Currency(0)):
        Company.__init__(self, title, asset)
        HGroup.__init__(self, title)
        self._memberFee = memberFee

    def add(self, person):
        ''' 加入群組

        覆蓋 HGroup.add() 的功能：加入會員須要扣款，健身房資本增加，會員帳戶餘款減少 
        '''

        if person.bankAccount is None:
            raise Exception(f'{person.name} does not apply bank account')
        enoughBalance = person.bankAccount.balance >= self._memberFee
        if not enoughBalance:
            raise Exception(
                f"{person.name} does not have enough funds to join.")
        if not self.isMember(person):
            person.bankAccount.withdraw(self._memberFee)
            self._asset = self._asset + self._memberFee
            super().add(person) # HGroup.add()

    @property
    def memberFee(self):
        return self._memberFee

    @memberFee.setter
    def memberFee(self, newFee):
        ''' 如果會費調漲高過 500, 會產生例外 '''

        if newFee >= self._memberFee + Currency(500):
            raise Exception("Too high member fee")
        self._memberFee = newFee

    def getGymInfo(self):
        ''' 回傳健身房基本資訊，包含資產與會費'''

        return f'🏋️‍♂️{self._title}: asset={self._asset}; fee={self._memberFee}'

    def show(self):
        ''' 印出會員數量，描述健身房狀態'''

        c = len(self._members)
        print(f'目前有{c}個會員，我們提供多項的健身活動、專業的設備'
              f'，以及舒適的環境。')

    def __str__(self):
        return '🏋️‍♂️' + super().__str__()


class Coach(Person):
    """ Coach 是一個 Person, 有額外的健身專長，對體檢的標準也不同 
    Attributes
        expertise : str
            教練的專長
    """
    def __init__(self, p: Person, expertise: str):
        ''' 
        由既有的一個 Person 物件生成一個教練物件

        因為 person 可能有其他的屬性如薪水，公司等，我們必須將之複製過來
        '''

        super().__init__(p.name, p.height, p.weight, bodyFat=p.bodyFat, age=p.age)
        self._expertise = expertise

        # 屬性複製
        for key, value in p.__dict__.items():
            if key not in ('_name', '_height', '_weight', '_bodyFat', '_age'):
                setattr(self, key, value)

        self._setInbody()

    def _setInbody(self):
        ''' 覆蓋 person 中設定 inbody 的值，因為教練的健康要求比較高 

        Exception
            必須設定體脂肪，才能設定 inbody; 若無，會拋出例外
        '''

        if (self._bodyFat is None):
            raise Exception("教練必須設定體脂肪")
        if self._bodyFat > 0.15:
            self._inbody = Inbody.OVER_BODY_FAT
        else:
            if (self.BMI < 19):
                self._inbody = Inbody.TOO_LIGHT
            elif (self.BMI > 22):
                self._inbody = Inbody.OVER_WEIGHTED
            else:
                self._inbody = Inbody.FIT


class Story:
    """ 定義故事每章節分段及裝飾的形式
    """

    chID = 1

    def cover(desc):
        ''' 印出首頁的形式 '''

        print("~"*len(desc))
        print(desc)
        print("~"*len(desc))

    def chapterHead(title, desc=""):
        ''' 印出章節頭形式 '''
        
        print(f'\n===== CHAPTER {Story.chID}: {title} =====')
        print(f"{desc}")
        Story.chID += 1

    def sectionHead(desc):
        ''' 印出小節頭形式 '''

        print(f'\n> {desc}\n')

    def chapterEnd():
        ''' 印出章節尾形式 '''
        pass

    def sectionEnd(desc=""):
        ''' 印出小節尾形式 '''
        print ('')

    def note(desc):
        ''' 印出註解說明形式 '''
        print(f'... {desc}')


def main():
    Story.cover('>>> FROM OVERWEIGHT TO OVERACHIVER <<< ')

    # chapter I
    Story.chapterHead('ABC 三個好朋友')

    Story.sectionHead('Alice, Bob, Charlie 是高中同學的好朋友，他們都用有很不錯的體態。')
    bob = Student('Bob', 1.72, 60,  bodyFat=0.15, age=18, major='Computer')
    charlie = Student('Charlie', 1.80, 72, age=18, bodyFat=0.15, major='Civil')
    alice = Person('Alice', 1.65, 45, age=18, bodyFat=0.12)

    for p in [bob, charlie, alice]:
        print(p)
    Story.sectionEnd()

    Story.sectionHead('他們成立了 Fit ABC 社團，致力推廣健康觀念')
    fit = HighShoolClub('Fit ABC')
    bob.join(fit)
    fit.add(charlie)
    fit.add(alice)
    fit.show()
    for p in [bob, charlie, alice]:
        print(p.getLifeInfo())
    Story.note('社團的平均 BMI 保持得很好')
    print(fit.getBmiAvgInfo())
    Story.sectionEnd()
    Story.chapterEnd()

    # chapter II
    Story.chapterHead('踏出校園')
    Story.sectionHead('出社會後，大家的體態與工作都有所變化')

    Story.note('Charlie成了教練，在一家健身中心工作')
    Story.note('他的身高變高，體脂肪和體重還下降了')
    charlie = Coach(charlie, expertise='舉重')
    charlie.updateInbody(height=charlie.height + 0.05,
                         weight=charlie.weight-5,
                         bodyFat=charlie.bodyFat-0.03)
    moveX = Company('MoveX', Currency(100000))
    charlie.workFor(moveX)

    print(charlie)

    Story.note('Bob 有點宅，也不太不健康')
    bob.updateInbody(weight=bob.weight+20,
                     bodyFat=bob.bodyFat*1.3)
    print(bob)

    # chapter III
    Story.chapterHead('工作賺錢')

    Story.sectionHead('Bob開了銀行帳戶，雖然錢不多')
    bob.bankAccount = BankAccount(title='Bob', balance=Currency(10000))
    print(bob.getBalanceInfo())
    Story.note('也把多年的美金存到戶頭')
    bob.bankAccount.deposit(Currency(10000, "USD"))
    print(bob.getBalanceInfo())

    Story.sectionHead('成功的找到工作')
    successTech = Company(title='成科股份有限公司', asset=Currency(1000000))
    successTech.show()
    successTech.hire(bob)
    # bob.workFor(successTech)
    Story.note(f'薪水 {Currency(50000)}')
    print(bob.getLifeInfo())
    successTech.paySalary(bob, Currency(50000, 'NTD'))
    Story.note('公司最近賺了不少錢')
    successTech.earnMoney(Currency(1500000))
    print(bob.getBalanceInfo())
    successTech.show()

    Story.chapterEnd()

    # Chapter IV
    Story.chapterHead('公司的補助')

    Story.note('雖然業績不錯，但 Bob 的身體不好')
    Story.note('公司鼓勵 Bob 和其他同仁大家都去健身房運動')
    strongLife = Gym('StrongLife',
                     asset=Currency(200000),
                     memberFee=Currency(600))
    print(strongLife.getGymInfo())
    try:
        bob.registerGym(strongLife)
    except Exception as noEnoughFund:
        print(noEnoughFund)
    Story.note('Bob 參加了健身房')
    print(bob.getLifeInfo())

    Story.sectionHead('Jack 報名了健身房，但錢不夠')
    jack = Person('Jack', 1.72, 100)
    jack.bankAccount = BankAccount(jack.name, balance=Currency(10))
    successTech.hire(jack)
    successTech.paySalary(jack, Currency(10))
    try:
        jack.registerGym(strongLife)
    except Exception as noEnoughFund:
        print(noEnoughFund)
    finally:
        print(jack.getBalanceInfo())

    Story.sectionHead('公司補助健身'+str(Currency(500)))
    successTech.subsidize(jack, Currency(500))
    try:
        jack.registerGym(strongLife)
    except Exception as noEnoughFund:
        print(noEnoughFund)
    print('Jack 也加入健身了')
    print(jack.getLifeInfo())

    # Chapter V
    Story.chapterHead('開始健身')
    Story.note('健身前的 Inbody！')
    print(bob.getInbodyInfo())

    Story.note('Charlie 轉職到 StrongLife, 擔任 Bob 的教練')
    bob.workout(Workout.FLYWHEEL, 60, '2023/10/03', 4)
    bob.workout(Workout.AEROBIC_EX, 60, '2023/10/10', 1)
    bob.workout(Workout.SWIM, 60, '2023/10/11', 3)
    bob.workout(Workout.WEIGHT_TRAIN, 60, '2023/10/14', 10)
    bob.workout(Workout.YOGA, 60, '2023/10/20', 10)

    Story.note('健身後體重降低了！')
    print(bob.getInbodyInfo())

    Story.chapterEnd()
                
if __name__ == "__main__":
    main()
    # printDocstring()
