###### tags: `IGER` `OOD`


# 從超重到卓越 

- From Overweight to Overachiver
(故事取自 與ChatGPT之互動)

有一個名叫鮑伯（Bob）的年輕人，他喜歡吃漢堡身材壯碩，總是被取笑。他有一個夢想，想要在一家大公司工作，但他一直找不到機會。鮑伯被他的朋友戲稱「大鮑勃」(Big Bob)。

高中時期的 Bob 可不是這樣，他和兩位好朋友 Alice 及 Charlie 共同創立一個社團 FitABC，推廣各項運動。除了 Alice 有點太瘦外，大家的平均體態都保持的相當的好，整個社團的平均 BMI 落在 19，相當的好。 

這一天，他看到一個工作招聘廣告，公司名叫「SuccessTech 有限公司」，是和他的本業資訊工程相關的。Bob 毅然決定嘗試一下，儘管他對自己的能力和外表感到缺乏自信。他經歷了一次緊張的面試，運氣不錯的，他被錄取了。

Bob 的工作並不輕鬆，他覺得自己無法跟上快節奏的工作和同事們的能力。但他非常努力工作，每天都加班，認真學習新東西。他的堅韌努力開始吸引同事和上司的關注。

公司的利潤與資產不斷增加，很大一部分要完成 Bob 的努力。他用他自己的方式解決問題，創造了一些令人驚嘆的解決方案。他的同事開始讚賞他的能力，而不再關心他的外表，他的薪水也不斷的上升。

然而，公司的高層開始擔心 Bob 的健康狀況，他的 BMI 是超高的 40。他長時間的加班和不健康的生活方式使他的體重和健康狀況惡化。公司決定採取行動。

他們安排了一次公司健康檢查，結果顯示 Bob 和其他員工們的健康狀況都不好。公司並沒有放棄他們。相反，他們提出了一個計劃，透過實際的補助鼓勵員工加入健身房，改善飲食，這對剛出社會沒有存款的 Jack 幫助特別大。

Bob 報名參加一間名為 StrongLife 的健身房，並參加健身課程，想不到還遇上以前好朋友 Charlie！作為健身教練的 Charlie 有這著更高的體脂肪及 BMI 要求標準，Bob 立刻邀請 Charlie 作為他的個人教練。而昔日的好友 Alice 現在是 Chalie 的老婆，目前是一位營養師。於是 Bob 邀請 Alice 作為他的營養師，改變他的飲食習慣並訂定減重計畫，遵循著好朋友的指導，他的健康狀況逐漸改善。

Alice 先幫 Bob 評估他的 TDEE, 也將是每日消耗的熱量-- 那可以由人體的代謝、運動量所估算出來。如果體脂肪越低則代謝能力越好；運動量高也會消耗更多的熱量。TDEE 如果大於攝取的熱量，則體重會減輕，7000大卡的熱量赤字大約可以減重一公斤。Alice 協助制定的計畫是每天攝取低於 TDEE 500 大卡的熱量，持續一個月; 再以相同攝取熱量為基礎增加活動量一個月，如此反覆的降低熱量攝取與增加運動強度，他們有信心可以協助 Bob 減重。

很快，Bob 變成了一個更健康、更自信、更有活力的人，他喜歡觀看自己的運動紀錄，從一開始低強度的運動（例如 MET=2.5的瑜伽）到現在的高強度運動（例如 MET=13 的跳繩），成就感和汗水一樣不斷的累積。在此同時，他也接管了 SuccessTech 公司，汗水、銀行帳戶、公司資產不斷的增加，也累積了他的成就感，給了他持續前進的動力。

後來，Bob 收購了 StrongLife 健身房，將 SuccessTech 的資料分析技術應用在健身房上，三位好朋友持續在健康科學上大放光彩。

## 關於本教材

* 故事導向-- 透過一個故事導向的方式，提供大家認識物件導向設計的方法。不同於傳統陳述物件特色的教條式解說，物件的世界是直覺而不需要太多陳述的 -- 我們希望大家可以直接進入物件導向程式設計的世界。
* Python-- 採用 Python 語法，雖會講解部分的語言特色，但著重在物件導向設計部分，其餘的略過，所以需要一點 Python 的基礎。
* 物件設計-- 既然是牽涉到設計就應該有設計圖。我們使用 PlantUML 來繪製他的設計圖，希望大家對照設計圖與程式，更容易了解物件設計的思維。
* 測試導向-- 程式要寫就要測，否則你永遠不知道他的對錯。我們特別著重呈現測試碼-- 因為這樣大家會先看到怎麽應用（呼叫）這些物件。這符合物件抽象的巨觀概念，由外而內的了解物件的設計。
* 循序漸進-- 劇中的人物 Bob 從高中，頹廢到發憤圖強的故事，我們拆解成10 個小單元，每一個單元大家會看到一點需求，一點設計，一點測試，循序漸進的了解整個系統。
* 故事產生器-- 我們創建了一個簡單的故事產生類別，透過它來描述 Bob 的故事。


