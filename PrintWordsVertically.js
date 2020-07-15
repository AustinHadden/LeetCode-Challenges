/**
 * @param {string} s
 * @return {string[]}
 */
var printVertically = function(s) {
    const arr = s.split(' ')
    const maxLength = Math.max(...arr.map(word => word.length))
    
    return [...Array(maxLength)].map((_, i) => arr.map(word => word[i] || ' ').join('').trimEnd())
};