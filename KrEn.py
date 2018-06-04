import re

""" 
    Author : Alex Kim (Arta)
    Date of modification : 06.04.2018
    Description : These lines of code convert Korean characteristics into English QWERTY Key strokes.
    
    How Korean characteristics are encoded is this : 
        Korean Unicode = ((First Character * 21) + Middle Character * 28 + Final Character + 0xAC00
    By using the equation above, we can sort out '안녕', as 'ㅇㅏㄴㄴㅕㅇ'.
    And because the Korean keyboard layout is just an overlay on top of the English QWERTY keyboard layout, 
    we can easily map out which Korean characters corresponds to which English letters.
             
"""

# 초성 중성 종성 리스트는 neotune 님의 코드에서 가져왔습니다. https://github.com/neotune
# The list of First, Middle, and Final character lists were imported from neotune. https://github.com/neotune

FIRST_CHAR = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ",
              "ㅍ", "ㅎ"]
MID_CHAR = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ",
            "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
FINAL_CHAR = [" ", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ",
              "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
KR_EN_DICTIONARY = {'ㅂ': 'q', 'ㅈ': 'w', 'ㄷ': 'e', 'ㄱ': 'r', 'ㅅ': 't', 'ㅛ': 'y', 'ㅕ': 'u', 'ㅑ': 'i', 'ㅐ': 'o',
                    'ㅔ': 'p', 'ㅁ': 'a', 'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j', 'ㅏ': 'k',
                    'ㅣ': 'l', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v', 'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm', 'ㅃ': 'Q',
                    'ㅉ': 'W', 'ㄸ': 'E', 'ㄲ': 'R', 'ㅆ': 'T', 'ㅒ': 'O', 'ㅖ': 'P', 'ㅘ': 'hk', 'ㅙ': 'ho', 'ㅚ': 'hl',
                    'ㅝ': 'nj', 'ㅞ': 'np', 'ㅟ': 'nl', 'ㅢ': 'ml', 'ㄳ': 'rt', 'ㄵ': 'sw', 'ㄶ': 'sg', 'ㄺ': 'fr',
                    'ㄻ': 'fa', 'ㄼ': 'fq', 'ㄽ': 'ft', 'ㄾ': 'fx', 'ㄿ': 'fv', 'ㅀ': 'fg', 'ㅄ': 'qt'}


def decompose(korean):  # this is a method to break down each characteristic as individual characters.
    word_list = list(korean)
    result = []
    for word in word_list:   # iterate through each characteristic
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]', word):   # regex to make sure the characteristic is in Korean.
            char = ord(word) - 44032   # Korean unicode starts from 44032.
            first = int(char / 588)
            result.append(FIRST_CHAR[first])
            mid = int((char - (first * 588)) / 28)
            result.append(MID_CHAR[mid])
            final = int((char - (first * 588) - (mid * 28)))
            if FINAL_CHAR[final] == " ":   # the final character doesn't have to exist, and if doesn't exist, skip.
                pass
            else:
                result.append(FINAL_CHAR[final])
        else:
            result.append(word)
    return result   # keeping the result in a list data structure helps to convert into English letters much easier.


def convert(word_list):   # a simple conversion algorithm using dictionary.
    result = ""
    for i in word_list:
        if i in KR_EN_DICTIONARY:
            result += (KR_EN_DICTIONARY[i])
        else:
            result += i
    return result


if __name__ == '__main__':
    user_input = input("Please enter Korean to convert to English equivalent keystrokes. \n")
    print("".join(convert(decompose(user_input))))