## Story code
```python
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
    bob.showWorkoutLog()

    Story.note('健身後體重降低了！')
    print(bob.getInbodyInfo())

    Story.chapterEnd()

    # Chapter VI
    Story.chapterHead('減重計畫')

    Story.sectionHead('現況評估')
    Story.note('Alice 擔任 Bob 的營養師')
    Story.note('還沒有減重計劃前 Bob 的狀況')
    Story.note('他的活動層級被評斷為坐立，這也帶表他每天消耗的熱量很低')

    act = ActivityLevel.SEDENTARY
    print(getTDEEEstInfo(bob, act))

    Story.note('他每天攝取的熱量大約 3000 大卡，如果這樣持續 30 天')
    dailyCalorie, days = 3000, 30
    Story.note('他的減重是負的！！（也就是體重持續增加')
    print(getWeightLossEstInfo(bob,
                               act,
                               dailyCalorie,
                               days))

    Story.sectionHead('第一階段減重')
    Story.note('活動力提升一點，少吃一點')
    act = ActivityLevel.MODERATELY_ACTIVE
    dailyCalorie, days = 2500, 30
    print(getWeightLossEstInfo(bob,
                               ActivityLevel.MODERATELY_ACTIVE,
                               dailyCalorie,
                               days))

    Story.sectionHead('第二階段減重')
    Story.note('活動力再提升，吃得更少，持續更久')
    act = ActivityLevel.MODERATELY_ACTIVE
    dailyCalorie, days = 2000, 100
    print(getWeightLossEstInfo(bob,
                               ActivityLevel.VERY_ACTIVE,
                               dailyCalorie,
                               days))

    Story.sectionHead('第三階段減重-- 保持')
    Story.note('先看看目前的體重下，TDEE是多少')
    print(getTDEEEstInfo(bob, act))

    Story.note('活動力再提升，吃得和消耗的差不多，體重就可以維持')
    act = ActivityLevel.MODERATELY_ACTIVE
    bmr = Inbody.estimatedBMR(bob.weight, bob.bodyFat)
    tdee = Inbody.estimatedTDEE(bmr, act)
    dailyCalorie, days = tdee, 100
    print(getWeightLossEstInfo(bob,
                               ActivityLevel.MODERATELY_ACTIVE,
                               dailyCalorie,
                               days))

    # Chapter VII
    Story.chapterHead('發達之路')
    successTech.earnMoney(Currency(100000000))
    successTech.paySalary(bob, Currency(500000))
    successTech.show()
    print(bob.getLifeInfo())
    print(bob.getInbodyInfo())
```

### Story by story code

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> FROM OVERWEIGHT TO OVERACHIVER <<< 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===== CHAPTER 1: ABC 三個好朋友 =====


> Alice, Bob, Charlie 是高中同學的好朋友，他們都用有很不錯的體態。

👤Bob Inbody: 1.72m, 60kg, BMI=20.28, bodyFat=0.15, inbody=體態合宜
👤Bob: 未參加任何群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶
👤Charlie Inbody: 1.8m, 72kg, BMI=22.22, bodyFat=0.15, inbody=體態合宜
👤Charlie: 未參加任何群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶
👤Alice Inbody: 1.65m, 45kg, BMI=16.53, bodyFat=0.12, inbody=過輕
👤Alice: 未參加任何群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶


> 他們成立了 Fit ABC 社團，致力推廣健康觀念

👤Bob: 參與Fit ABC等群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶
👤Charlie: 參與Fit ABC等群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶
👤Alice: 參與Fit ABC等群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶
... 社團的平均 BMI 保持得很好
🎇Fit ABC的成員平均 BMI 為19.68

===== CHAPTER 2: 踏出校園 =====


> 出社會後，大家的體態與工作都有所變化

... Charlie成了教練，在一家健身中心工作
... 他的身高變高，體脂肪和體重還下降了
👤Charlie Inbody: 1.85m, 67kg, BMI=19.58, bodyFat=0.12, inbody=體態合宜
👤Charlie: 參與Fit ABC等群組;在MoveX工作;目前沒有參加健身房;目前沒有銀行帳戶
... Bob 有點宅，也不太不健康
👤Bob Inbody: 1.72m, 80kg, BMI=27.04, bodyFat=0.2, inbody=過重
👤Bob: 參與Fit ABC等群組;目前沒有工作;目前沒有參加健身房;目前沒有銀行帳戶

===== CHAPTER 3: 工作賺錢 =====


> Bob開了銀行帳戶，雖然錢不多

👤Bob存款：💰NTD10,000
... 也把多年的美金存到戶頭
👤Bob存款：💰NTD310,000

> 成功的找到工作

🏢成科股份有限公司是合法登記的公司，目前資產有💰NTD1,000,000
... 薪水 💰NTD50,000
👤Bob: 參與Fit ABC等群組;在成科股份有限公司工作;目前沒有參加健身房;有💰NTD310,000存款
... 公司最近賺了不少錢
👤Bob存款：💰NTD360,000
🏢成科股份有限公司是合法登記的公司，目前資產有💰NTD2,450,000

===== CHAPTER 5: 開始健身 =====

... 健身前的 Inbody！
👤Bob Inbody: 1.72m, 80kg, BMI=27.04, bodyFat=0.2, inbody=過重
... Charlie 轉職到 StrongLife, 擔任 Bob 的教練
Bob 的健身紀錄：
------------
👤Bob於 10/03, 在🏋️‍♂️StrongLife 進行飛輪訓練4次，每次60分鐘。
👤Bob於10/10, 在🏋️‍♂️StrongLife 進行有氧運動訓練1次，每次60分鐘。
👤Bob於10/11, 在🏋️‍♂️StrongLife 進行游泳訓練3次，每次60分鐘。
👤Bob於10/14, 在🏋️‍♂️StrongLife 進行重訓訓練10次，每次60分鐘。
👤Bob於10/20, 在🏋️‍♂️StrongLife 進行瑜伽訓練10次，每次60分鐘。
------------
... 健身後體重降低了！
👤Bob Inbody: 1.72m, 78.54kg, BMI=26.55, bodyFat=0.2, inbody=過重


