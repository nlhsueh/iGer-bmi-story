from enum import Enum


class Workout(Enum):
    YOGA = ('瑜伽', 3)  # 名稱、運動強度 (MET)
    SWIM = ('游泳', 10)
    FLYWHEEL = ('飛輪', 9)
    WEIGHT_TRAIN = ('重訓', 4)
    AEROBIC_EX = ('有氧運動', 6)

    def __init__(self, name, met):
        self._name = name
        self._met = met

    def caloriesBurn(self, weight, duration):
        '''
        @param weight: 體重，單位公斤
        @param duration: 時長，單位分鐘
        @return 大卡
        '''
        return round(self._met * weight * duration / 60, 1)

    def weightLoss(self, weight, duration, times):
        ' 每7700 大卡約降 1kg '
        caloriesBurn = round(self.caloriesBurn(weight, duration*times), 3)
        return (round(caloriesBurn/7700, 2))

    def __str__(self):
        return self._name


' 與 Workout 不同, ActivityLevel 指的是生活型態'


class ActivityLevel(Enum):
    SEDENTARY = 1           # 久坐（辦公室工作，少運動）
    LIGHTLY_ACTIVE = 2      # 輕度活動（輕度運動或步行）
    MODERATELY_ACTIVE = 3   # 中度活動（中度運動或運動幾次）
    VERY_ACTIVE = 4         # 高度活動（每天劇烈運動）
    SUPER_ACTIVE = 5        # 超級活動（極高的運動水平）

    def __str__(self):
        actMap = {1: '久坐',
                  2: '輕度活動',
                  3: '中度活動',
                  4: '高度活動',
                  5: '超級活動'}

        return actMap[self.value]


' 身體指數 '


class Inbody(Enum):
    OVER_WEIGHTED = '過重'
    TOO_LIGHT = '過輕'
    FIT = '體態合宜'
    OVER_BODY_FAT = '體脂肪過高'

    @staticmethod
    def bmi(height, weight):
<<<<<<< HEAD
        return round(weight/(height*height), 2)
=======
        return round(weight/(height*height), 2)

    @staticmethod
    def estimatedBMR(weight, bodyFat):
        ''' 
        @param weight: 體重 單位公斤
        @param bodyFat: 體脂肪率，例如 0.2
        @rtype float: 預估的 BMR 基礎代謝
        Katch-McArdle 依據體重和體脂肪率算出 BMR 基礎代謝 basal metabolic rate
        BMR就是身體需要的最低熱量
        BMR = 370 + (21.6 * Lean Body Mass [kg])
        LBM = (Weight [kg] * (100 - Body Fat %) / 100
        '''
        LBM = weight * (1-bodyFat)
        BMR = round(370 + (21.6 * LBM), 1)
        return BMR

    @staticmethod
    def estimatedTDEE(BMR, activityLevel):
        ''' 
        @param BMR: basal metabolic rate 基礎代謝

        TDEE (Total Daily Energy Expenditure; 每日熱量總耗)  = BMR + TEA + TEF
        - TEA thermic effect of activity 運動誘發熱能
        - TEF thermic effect of food 食物誘發熱能 (消化食物所消耗的熱能)
        '''
        activityMultipliers = {
            ActivityLevel.SEDENTARY: 0.2,
            ActivityLevel.LIGHTLY_ACTIVE: 0.375,
            ActivityLevel.MODERATELY_ACTIVE: 0.55,
            ActivityLevel.VERY_ACTIVE: 0.725,
            ActivityLevel.SUPER_ACTIVE: 0.9
        }

        if activityLevel in activityMultipliers:
            TEA = BMR * activityMultipliers[activityLevel]
        else:
            return "Invalid activity level input."

        TEF = (BMR + TEA) * 0.1  # 估算
        TDEE = BMR + TEA + TEF
        return round(TDEE)

    def estimatedWeightLoss(TDEE, DCI, nDays):
        ''' 
        @param TDEE (Total Daily Energy Expenditure 每日熱量總耗)
        @param DCI daily calorie intake 每日熱量攝取
        @param nDays 天數

        Calorie deficit (CD) 熱量赤字 = TDEE - DCI
        estimated weight loss = CD / 7700 # calorie deficit 每 7700 大卡可以降低 1kg
        '''
        CD = TDEE - DCI
        estimatedWeightLoss = round(CD/7700, 2) * nDays
        return round(estimatedWeightLoss, 1)
>>>>>>> u10_plan
