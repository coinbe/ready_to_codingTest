# 개념적 알고리즘
def is_prime_number(m):
  for i in range(2, m):
    if m % i == 0:
      return False
  return True

print(is_prime_number(121)) # False
print(is_prime_number(32)) # False

# 단점 : 모든 수를 계산해봐야 하기 때문에 효율이 떨어진다 => O(n)


# 약수를 이용한 알고리즘 
import math

def is_prime_number2(n):
  for i in range(2, int(math.sqrt(n)) + 1): # sqrt() : 제곱근
    if n % i == 0:
      return False
  return True

print(is_prime_number2(17)) # True
print(is_prime_number2(33)) # False

"""
약수가 짝을 짓는 것을 활용한다 => O(n^1/2)
ex) 16이 소수인지 판단해보자
    16의 약수 = 1, 2, 4, 8, 16 (소수, 1과 자기자신만을 약수로 가져야한다)
    (1, 16), (2, 8), (4, 4), (8, 2), (16, 1)로 짝을 짓는다 => 가운데 값을 기준으로 반만 비교하면 된다
    => 2 ~ 4까지만 나누어 보면 된다 
"""



