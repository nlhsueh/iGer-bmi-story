import unittest
from bmiStory import *
from healthUtil import *


class TestPerson(unittest.TestCase):

    def test_inbody(self):
        bob = Student('Bob', 1.72, 60, 0.13, 'Computer')
        charlie = Student('Charlie', 1.80, 70, 0.15, 'Civil')
        alice = Person('Alice', 1.65, 45, 0.12)

        people = [bob, charlie, alice]
        for p in people:
            self.assertTrue(p.weight < 200 and p.weight > 30)
            self.assertTrue(p.height < 2.2)
            self.assertTrue(p.bodyFat < 1)
            self.assertTrue(p.BMI < 50 and p.BMI > 10)

        self.assertEqual(charlie.name, 'Charlie')
        self.assertAlmostEqual(bob.BMI, 20.25, places=1)
        self.assertEqual(alice.inbody, Inbody.TOO_LIGHT)

        # bob 體重增到了 120
        bob.updateInbody(weight=120)
        self.assertAlmostEqual(bob.BMI, 40.56, places=1)


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.bob = Student('Bob', 1.72, 60, 0.13, 'Computer')
        self.charlie = Student('Charlie', 1.80, 70, 0.15, 'Civil')
        self.alice = Person('Alice', 1.65, 45, 0.12)

        # 社團
        self.fit = HighShoolClub('Fit ABC')

    def test_group_bmi(self):
        ' 加入一群人後，群體 bmi 要正確 '
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        self.assertAlmostEqual(self.fit.avgBMI(), 19.45, 1)

    def test_query_by_inbody(self):
        ' 找出一個群組中，健康的人、過重的、過輕的 '
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        self.assertEqual(self.fit.queryByInbody(
            Inbody.FIT), {self.bob, self.charlie})
        self.assertEqual(self.fit.queryByInbody(
            Inbody.TOO_LIGHT), {self.alice})
        self.assertEqual(self.fit.queryByInbody(Inbody.OVER_WEIGHTED), None)

    def test_show_group_show(self):
        ' 展示不同的群組有不同的描述方法 (desc) '
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        google = Company('Google', asset=100)
        groups = [self.fit, google]

        print('\n==== Group description ====')
        for g in groups:
            g.show()

    def test_add(self):
        self.fit.add(self.bob)
        # print("***", self.fit.getMembers())
        self.assertTrue(self.fit._members == [self.bob])
        # self.assertEqual(self.bob._groups, [self.fit])


' 測試錢幣的處理：加減、比較 '


class TestCurrency(unittest.TestCase):
    def test_currency(self):
        ntd120 = Currency(120)
        self.assertEqual(ntd120.amount, 120)
        self.assertEqual(ntd120.symbol, 'NTD')

        ntd100 = Currency(100, 'NTD')
        r = ntd120 + ntd100
        self.assertEqual(r.amount, 220)
        self.assertEqual(r.symbol, 'NTD')

        r = ntd120 - ntd100
        self.assertEqual(r.amount, 20)
        self.assertEqual(r.symbol, 'NTD')

        self.assertTrue(ntd120 >= ntd100)
        self.assertFalse(ntd100 >= ntd120)

    def test_currency_convert(self):
        ' 台幣與美金的運算 '
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


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        # bob
        self.bob = Person('Bob', 1.72, 100, 0.2, 40)
        self.bob_bAccount = BankAccount(self.bob.name, balance=Currency(10000))
        self.bob.bankAccount = self.bob_bAccount

    def test_currency(self):
        x = Currency(100)
        if x is None:
            print(x)

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
            '餘額不足' in str(e.exception))
        self.assertEqual(self.bob_bAccount.balance, Currency(10000))  # 餘款不變


class TestCompanyGym(unittest.TestCase):

    def setUp(self):
        self.asset = Currency(100000)
        self.balance = Currency(10000)
        self.gym_asset = Currency(100000)
        self.fee = Currency(500)

        # successTech
        self.successTech = Company('Success Tech.', self.asset)

        # bob
        self.bob = Person('Bob', 1.72, 100, 0.2, 40)
        self.bob_bAccount = BankAccount(self.bob.name, self.balance)
        self.bob.bankAccount = self.bob_bAccount

        # gym
        self.strongLife = Gym('Strong Life', self.gym_asset, self.fee)

    def test_company_earnMoney(self):
        self.successTech.earnMoney(Currency(100000))
        self.assertEqual(self.successTech.asset, self.asset + Currency(100000))

    def test_paySalary(self):
        salary = Currency(50000)
        self.bob.workFor(self.successTech)
        self.successTech.paySalary(self.bob, salary)

        self.assertEqual(self.successTech.asset, self.asset - salary)
        self.assertEqual(self.bob.getBalance(), self.balance + salary)

    # 加入健身房: 健身房資產增加，會員帳戶餘額減少
    # @unittest.skip
    def test_register_gym(self):
        self.bob.registerGym(self.strongLife)
        self.assertTrue(self.bob.getBalance() == (self.balance - self.fee))

        self.assertTrue(self.strongLife.asset == self.fee + self.gym_asset)

    def test_is_gym_member(self):
        ''' he/she should be a member '''
        self.bob.registerGym(self.strongLife)
        self.assertTrue(self.strongLife.isMember(self.bob))

    # @unittest.skip
    def test_update_memberfee(self):
        self.strongLife.memberFee = Currency(600)
        self.assertEqual(self.strongLife.memberFee, Currency(600))

        # 調價太高，會產生例外
        with self.assertRaises(Exception) as e:
            self.strongLife.memberFee(Currency(1600))

    # @unittest.skip
    def test_register_gym_implies_join(self):
        ''' if a person register a gym, 
            it imples it join the gym group
        '''
        bmi = self.bob.BMI
        self.bob.registerGym(self.strongLife)
        self.assertEqual(self.strongLife.avgBMI(), bmi)
        print(self.bob.getInbodyInfo())