===== CHAPTER 6: 減重計畫 =====


> 現況評估

... Alice 擔任 Bob 的營養師
... 還沒有減重計劃前 Bob 的狀況
... 他的活動層級被評斷為坐立，這也帶表他每天消耗的熱量很低
依據Bob的體重、體脂肪及活動量(久坐)， 預估BMR基礎代謝🔥1,727大卡; TDEE 每日熱量總耗🔥2,280大卡
... 他每天攝取的熱量大約 3000 大卡，如果這樣持續 30 天
... 他的減重是負的！！（也就是體重持續增加
Bob每天的熱量攝取🔥3000大卡, BMR基礎代謝🔥1,727大卡; 活動習慣:久坐; TDEE 每日熱量總耗🔥2,280大卡
預估30天後減重 -2.7kg
👤Bob Inbody: 1.72m, 81.24kg, BMI=27.46, bodyFat=0.2, inbody=過重

> 第一階段減重

... 活動力提升一點，少吃一點
Bob每天的熱量攝取🔥2500大卡, BMR基礎代謝🔥1,774大卡; 活動習慣:中度活動; TDEE 每日熱量總耗🔥3,024大卡
預估30天後減重 2.1kg
👤Bob Inbody: 1.72m, 79.14kg, BMI=26.75, bodyFat=0.2, inbody=過重

> 第二階段減重

... 活動力再提升，吃得更少，持續更久
Bob每天的熱量攝取🔥2000大卡, BMR基礎代謝🔥1,738大卡; 活動習慣:高度活動; TDEE 每日熱量總耗🔥3,297大卡
預估100天後減重 17.0kg
👤Bob Inbody: 1.72m, 62.14kg, BMI=21.0, bodyFat=0.2, inbody=體態合宜

> 第三階段減重-- 保持

... 先看看目前的體重下，TDEE是多少
依據Bob的體重、體脂肪及活動量(中度活動)， 預估BMR基礎代謝🔥1,444大卡; TDEE 每日熱量總耗🔥2,462大卡
... 活動力再提升，吃得和消耗的差不多，體重就可以維持
Bob每天的熱量攝取🔥2462大卡, BMR基礎代謝🔥1,444大卡; 活動習慣:中度活動; TDEE 每日熱量總耗🔥2,462大卡
預估100天後減重 0.0kg
👤Bob Inbody: 1.72m, 62.14kg, BMI=21.0, bodyFat=0.2, inbody=體態合宜

===== CHAPTER 7: 發達之路 =====

🏢成科股份有限公司是合法登記的公司，目前資產有💰NTD101,949,490
👤Bob: 參與Fit ABC,🏋️‍♂️StrongLife等群組;在成科股份有限公司工作(薪水{self._salary}k);在StrongLife健身;有💰NTD859,400存款
👤Bob Inbody: 1.72m, 62.14kg, BMI=21.0, bodyFat=0.2, inbody=體態合宜
```

## Unit01 Bob, Charlie 和 Alice 

* 一個人 (Person) 有姓名、身高、體重、年齡等資訊
    * name, weight 等稱之為物件的屬性
* 可以透過 person.BMI 來取得其 BMI 的數值
* 可以透過 person.getInbodyInfo() 獲得其健康的狀態
* 學生 (Student) 也是一種人 (Person)，差別在於前者在生成時必須設定其主修
    * Student 是 Person 的延伸類別（或稱之為子類別）
* 可以修改體重，同時要修改 BMI 及健康狀態
    * update() 稱之為方法 (method)，用來提供一個外界與該物件溝通的介面

#### Design
```plantuml
class Person {
    - __init__(name, weight, height, body, bodyFat)
    - name: String
    - weight: int
    - height: float
    - bodyFat: float
    - salary: float
    - age: int
    - {derived} BMI: float
    ---
    + updateInbody(weight, height, bodyFat)
    + getInbodyInfo(): str
    + __str__(): String
}

class Student {
    - major: String
}


Person <|-- Student
```

#### Test code: 
```python
class TestPerson(unittest.TestCase):

    # 個人的 BMI 和健康狀態要正確
    def test_person(self):
        bob = Student('Bob', 1.72, 60, 18, 'Computer')
        charlie = Student('Charlie', 1.80, 70, 18, 'Civil')
        alice = Person('Alice', 1.65, 45, 18)

        self.assertAlmostEqual(bob.getBMI(), 20.25, places=1)
        self.assertEqual(charlie.name, 'Charlie')
        self.assertEqual(alice.getHealthStatus(), Health.TOO_LIGHT)

        # bob 體重增到了 120
        bob.update(weight=120)
        self.assertAlmostEqual(bob.getBMI(), 40.56, places=1)
```    

#### Implementation

* 類別與物件
    * Person 是類別; nick 是物件
* 封裝
    * name, weight, height 被封裝在 Person 中
* 公開方法
    * `getBMI() 提供服務; 身高體重則隱藏不公開
* Python 
    * `__str__()` 是一個魔術方法 (magic 方法); 當呼叫 `print()` 時，就會引用此方法。
    * `__init__()` 是物件的建構子
    * `self` 表示物件本身，只要引用物件內部的屬性和方法，就必須加上 `self`


