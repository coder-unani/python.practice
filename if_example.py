'''
학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.

이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.

A: 90점 이상
B: 80점 이상 90점 미만
C: 70점 이상 80점 미만
D: 60점 이상 70점 미만
F: 60점 미만
print_grade() 함수는 파라미터로 중간고사 점수 midterm_score와 기말고사 점수 final_score를 받아서 최종 성적을 출력합니다.
'''
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")

'''
while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.

예를 들어서 16은 8의 배수이지만 12의 배수가 아니니까 조건에 부합합니다. 하지만 48은 8의 배수이면서 12의 배수이기도 해서 조건에 부합하지 않습니다.
'''
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1

'''
10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.

while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 코드를 작성해 보세요.
'''
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)

'''
약수는 정수 n을 어떤 수로 나누었을 때 나누어떨어지게 하는 정수를 의미합니다. 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 됩니다.

정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 코드를 작성해 보세요.
'''
N = 120
i = 1
count = 0

while i <= N:
    if N % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개입니다.".format(N, count))

'''
1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만 원을 받았습니다.

이 돈을 어떻게 할지 고민하던 택이는, 이웃인 동일 아저씨와 미란 아주머니의 의견 중 하나를 선택하려 합니다.

동일 아저씨 의견
> 원금에 붙은 이자에 다시 이자가 붙는 연복리 예금에 넣기


 <연복리 예금 상품 정보>

 원금: 50,000,000 원
 연 이율: 12%
 1년 뒤 은행 잔고: 50,000,000 * (1 + 12%) = 56,000,000 원
 2년 뒤 은행 잔고: 50,000,000 * (1 + 12%) * (1 + 12%) = 62,720,000 원
 ...
미란 아주머니 의견
> 아파트 가치 상승을 고려하여 당시 매매가 5000만 원인 은마 아파트 사기

2016년 기준 은마아파트의 매매가는 11억 원인데요. 1988년 은행에 5,000만 원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,

은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.를 출력하고
은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다.를 출력하는 코드를 작성해 보세요.
'''
# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000

# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))

'''
피보나치 수열(Fibonacci Sequence)이라고 들어 보셨나요?

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다. 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다. 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며, 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.

피보나치 수열의 첫 50개 항을 차례대로 출력하는 코드를 작성해 보세요.
'''
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    previous, current = current, current + previous
    i += 1

# or
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1

'''
구구단을 출력하세요
'''
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print("{} * {} = {}".format(i, j, i * j))
        j += 1
    i += 1