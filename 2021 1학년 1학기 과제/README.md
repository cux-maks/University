# 과제

###### 2021 1학년 1학기 컴퓨팅사고 과제 모음


## 과제 1
#### 문제1. 입력받은 변수 x와 y의 값을 서로 바꾸는 프로그램을 작성하시오.

```python
#변수 x와 y 입력
x = int(input("x = "))
y = int(input("y = "))

#변수 x와 y 값 바꾸기
num = x
x = y
y = num

#바뀐 값 출력하기
print("x = ", x)
print("y = ", y)
```

#### 문제2. ![<me1.png>](https://github.com/cux-maks/B_HA/blob/main/2021%201%ED%95%99%EB%85%84%201%ED%95%99%EA%B8%B0%20%EA%B3%BC%EC%A0%9C/me1.png) 에서 x = 3일 때, 함수의 값을 계산하시오.

```python
#값 계산
num1 = 3*3*3 #첫 번째 항 계산
num2 = 3*3*3 #두 번째 항 계산
num3 = 7*3 #세 번째 항 계산
num4 = 10 #네 번째 항 계산

#최종 결과값
print(num1+num2+num3+num4)
```