## Unit02 FitABC 社團

* 人可以加入一個群體，例如社團、公司或是健身房
* 此設定主要是要計算群組健康指標
* 可以查詢一個群組符合某個健康狀態的人有哪些，作為後續健康追蹤的目的

#### Design

```plantuml
abstract class HGroup {
    - title: String
    - people: list(Person)
    ---
    + avgBMI(): float
    + queryByInbody(Inbody): list(Person)
    + add(Person)
    + getMembers(): Person
    + {abstract} show()
}

HGroup "0..*" o-->"0..*" Person
HGroup <|-- Gym
Company <|-- Gym
HGroup <|-- HighSchoolClub

```

#### Test
```python
class TestGroup(unittest.TestCase):

    def setUp(self):
        self.bob = Student('Bob', 1.72, 60, 18, 'Computer')
        self.charlie = Student('Charlie', 1.80, 70, 18, 'Civil')
        self.alice = Person('Alice', 1.65, 45, 18)

        # 社團
        self.fit = HighShoolClub('Fit ABC')

    # 群組：加入一群人後，群體 bmi 要正確
    def test_group_health(self):
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        self.assertAlmostEqual(self.fit.avgBMI(), 19.45, 1)

    # 群組：找出一個群組中，健康的人、過重的、過輕的
    def test_get_healthy_people(self):
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        self.assertEqual(self.fit.getHealthList(
            Health.FIT), {self.bob, self.charlie})
        self.assertEqual(self.fit.getHealthList(
            Health.TOO_LIGHT), {self.alice})
        self.assertEqual(self.fit.getHealthList(Health.OVER_WEIGHTED), None)

    # 展示不同的群組有不同的描述方法 (desc)
    def test_show_group_desc(self):
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        google = Company('Google', asset=100)
        groups = [self.fit, google]

        print('\n==== Group description ====')
        for g in groups:
            g.desc()
```

群組：找出一個群組中，健康的人、過重的、過輕的

```python
    def test_get_healthy_people(self):
        bob = Student(name='Bob', height=1.72, weight=60, age=18,
                      major='Computer')
        charlie = Student('Charlie', 1.80, 70, 18, 'Civil')
        alice = Person('Alice', 1.65, 45, 18)
        fit_friend = Group('Fit ABC')
        fit_friend.add(bob)
        fit_friend.add(charlie)
        fit_friend.add(alice)

        self.assertEqual(fit_friend.getHealthList(Health.FIT), {bob, charlie})
        self.assertEqual(fit_friend.getHealthList(Health.TOO_LIGHT), {alice})
        self.assertEqual(fit_friend.getHealthList(Health.OVER_WEIGHTED), None)
```        
## Unit03 錢幣與匯兌

* 錢幣應該包含數量與幣值
* 錢幣可以相加，相減，比較，即便是不同的幣值

#### Design

```plantuml
class Currency {
    - amount: float
    - symbol: string
    - convert()
    + __add__()
    + __sub__()
    + __le__()
    + __ge__()    
}
```

#### Test


```python
    # 測試錢幣的處理，臺幣和臺幣
    def test_currency(self):
        ntd120 = Currency(120)
        self.assertEqual(ntd120.amount, 120)
        self.assertEqual(ntd120.symbol, 'NTD')

        ntd100 = Currency(100, 'NTD')
        r = ntd120+ntd100
        self.assertEqual(r.amount, 220)
        self.assertEqual(r.symbol, 'NTD')

        r = ntd120-ntd100
        self.assertEqual(r.amount, 20)
        self.assertEqual(r.symbol, 'NTD')

        self.assertTrue(ntd120 >= ntd100)
        self.assertFalse(ntd100 >= ntd120)

    # 台幣與美金的運算
    def test_currency_convert(self):
        ntd120 = Currency(120)
        us100 = Currency(100, 'USD')
        self.assertEqual(Currency.NTD_RATE, 30)
        sum = ntd120 + us100
        self.assertEqual(sum.amount, 120+100*Currency.NTD_RATE)
        self.assertEqual(sum.symbol, 'NTD')

        diff = us100 - ntd120
        self.assertEqual(diff.amount, 100 - 120/Currency.NTD_RATE, 2)
        self.assertEqual(diff.symbol, 'USD')

        self.assertTrue(us100 >= ntd120)
        self.assertFalse(ntd120 >= us100)
```

#### Implementation

* Company 建立時必須有資產，所以建構子需要加上資產 assert 的參數
* 錢幣是一個類別，因為他必須封裝金額與幣值
* 角色是一個子類別嗎？Worker 是一個類別抑或是 Person 中添加一個 role 的屬性？
* Currency 的魔術方法：`__add__()` 與 `__sub__()`  分別代表 `+`, `-`

## Unit04 Bob 的存款

* 銀行帳戶可以儲存與領出錢幣，必須要有申請者的姓名
* 只支援台幣帳戶，如果指明是美金的話，會通過匯率的轉換存入/提出
* 銀行帳戶可以查詢餘款
* 如果提款金額大於餘款，要拋出例外，且餘款不變

#### Design

```plantuml
class BankAccount {
    - title_: str
    - balance: Currency
    + deposit(Currency)
    + withdraw(Currency)
}

class Person {
    - bankAccount: BankAccount
    + getBalance(): Currency
}


Person "1" *-> "*" BankAccount: own
BankAccount -> Person: belongs to
BankAccount o--> Currency
```

