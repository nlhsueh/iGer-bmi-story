from enum import Enum

' 身體指數 '
class Inbody(Enum):
    OVER_WEIGHTED = '過重'
    TOO_LIGHT = '過輕'
    FIT = '體態合宜'
    OVER_BODY_FAT = '體脂肪過高'

    @staticmethod
    def bmi(height, weight):
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