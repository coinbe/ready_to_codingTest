# 소수

1보다 큰 자연수 중 1과 자기자신으로만 나누어 떨어지는 수

python

```py
def is_prime_number(n):
  # 2부터 n-1까지 수로 나누어 가면서 확인하자
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

print(is_prime_number(121))
print(is_prime_number(32))
```

javascript

```js
function primecheck(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) return false;
  }
  return true;
}

primecheck(123);
```