#### Test

```python
class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        # bob
        self.bob = Person('Bob', 1.72, 100, 40)
        self.bob_bAccount = BankAccount(self.bob.name, balance = Currency(10000))
        self.bob.setBankAccount(self.bob_bAccount)

    def test_deposit_ntd(self):
        self.bob_bAccount.deposit(Currency(10000))        # 存入台幣 10000
        self.assertEqual(self.bob.getBalance(), Currency(20000))

    def test_deposit_usd(self):
        self.bob_bAccount.deposit(Currency(100, "USD"))   # 存入美金
        newB = 10000 + 100 * Currency.NTD_RATE
        self.assertEqual(self.bob.getBalance(), Currency(newB))

    def test_withdraw_usd(self):
        self.bob_bAccount.withdraw(Currency(100, "USD"))  # 領出美金
        newB = 10000 - 100 * Currency.NTD_RATE
        self.assertEqual(self.bob.getBalance(), Currency(newB))

    def test_withdraw_insufficient(self):
        with self.assertRaises(Exception) as e:
            self.bob_bAccount.withdraw(Currency(12000))
        self.assertTrue(
            'Insufficient funds in the account' in str(e.exception))
        self.assertEqual(self.bob_bAccount.getBalance(), Currency(10000))  # 餘款不變
```

## Unit05 公司與健身房

* 公司有名稱與資產
* 公司有營收，會因此增加資產
* 當員工加入公司，公司付薪水給員工時，員工的銀行帳戶會增加餘額，公司資產會減少
* 健身房也是一間公司，必須設定會員費
* 當會員加入健身房後，該會員的帳戶餘額會減少，健身房資產增加

#### Design

```plantuml
class Company {
    - _title
    + asset: Currency
    + paySalary(Person, Currency)
    + hire(Person)
    + earnMoney(Currency)    
}
class Person {
    + registerGym(Gym)
}
class Gym extends HGroup
class Gym extends Company

class Gym {
    - memberFee: Currency
    + isMember()
    + add(Person)
}

Person -> Gym: register
Person ..> Exception: No enough funds
```

#### Test


```python
class TestCompanyGym(unittest.TestCase):

    def setUp(self):
        # successTech
        self.successTech = Company('Success Tech.', Currency(100000))

        # bob
        self.bob = Person('Bob', 1.72, 100, 40)
        self.bob_bAccount = BankAccount(self.bob.name, balance = Currency(10000))
        self.bob.setBankAccount(self.bob_bAccount)

        # gym
        self.strongLife = Gym('Strong Life', Currency(100000), Currency(1000))
                
    def test_company_earnMoney(self):
        self.successTech.earnMoney(Currency(100000))
        self.assertEqual(self.successTech.getAsset(), Currency(200000))

    def test_paySalary(self):
        self.bob.workFor(self.successTech)
        self.successTech.paySalary(self.bob, Currency(50000, symbol='NTD'))

        self.assertEqual(self.successTech.getAsset(), Currency(50000))
        self.assertEqual(self.bob.getBalance(), Currency(60000))

    # 加入健身房: 健身房資產增加，會員帳戶餘額減少
    def test_register_gym(self):
        self.bob.registerGym(self.strongLife)
        self.assertEqual(self.bob.getBalance(), Currency(10000-1000))
        self.assertTrue(self.strongLife.getAsset() == Currency(100000+1000))

    def test_is_gym_member(self):
        ''' he/she should be a member '''    
        self.bob.registerGym(self.strongLife)
        self.assertTrue(self.strongLife.isMember(self.bob))
```

## Unit06 補助健身費用

* 公司補助員工健身
* 只有公司職員才能接受補助
* 補助後員工的帳戶餘額會增加，公司資本減少

#### Design

```plantuml
abstract class HGroup {
    + addMember(People)
    + avgBMI(): float
    + queryByInbody(Inbody)
}
class Gym {
    - memberFee: Currency
}
class Person {
    + register(Gym)
}
class Company {
    + subsidize(Person, amount):
}

class BankAcount {
    + deposit(Currency)
    + withdraw(Currency)
}
HGroup <|-- Gym
Company -> Person: subsidize
Person -> Gym: join
Person -> BankAcount: own
Person ..> Exception: raise
```

#### Test

```python
class TestCompanySupport(unittest.TestCase):
    # 補助：只有員工才能補助; 補助後公司資產減少，員工帳戶增加

    def setUp(self) -> None:
        # successTech
        self.successTech = Company('Success Tech.', Currency(100000))

        # bob
        self.bob = Person('Bob', 1.72, 100, 40)
        self.bob_bAccount = BankAccount(self.bob.name, balance = Currency(10000))
        self.bob.setBankAccount(self.bob_bAccount)

        # gym
        self.strongLife = Gym('Strong Life', Currency(100000), Currency(1000))

    def test_subsidize_balance_asset(self):
        self.bob.workFor(self.successTech)
        self.successTech.subsidize(self.bob, Currency(500))
        # 受補助的錢會變多
        self.assertEqual(self.bob.getBalance(), Currency(10000+500))        
        # 公司資產錢會變少
        self.assertEqual(self.successTech.getAsset(), Currency(100000-500))

    def test_subsidize_employee_only(self):
        # annie 不是員工
        annie = Person('Annie', 1.62, 55)
        with self.assertRaises(Exception) as e:
            self.successTech.subsidize(annie, Currency(500))

```

