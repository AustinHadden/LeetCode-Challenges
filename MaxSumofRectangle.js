/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var maxSumSubmatrix = function(m, k) {
    let max = -Infinity;
    const rows = m.length, cols = m[0].length;
    const sums = Array(rows);
    for (let c1 = 0; c1 < cols; c1++) {
      sums.fill(0);
      for (let c2 = c1; c2 < cols; c2++) {
        for (let row = 0; row < rows; row++) {
          sums[row] += m[row][c2];
        }
        for (let i = 0; i < rows; i++) {
          let sum = 0;
          for (let j = i; j < rows; j++) {
            sum += sums[j];
            if (sum > max && sum <= k) {
              max = sum;
            }
          }
        }
      }
    }
    return max;
  };