class TestCompanySupport(unittest.TestCase):
    # 補助：只有員工才能補助; 補助後公司資產減少，員工帳戶增加

    def setUp(self) -> None:
        # successTech
        self.successTech = Company('Success Tech.', Currency(100000))

        # bob
        self.bob = Person('Bob', 1.72, 100, 0.2, 40)
        self.bob_bAccount = BankAccount(self.bob.name, balance=Currency(10000))
        self.bob.bankAccount = self.bob_bAccount

        # gym
        self.strongLife = Gym('Strong Life', Currency(100000), Currency(1000))

    def test_subsidize_balance_asset(self):
        self.bob.workFor(self.successTech)
        self.successTech.subsidize(self.bob, Currency(500))
        # 受補助的錢會變多
        self.assertEqual(self.bob.getBalance(), Currency(10000+500))
        # 公司資產錢會變少
        self.assertEqual(self.successTech.asset, Currency(100000-500))

    def test_subsidize_employee_only(self):
        # annie 不是員工
        annie = Person('Annie', 1.62, 55)
        with self.assertRaises(Exception) as e:
            self.successTech.subsidize(annie, Currency(500))


class TestCoach(unittest.TestCase):
    # 教練：教練的健康標準比較高

    def setUp(self) -> None:
        self.nick = Person('Nick', 1.72, 70)
        self.charlie = Person('Charlie', 1.72, 70, bodyFat=0.1)    # BMI: 23.66
        self.charlie = Coach(self.charlie, '舉重')     # charlie is a Coach

    def test_coach_same_inbody(self):
        self.assertEqual(self.nick.inbody, Inbody.FIT)  # BMI: 23.66
        self.assertEqual(self.charlie.inbody, Inbody.OVER_WEIGHTED)

    def test_bodyFat(self):
        ''' low BMI, but high body fat
            BMI: 20.28 ok but high body fat'''

        self.charlie.updateInbody(weight=60, bodyFat=0.25)
        self.assertEqual(self.charlie.inbody, Inbody.OVER_BODY_FAT)

    def test_fit(self):
        ''' a fit coach '''
        self.charlie.updateInbody(weight=60, bodyFat=0.15)
        self.assertEqual(self.charlie.inbody, Inbody.FIT)

    # @unittest.skip
    def test_original_attr(self):
        ''' if a person have other attribute (like group) 
            we should add back these attribute to coach
        '''
        annie = Person('Annie', 1.6, 45, 0.13)
        account = BankAccount('Annie', Currency(10000))
        annie.bankAccount = account
        annie = Coach(annie, 'running')
        print(annie.getLifeInfo())
        self.assertEqual(annie.getBalance(), Currency(10000))

# @unittest.skip


class TestWorkout(unittest.TestCase):

    def setUp(self) -> None:
        # swim
        self.swim = Workout.SWIM

        # bob
        self.bob = Person('Bob', 1.72, 100, 0.2, 40)
        self.bob_bAccount = BankAccount(self.bob.name, balance=Currency(0))
        self.bob.bankAccount = self.bob_bAccount
        self.bob.registerGym(Gym('StrongLife', Currency(0)))

    # 健身：健身後體重減輕，bmi 下降
    def test_Workout_swim(self):
        cal = self.swim.caloriesBurn(weight=100, duration=60)
        loss = self.swim.weightLoss(100, 60, 30)

        self.assertEqual(cal, self.swim.value[1]*100*60/60)
        self.assertEqual(loss, 3.9)

        # bob 到健身房游泳
        self.bob.workout(self.swim, 60, '2023/10/10', 30)
        self.assertEqual(self.bob.weight, 100-loss)

# @unittest.skip