## Unit07 Charlie 健身教練

* 健身教練相較於一般的人，其健康標準較嚴格: 對於 BMI 的標準越高 (19-22)，也包含體脂肪的檢查 (<=0.15)
* 每個健身教練都一個主修

#### Design

```plantuml
abstract class HGroup {
    + __init__(title)
    + avgBMI()
    + {abstract} desc(): String
}

class HighSchoolClub {
    + desc(): String
}

class Company {
    + desc(): String
}


HGroup <|-- HighSchoolClub
```

#### Test

```python
    def test_coach(self):
        nick = Person('Nick', 1.72, 70)
        self.assertEqual(nick.getHealthStatus(), Health.FIT)     # BMI: 23.66

        charlie = Person('Charlie', 1.72, 70, bodyFat=0.2)       # BMI: 23.66
        charlie = Coach(charlie, '舉重')
        self.assertEqual(charlie.getHealthStatus(), Health.OVER_WEIGHTED)

        # BMI: 20.28 ok but high body fat
        charlie.update(weight=60, bodyFat=0.25)
        self.assertEqual(charlie.getHealthStatus(), Health.OVER_BODY_FAT)

        charlie.update(weight=60, bodyFat=0.14)
        self.assertEqual(charlie.getHealthStatus(), Health.FIT)
```

## Unit08 健身減重

* 不同的運動項目的 MET 不同，所謂的 MET 是指人類在活動時相對於靜止不動的消耗量，MET 越高表示期消耗的熱量約高，其減重效果越高。
*  消耗的熱量與體重、運動項目及時程有關 (=該運動 MET * 體重 * 小時數)
*  每消耗 7700 大卡，約可減重 1kg

#### Design

```plantuml
class Workout {
    - name 
    + {static} calBurned()
    + {static} weightLoss()
}

Enum <|-- Workout
```

#### Test


```python
def test_workout(self):
        # swim 運動消耗熱量, 並減重
        swim = Workout.SWIM
        cal = swim.caloriesBurn(weight=100, duration=60)
        print (f'{swim.value[0]}一小時約耗{cal}大卡')
        self.assertEqual(cal, swim.value[1]*100*60/60)

        loss = swim.weightLoss(100, 60, 30)
        print (f'每天{swim.value[0]}一小時，一個月可以減重{loss}kg')
        self.assertEqual(3.9, loss)

        # bob 到健身房游泳
        bob = Person(name='Bob', height=1.72, weight=100, age=40)
        bob_bAccount = BankAccount(bob.name, balance=Currency(0))
        bob.setBankAccount(bob_bAccount)
        bob.registerGym(Gym('StrongLife', Currency(0)))
        bob.workOut(swim, 60, '2023/10/10', 30)
        self.assertEqual(bob.weight, 100-loss)
```

## Unit09 健身歷程

#### Design

```plantuml
Person o->"1" ExerciseLog
ExerciseLog o->"*" ExerciseRec

class ExerciseRec {
    - ex: Exercise
    - person: Person
    - duration: min
    - date: Date
    - caloryBurn: float
    - weightLost: float
}

class Person {
    - exerciseLog: list(ExerciseRec) 
    + workout(Workout, durationMins, date, durationDays)
    + showExLog()
}
```

#### Test

```python
    # 健身：記錄健身
    def test_workout_rec(self):
        # bob 到健身房游泳
        bob = Person(name='Bob', height=1.72, weight=100, age=40)
        bob_bAccount = BankAccount(bob.name, balance=Currency(0))
        bob.setBankAccount(bob_bAccount)
        bob.registerGym(Gym('StrongLife', Currency(0)))
        bob.workOut(Workout.FLYWHEEL, 60, '2023/10/03', 4)
        bob.workOut(Workout.AEROBIC_EX, 60, '2023/10/10', 1)
        bob.workOut(Workout.SWIM, 60, '2023/10/11', 3)
        bob.workOut(Workout.WEIGHT_TRAIN, 60, '2023/10/14', 10)
        bob.workOut(Workout.YOGA, 60, '2023/10/20', 10)
        bob.showWorkoutLog()
```

## Unit10 Alice 的減重計畫

* 當我們攝取的熱量(Calorie intake)比消耗的熱量(TDEE)來得低，其差就是熱量赤字, 每7700 大卡約可減重1kg。
* 每日消耗熱量與代謝率 (BMR) 及運動誘發熱能 (TEA) 及食物誘發熱能 (TEF) 有關
  * BMR 可由體重、體脂肪估算出來
  * TEA 可以由 BMR, 活動程度估算出來
  * TEF 可由 BMR, TEA 估算出來
* 估算出 TDEE 後，我們可以擬定飲食計畫，每天吃比 TDEE 少約 500大卡的熱量，日子久了就會減重

