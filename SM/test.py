test = "Hello World"
print(test)

fruits = ('100','200', '300', 'grape', 'apple', 'watermellon')
kk = 1,2,3,4,5
print(fruits)
print(fruits[1])
print(kk[1])


dt = {'교수':"반기철", '지역':"전주", '기간':5}
dt1 = {'학교':"한국대학교", "교육내용":"DSACM1", "종목":'python'}
dt2= {'grade':4, "결과":"매우만족", "휴대전화":'010-4506-1007'}



print(dt1['학교'])

print(dt1['교육내용'])

print("korea" == "korea")
print("korea" != "korea")
print("Korea" > "korea")
print("Korea" <"korea")

#len() 문자열의 길이
#min() 아스키코드값이 가장 큰 문자 소문자 -> 대문자 -> 스페이스 순
#max() 아스키코드값이 가장 작은 문자
#sum() 문자열에는 적용 불가
#sorted() 문자열의 아스키코드값으로 정렬하여 결과를 리스트로 반환
#reversed() 문자열을 역순으로 바꿈 반드시 리스트 함수를 적용해야함

# 문자열 메소드메소드: 문자열에만 적용가능한 함수 - 출력문자 대/소문자 변환하기
# .capitalize() 첫 문자 대문자
# .title() 단어의 첫글자를 대문자
# .upper()
# .lower()
# .swapcase() 문자열 전체 대문자 -> 소문자, 소문자 -> 대문자

# .center() 가운데로 이동 공백 ??로 채우기
# .ljust() 왼쪽으로 정렬 공백 ??로 채우기
# .rjust() 오른쪽으로 정렬 공백 ??로 채우기
price = 10000
age = int(input("나이를 입력하세요: "))
if age >= 65 or age< 8:
    price =0
elif age>=20:
    price=500
else:
    price= 300

print(age, ' ',price)

score = int(input("당신의 국어 성적을 입력하세요: "))
score += int(input("당신의 수학 성적을 입력하세요: "))
score += int(input("당신의 영어 성적을 입력하세요: "))

score /= 3
print(score)
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("See you next year")


