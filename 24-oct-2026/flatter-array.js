
// Problem : https://leetcode.com/problems/flatten-deeply-nested-array/
// Difficulty Medium : solved by my self yeahhhh

var flat = function (arr, n) {
   return flattenArray(arr, n)
};

function flattenArray(arr, n, currentLevel = 0) {
     if (n == 0 || currentLevel == n){
        return arr
    }
    ans = []
    let i = 0;
    while (i < arr.length ) {
        if (arr[i] instanceof Array) {
            ans = [...ans, ...flattenArray(arr[i], n, currentLevel + 1)]
        } else {
            ans.push(arr[i])
        }
        i+= 1
    }
    return ans
}

data = [1,2,3,[4,5,6],[7,8,[9,10,11],12],[13,14,15]]

console.log(flat(data, 1))