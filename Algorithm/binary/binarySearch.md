# 이진탐색

정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘

## 특징

---

1. 데이터가 정렬된 상태여야 한다
2. 가운데 값과 찾고자하는 값을 비교하여 두 부분으로 나누어 검색한다
3. 시간복잡도 : O(log2N)

---

### python

```py
def binary_search(data, search):
  data.sort()
  if len(data) == 1 and search == data[0]:
    return True

  if len(data) == 1 and search != data[0]:
    return False

  if len(data) == 0:
    return False

  mid = len(data) // 2
  if search == data[mid]:
    return True

  else:
    if search > data[mid]:
      return binary_search(data[mid:], search)
    else:
      return binary_search(data[:mid], search)
```

### javascript

```js
const sorted = (arr) => {
  return arr.sort((a, b) => a - b); // 오름차순정렬
};

const binarySearch = function (arr, search) {
  let mid = Math.floor(arr.length / 2);

  if (!arr.length) return false; // 배열의 길이가 0이면

  if (arr[mid] == search) {
    return true;
  }
  if (arr[mid] > search) {
    return binarySearch(arr.slice(0, mid), search);
  } else return binarySearch(arr.slice(mid + 1), search);
};
```
