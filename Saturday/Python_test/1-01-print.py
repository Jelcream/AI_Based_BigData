# print() 함수 : 출력
# 파일명: 1-01-print.py

my_string = " 머신러닝기반 '빅데티터 분석' 파이썬 "

print('''문자열
연습
입니다''')

print("""문자열
연습
입니다""")
print("\n")

print(my_string)
print("\n")

print("안녕하세요? 제이름은","파이썬이고",20,"살 입니다")
print("안녕하세요? 제이름은" + "파이썬이고",20,"살 입니다")
print("\n")

print("안녕하세요? 제이름은\n", "\"파이썬\" 입니다.", "C:\\aaa\\bbb\\")
print("\n")

line = "=" * 50
print(line)
print("\n")

message = "Hi Have great day!"
print(message * 3)
print("\n")

price = 10000
print("상품의 가격은 %s원 입니다" %price)  # , 구분자 없음