class TestWorkoutRec(unittest.TestCase):
    # 健身：記錄健身
    def test_Workout_rec(self):
        # bob 到健身房游泳
        bob = Person(name='Bob', height=1.72, weight=100, age=40)
        bob_bAccount = BankAccount(bob.name, balance=Currency(0))
        bob.bankAccount = bob_bAccount
        bob.registerGym(Gym('StrongLife', Currency(0)))
        bob.workout(Workout.FLYWHEEL, 60, '2023/10/03', 4)
        bob.workout(Workout.AEROBIC_EX, 60, '2023/10/10', 1)
        bob.workout(Workout.SWIM, 60, '2023/10/11', 3)
        bob.workout(Workout.WEIGHT_TRAIN, 60, '2023/10/14', 10)
        bob.workout(Workout.YOGA, 60, '2023/10/20', 10)
        bob.showWorkoutLog()

# @unittest.skip


class TestWeightLossPlan(unittest.TestCase):

    def test_BMR(self):
        ' 測試 BMR 是否正確 '
        weight, bodyFat = 90, 0.2
        bmr = Inbody.estimatedBMR(weight, bodyFat)

        self.assertAlmostEqual(bmr, 1925.2, places=1)

    def test_weight_loss_SEDENTARY(self):
        ' 測試 預估減輕的重量是否正確 '
        weight, bodyFat = 90, 0.2
        act = ActivityLevel.SEDENTARY
        dailyCalorie, days = 3000, 30

        bmr = Inbody.estimatedBMR(weight, bodyFat)
        tdee = Inbody.estimatedTDEE(bmr, act)
        weightLoss = Inbody.estimatedWeightLoss(tdee, dailyCalorie, days)
        self.assertEqual(-1.8, weightLoss)

    def test_weight_loss_MODERATELY_ACTIVE(self):
        weight, bodyFat = 90, 0.2
        act = ActivityLevel.MODERATELY_ACTIVE
        dailyCalorie, days = 3000, 30

        bmr = Inbody.estimatedBMR(weight, bodyFat)
        tdee = Inbody.estimatedTDEE(bmr, act)
        weightLoss = Inbody.estimatedWeightLoss(tdee, dailyCalorie, days)
        self.assertEqual(1.2, weightLoss)

    def test_weight_loss_SUPER_ACTIVE(self):
        weight, bodyFat = 90, 0.2
        act = ActivityLevel.SUPER_ACTIVE
        dailyCalorie, days = 3000, 30

        bmr = Inbody.estimatedBMR(weight, bodyFat)
        tdee = Inbody.estimatedTDEE(bmr, act)
        weightLoss = Inbody.estimatedWeightLoss(tdee, dailyCalorie, days)
        self.assertEqual(3.9, weightLoss)

    # @unittest.skip('done')
    # 測試 BMR, TDEE, 與減輕之重量
    def test_show_bob_plan(self):
        # 一開始的 bob, 沒有運動, 吃的也多
        bob = Person(name='Bob', height=1.72, weight=120, age=40, bodyFat=0.3)

        # 可以採用(1) 固定熱量赤字的方式來減重，或是(2) 增加運動強度、固定攝取熱量的方式
        # activity level, dificit, daily_cal, days
        actPlan = [(ActivityLevel.SEDENTARY, 500, '-', 30),           # 熱量赤字 500
                   (ActivityLevel.LIGHTLY_ACTIVE, 500, '-', 30),      # 熱量赤字 500
                   (ActivityLevel.LIGHTLY_ACTIVE, '-', 2000, 30),     # 攝取熱量 2000
                   (ActivityLevel.MODERATELY_ACTIVE, '-', 3000, 30),  # 攝取熱量 3000
                   (ActivityLevel.VERY_ACTIVE, '-', 3000, 30),        # 攝取熱量 3000
                   (ActivityLevel.SUPER_ACTIVE, '-', 3000, 30),       # 攝取熱量 3000
                   ]

        print("\n=================")
        print(f"{bob.name}的減重歷程")
        print("=================")
        for act in actPlan:
            actLevel = act[0]
            dificit = act[1]
            dailyCalorie = act[2]
            days = act[3]

            bob_bmr = Inbody.estimatedBMR(bob.weight, bob.bodyFat)
            bob_tdee = Inbody.estimatedTDEE(bob_bmr, actLevel)
            if dificit != '-':
                dailyCalorie = bob_tdee - dificit
            weightLoss = Inbody.estimatedWeightLoss(
                bob_tdee, dailyCalorie, days)
            print(
                f'bob重{bob.weight:.1f}, {actLevel}, 預估每日消耗熱量{bob_tdee}, 如果每日攝取熱量{dailyCalorie}, {days}天後，預計體重減少{weightLoss}kg')

            bob.updateInbody(weight=bob.weight - weightLoss)
            # print (f'新體重：{bob.weight:.1f}')


if __name__ == '__main__':
    unittest.main()
