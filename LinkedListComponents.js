/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number[]} G
 * @return {number}
 */
var numComponents = function(head, G) {
    if(!head) return null;
    let GSet = new Set(G);  
    let ret = 0, series = 0;
    while(head) {
      series = GSet.has(head.val) ? series + 1 : 0;
      if(series == 1)
        ret += 1;
      head = head.next;
    }
    return ret;
  };