```python
    @unittest.skip('done')
    # 測試 BMR, TDEE, 與減輕之重量
    def test_BMR(self):
        weight, bodyFat = 90, 0.2
        bmr = Health.estimatedBMR(weight, bodyFat)
        print('BMR: ', bmr)

        tdee = Health.estimateTDEE(bmr, ActivityLevel.LIGHTLY_ACTIVE)
        dailyCalorie = tdee - 400
        weightLoss = Health.estimatedWeightLoss(tdee, dailyCalorie, 30)
        print('Weight loss: ', weightLoss)

        bmr = Health.estimatedBMR(weight-weightLoss, 0.2)
        tdee = Health.estimateTDEE(bmr, ActivityLevel.VERY_ACTIVE)
        weightLoss = Health.estimatedWeightLoss(tdee, dailyCalorie, 30)
        print('Weight loss: ', weightLoss)

        bmr = Health.estimatedBMR(weight-weightLoss, 0.2)
        tdee = Health.estimateTDEE(bmr, ActivityLevel.VERY_ACTIVE)
        weightLoss = Health.estimatedWeightLoss(tdee, dailyCalorie+100, 30)
        print('Weight loss: ', weightLoss)

    # @unittest.skip('done')
    # 測試 BMR, TDEE, 與減輕之重量
    def test_bob(self):
        # 一開始的 bob, 沒有運動, 吃的也多
        bob = Person(name='Bob', height=1.72, weight=120, age=40, bodyFat=0.3)
        bob_bmr = Health.estimatedBMR(bob.weight, bob.bodyFat)
        bob_activity = ActivityLevel.SEDENTARY
        bob_tdee = Health.estimateTDEE(bob_bmr, bob_activity)
        dailyCalorie = 4000
        weightLoss = Health.estimatedWeightLoss(bob_tdee, dailyCalorie, 30)
        print(
            f'\nbob 重{bob.weight}, 平常{bob_activity}, 每日消耗熱量{bob_tdee}, 攝取熱量{dailyCalorie}, 30天後，體重減少{weightLoss}kg')

        bob.update(weight=bob.weight - weightLoss)

        # 第一個月運動
        bob_bmr = Health.estimatedBMR(bob.weight, bob.bodyFat)
        bob_activity = ActivityLevel.VERY_ACTIVE
        bob_tdee = Health.estimateTDEE(bob_bmr, bob_activity)
        dailyCalorie = bob_tdee - 500
        weightLoss = Health.estimatedWeightLoss(bob_tdee, dailyCalorie, 30)
        print(
            f'\nbob 重{bob.weight}, 平常{bob_activity}, 每日消耗熱量{bob_tdee}, 攝取熱量{dailyCalorie}, 30天後，體重減少{weightLoss}kg')

        bob.update(weight=bob.weight - weightLoss)

        # 第二個月運動、飲食控制
        bob_bmr = Health.estimatedBMR(bob.weight, bob.bodyFat)
        bob_activity = ActivityLevel.SUPER_ACTIVE
        bob_tdee = Health.estimateTDEE(bob_bmr, bob_activity)
        dailyCalorie = bob_tdee - 1500
        weightLoss = Health.estimatedWeightLoss(bob_tdee, dailyCalorie, 30)
        print(
            f'\nbob 重{bob.weight}, 平常{bob_activity}, 每日消耗熱量{bob_tdee}, 攝取熱量{dailyCalorie}, 30天後，體重減少{weightLoss}kg')
        bob.update(weight=bob.weight - weightLoss)

        # 第三個月運動、飲食控制
        bob_bmr = Health.estimatedBMR(bob.weight, bob.bodyFat)
        bob_activity = ActivityLevel.SUPER_ACTIVE
        bob_tdee = Health.estimateTDEE(bob_bmr, bob_activity)
        dailyCalorie = bob_tdee - 2500
        weightLoss = Health.estimatedWeightLoss(bob_tdee, dailyCalorie, 30)
        print(
            f'\nbob 重{bob.weight}, 平常{bob_activity}, 每日消耗熱量{bob_tdee}, 攝取熱量{dailyCalorie}, 30天後，體重減少{weightLoss}kg')
        bob.update(weight=bob.weight - weightLoss)

        while bob.weight > 70:
            bob_bmr = Health.estimatedBMR(bob.weight, bob.bodyFat)
            bob_activity = ActivityLevel.SUPER_ACTIVE
            bob_tdee = Health.estimateTDEE(bob_bmr, bob_activity)
            dailyCalorie = bob_tdee - 2500
            weightLoss = Health.estimatedWeightLoss(bob_tdee, dailyCalorie, 30)
            print(
                f'\nbob 重{bob.weight}, 平常{bob_activity}, 每日消耗熱量{bob_tdee}, 攝取熱量{dailyCalorie}, 30天後，體重減少{weightLoss}kg')
            bob.update(weight=bob.weight - weightLoss)
```

## All design

```plantuml

class Person {
    - name
    - height
    - weight
    
    + getBMI()
    + getHealthStatus()
    + workFor(Company)
    + join(Gym)
    + exercise()
    + showExLog()
}

class Currency

class BankAccount

Person o-> BankAccount
BankAccount ..> Currency

ExerciseRec o--> Exercise

class Exercise

class ExerciseRec {
    - Exercise
    - duration
    - date
}

Person ---> Exercise: do

GeneralStu --|> Person
AtheleteStu --|> Person

class AtheleteStu {
    - major
}

class Group {
    + showHealthStatus()
}

class Worker {
    - salary
    + workFor (Company)
}

Worker -> Company: work for

class Worker extends Person 

class Company extends Group {
    - asset
    + earnMoney(Currency)
    + offerSudside(Worker)
}

class Gym extends Company

class Gym {
    - fee
}

Person -> Gym: join
Person o->"1" ExerciseLog
ExerciseLog o->"*" ExerciseRec
```

## Class design (docstring)


