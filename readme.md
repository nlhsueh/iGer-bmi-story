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

### Story by story code

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> FROM OVERWEIGHT TO OVERACHIVER <<< 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



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