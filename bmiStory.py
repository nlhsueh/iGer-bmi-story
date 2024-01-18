from datetime import date
from abc import ABC, abstractmethod
from healthUtil import Inbody, ActivityLevel, Workout


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

    def getLifeInfo(self) -> str:
        ''' 回傳此人的一般生活資訊, 包含參與的社團 '''

        if len(self._groups) != 0:
            g = f"參與{','.join(list(map(str, self._groups)))}等群組"
        else:
            g = '未參加任何群組'

        return f'👤{self._name}: ' + ';'.join([g])

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

    Story.note('Bob 有點宅，也不太不健康')
    bob.updateInbody(weight=bob.weight+20,
                     bodyFat=bob.bodyFat*1.3)
    print(bob)

    Story.chapterEnd()
                
if __name__ == "__main__":
    main()
    # printDocstring()
