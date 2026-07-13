# PCCE 대비 연습문제 (Python)

실제 PCCE 시험은 빈칸 채우기, 디버깅, 코드 작성 유형으로 총 10문항이 출제됩니다. 아래 문제도 동일한 3가지 유형으로 구성했습니다. 언어는 Python 기준입니다.

---

## 1번. [빈칸 채우기] 출력

다음 코드는 정수 `a`, `b`를 입력받아 두 수의 합, 차, 곱을 순서대로 출력합니다. 빈칸을 채우세요.

```python
a, b = map(int, input().split())

print(a + b)
print(______)
print(______)
```

**입력**: `7 3`
**출력**:
```
10
4
21
```

---

## 2번. [디버깅] 조건문

다음 코드는 정수 `n`이 짝수면 "짝수", 홀수면 "홀수"를 출력해야 합니다. 코드에 오류가 있습니다. 잘못된 부분을 찾아 고치세요.

```python
n = int(input())

if n % 2 == 1:
    print("짝수")
else:
    print("홀수")
```

**입력**: `4`
**기대 출력**: `짝수`

---

## 3번. [코드 작성] 반복문

1부터 `n`까지의 정수 중 3의 배수의 합을 구해 출력하는 코드를 작성하세요.

**입력**: `n = 10`
**출력**: `18` (3+6+9)

```python
n = int(input())

# 여기에 코드 작성

```

---

## 4번. [빈칸 채우기] 리스트

리스트 `numbers`에서 최댓값과 최솟값의 차이를 출력하는 코드입니다. 빈칸을 채우세요.

```python
numbers = [4, 8, 15, 16, 23, 42]

biggest = ______(numbers)
smallest = ______(numbers)

print(biggest - smallest)
```

**출력**: `38`

---

## 5번. [디버깅] 문자열

다음 코드는 문자열 `word`를 거꾸로 뒤집어 출력해야 합니다. 오류를 찾아 고치세요.

```python
word = "programmers"
reversed_word = word[0:-1]
print(reversed_word)
```

**기대 출력**: `sremmargorp`

---

## 6번. [코드 작성] 함수

두 정수를 입력받아 더 큰 값을 반환하는 함수 `get_max(a, b)`를 작성하고, 이를 이용해 세 정수 중 최댓값을 출력하는 코드를 작성하세요.

**입력**: `5 9 2`
**출력**: `9`

```python
def get_max(a, b):
    # 여기에 코드 작성

a, b, c = map(int, input().split())
# get_max를 활용해 최댓값 출력
```

---

## 7번. [빈칸 채우기] 2차원 리스트

3x3 리스트에서 대각선 원소들의 합을 구하는 코드입니다. 빈칸을 채우세요.

```python
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0
for i in range(3):
    total += board[i][______]

print(total)
```

**출력**: `15` (1+5+9)

---

## 8번. [코드 작성] 딕셔너리

학생 이름과 점수가 담긴 딕셔너리에서 점수가 80점 이상인 학생의 이름만 리스트로 출력하는 코드를 작성하세요.

```python
scores = {"민수": 85, "지은": 72, "하늘": 91, "서준": 68}

# 여기에 코드 작성

```

**출력**: `['민수', '하늘']`

---

## 9번. [디버깅] 조건문 + 반복문

다음 코드는 1부터 20까지의 수 중 소수(prime number)를 모두 출력해야 하는데, 오류가 있어 일부 소수가 아닌 값도 출력됩니다. 오류를 찾아 고치세요.

```python
for n in range(1, 21):
    is_prime = True
    for i in range(1, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(n, end=" ")
```

**기대 출력**: `2 3 5 7 11 13 17 19`

---

## 10번. [코드 작성] 종합 (데이터 처리)

여러 학생의 국어, 영어, 수학 점수가 2차원 리스트로 주어집니다. 각 학생의 평균 점수를 구해, 평균이 가장 높은 학생의 번호(0부터 시작)와 그 평균을 출력하는 코드를 작성하세요.

```python
students = [
    [80, 90, 70],
    [95, 85, 100],
    [60, 75, 65]
]

# 여기에 코드 작성

```

**출력**:
```
1번 학생
평균: 93.33
```

---
---

# 정답 및 해설

**1번**
```python
print(a - b)
print(a * b)
```

**2번**
`if n % 2 == 1:` → `if n % 2 == 0:` 으로 수정 (짝수 판별 조건이 반대로 되어 있었음)

**3번**
```python
total = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        total += i
print(total)
```

**4번**
```python
biggest = max(numbers)
smallest = min(numbers)
```

**5번**
`word[0:-1]`은 마지막 글자를 뺀 부분 문자열입니다. 뒤집으려면 `word[::-1]`로 수정해야 합니다.

**6번**
```python
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

a, b, c = map(int, input().split())
print(get_max(get_max(a, b), c))
```

**7번**
대각선 원소는 `board[i][i]`이므로 빈칸은 `i`

**8번**
```python
result = [name for name, score in scores.items() if score >= 80]
print(result)
```

**9번**
`range(1, n)`이 1부터 시작해 1로 나눈 나머지가 항상 0이 되어 모든 수가 소수가 아닌 것으로 잘못 처리됩니다(또한 n=1도 소수로 판정되는 문제 있음). `range(2, n)`으로 수정하고, `n`이 1일 때는 처음부터 제외하도록 `if n < 2: continue`를 추가해야 합니다.

```python
for n in range(1, 21):
    if n < 2:
        continue
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(n, end=" ")
```

**10번**
```python
averages = [sum(s) / len(s) for s in students]
best = averages.index(max(averages))
print(f"{best}번 학생")
print(f"평균: {round(max(averages), 2)}")
```