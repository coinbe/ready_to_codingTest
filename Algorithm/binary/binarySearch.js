// 이진탐색

data_list = [11, 2, 54, 23, 33, 12, 6];

const sorted = (arr) => {
  return arr.sort((a, b) => a - b); // 오름차순정렬
};

const binarySearch = function (arr, search) {
  
  while(mid == search)
    let mid = Math.floor(arr.length / 2);

    if (!arr.length) return false; // 배열의 길이가 0이면

    if (arr[mid] == search) {
      return true;
    }
    if (arr[mid] > search) {
      return binarySearch(arr.slice(0, mid), search);
    } else return binarySearch(arr.slice(mid + 1), search);
};

console.log(binarySearch(sorted(data_list), 23)); // true
console.log(binarySearch(sorted(data_list), 87)); // false