#### CLASS Person
```

 封裝一個人的資訊。

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
    
-- Methods --

	.updateInbody(): 更新身高質量，包含身高體重體脂肪。更新後，也會重新計算 BMI 及 inbody 的狀態。
        

	._setInbody(): 設定 inbody, 太輕、太重或是健康 

	.getInbodyInfo(): 回傳細部的身體指數，包含身高體重, BMI, 體脂肪率及 inbody 的狀態 

	.join(): 參與一個社群; 同時會呼叫 group.add() 成為雙邊關係 

	.workFor(): 加入公司工作; 同時會呼叫 company.hire() 建立雙邊關係 

	.getBalance(): 回傳所連結的銀行帳戶的餘款 

	.getBalanceInfo(): 回傳帳務資訊的字串 

	.showBalance(): 印出姓名與帳戶存款 

	.registerGym(): 報名健身房; 同時呼叫 gym.add() 建立雙邊關係 

	.workout(): 健身後可以減重，進而變更 BMI, 同時產生健身紀錄

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
        

	.getLifeInfo(): 回傳此人的一般生活資訊, 包含參與的社團，公司，健身房與帳戶存款 

	.showWorkoutLog(): 印出此人的健身紀錄 

```

#### CLASS Currency
```

 封裝金額與幣值，提供錢幣的處理 

    Attributes
      - amount: 金額
      - symbol: 貨幣
    
-- Methods --

	._convert(): 匯率的轉換，目前僅支援台幣美金的轉換 

```

#### CLASS BankAccount
```

銀行帳戶

    Attributes:
    ----------
    title: str 
        開戶者的名稱
    balance : Currency
        存款
    
-- Methods --

	.deposit(): 存款 

	.withdraw(): 提款 

```

#### CLASS Student
```

 Student 有一個主額外的資訊：主修科目，其餘與 Person 同 
```

#### CLASS HGroup
```

抽象的健康群組
    
    HGroup (Health Group) 是一個抽象的類別, 
    封裝一個重視健康的群組應有的功能，
    包含回傳一個群體的平均 BMI, 以了解群組的健康度
    包含可以查詢回傳某一個健康狀態（例如過重）的子群
    
-- Methods --

	.add(): 將某人加入此群組，會同時呼叫 person.add 建立雙邊關係 

	.isMember(): 回傳是否為會員 

	.avgBMI(): 回傳此群組的平均 BMI 

	.getBmiAvgInfo(): 回傳此群組的平均 BMI 的字串訊息 

	.getMembers(): 回傳此群組的所有成員所形成的字串，以 , 連結 

	.queryByInbody(): 回傳符合某一健康狀態 (inbody) 的所有人所形成的 list
        Parameters:
            status : Inbody
                過重, 過輕或體態合宜

        Return: list
            滿足所有 status 狀態的人    

        Exception: 查無此體態
        

	.show(): 抽象方法，不同群體的目的不同，所以描述的方式也不同 
        
        印出群組的描述。
        

```

#### CLASS HighShoolClub
```

 高中社團是一種 HGroup，所以必須實踐 show()

    Attributes
        school : str 
            校名
    
-- Methods --

	.setSchool(): 設定此社團所屬的高中校名 

	.show():None

```

#### CLASS Company
```

 公司有公司名稱、資產及員工等屬性。

    Attributes
        title : str
            公司名稱
        asset : Currency
            公司資產    
    
-- Methods --

	.paySalary(): 付薪水，該員工的戶頭會增加錢，公司的資本減少 

        Parameter
            employee(People): 受薪的員工
            currency(Currency): 薪水
        Return
            None
        Exception
            - 發薪給未僱用的人                        
            - 受薪者還沒有設定帳戶
        

	.earnMoney(): 公司營收，資本增加 

	.hire(): 雇用員工

        employee 的 list 會加入此 person
        要先檢查是否已經聘用了, 因為可能透過員工.workFor() 加入公司
        

	.isHired(): 回傳是否已經受聘於此公司 

	.subsidize(): 補助員工參與健身等活動 

        - 補助前先檢查是否為公司員工
        - 錢會直接匯到該員工的帳戶
        - 公司的資產會因此減少

        Exception:
            受補助的人並不是公司員工
        

	.show():None

```

#### CLASS Gym
```

健身房

    - 健身房是一個公司，也是一個提倡健康的群組。
    - 多重繼承 Company 與 HGroup 
    
-- Methods --

	.add(): 加入群組

        覆蓋 HGroup.add() 的功能：加入會員須要扣款，健身房資本增加，會員帳戶餘款減少 
        

	.getGymInfo(): 回傳健身房基本資訊，包含資產與會費

	.show(): 印出會員數量，描述健身房狀態

```

#### CLASS Coach
```

 Coach 是一個 Person, 有額外的健身專長，對體檢的標準也不同 
    Attributes
        expertise : str
            教練的專長
    
-- Methods --

	._setInbody(): 覆蓋 person 中設定 inbody 的值，因為教練的健康要求比較高 

        Exception
            必須設定體脂肪，才能設定 inbody; 若無，會拋出例外
        

```

#### CLASS WorkoutRec
```

 封裝一筆健身紀錄，包含人事時地物
        
    - 什麼人進行的健身 (person)
    - 進行什麼重訓 (workout)
    - 什麼時間 (date)
    - 在哪一個健身房 (gym)
    - 一次進行了多久 (duration)
    - 進行了多少次 (times)
    
```
  
