
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
