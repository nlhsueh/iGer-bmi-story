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