from datetime import date
from healthUtil import Inbody

class Person:

    def __init__(self, name, height, weight, bodyFat=None, age=None):
        ''' 依據姓名身高體重等資訊生成 Person 物件 '''
        self._name = name
        self._height = height
        self._weight = weight
        self._bodyFat = bodyFat
        self._age = age
        self.__bankAccount = None
        self._gym = None
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

    def __str__(self):
        ''' 回傳 inbody 和 life 相關的資訊 '''

        body = self.getInbodyInfo()

        # return '\n'.join([body, life])
        return body


class Student(Person):
    """ Student 有一個主額外的資訊：主修科目，其餘與 Person 同 """

    def __init__(self, name, height, weight, bodyFat=None, age=None, major=None):
        super().__init__(name, height, weight, bodyFat, age)
        self.major = major

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
    Story.chapterEnd()
      
if __name__ == "__main__":
    main()
    # printDocstring()
