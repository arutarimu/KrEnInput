# Introduction 
Korean written language called "한글" (Hangul) is a composition of two to three individual characters.  
"Hello" in Korean is "안녕", and you can clearly see there are three components to each characteristic.  
"안 -> ㅇㅏㄴ" and "녕 -> ㄴㅕㅇ"  
* I will use First, Middle, and Final characters to identify the three characters.  
(Check : https://en.wikipedia.org/wiki/Hangul for better terms and information.)  


Let's go back to "안녕" to demonstrate.  
안녕's 안 is made up of First : ㅇ Middle :ㅏ Final : ㄴ, and each characters can be typed with one keystroke.  
* Note that not every characteristic uses the Final character, like "가" using only First and Middle.  

Because Korean keyboard layout is essentially just an overlay on the English QWERTY keyboard, it is easy to convert.  
*for example*: 안녕 -> dkssud
  
![Image](https://i.imgur.com/FxWXp4N.png)

# KrEnInput
KrEnInput utilizes Korean encoding methods to break down each characteristics into individual characters.  
After decomposing the characteristic, it uses a dictionary to convert the characters into English letters.  

# Special Thanks 
* This program uses neotune's list of Korean First, Middle, Final characters. https://github.com/neotune  
* Hamlet from AHK Forums https://autohotkey.com/board/topic/97036-korean-support/#entry611177

# License
You are more than welcome to use, modify, and share.

# 한글 README
python3를 이용하여 한글을 분해하고 영타로 변환하는 소스입니다.    
예 : 안녕 -> dkssud  
neotune님의 초성, 중성, 종성 리스트와 소스를 바탕으로 만들어졌습니다. https://github.com/neotune
