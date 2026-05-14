"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.

Reference: https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Iterator, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        def _merge_sorted(node1: Optional[ListNode], node2: Optional[ListNode]):
            while node1 and node2:
                if node1.val <= node2.val:
                    yield node1
                    node1 = node1.next
                else:
                    yield node2
                    node2 = node2.next
            while node1:
                yield node1
                node1 = node1.next
            while node2:
                yield node2
                node2 = node2.next

        merging_nodes: Iterator[ListNode] = _merge_sorted(list1, list2)
        new_head: ListNode = next(merging_nodes)

        last: ListNode = new_head
        for node in merging_nodes:
            last.next = node
            last = node
        last.next = None

        return new_head


def test_solution():
    solution = Solution()
    
    # Test case 1: Both lists have elements
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = solution.mergeTwoLists(list1, list2)
    assert merged.val == 1
    assert merged.next.val == 1
    assert merged.next.next.val == 2
    assert merged.next.next.next.val == 3
    assert merged.next.next.next.next.val == 4
    assert merged.next.next.next.next.next.val == 4
    assert merged.next.next.next.next.next.next is None
    
    # Test case 2: One list is empty
    list1 = None
    list2 = ListNode(0)
    merged = solution.mergeTwoLists(list1, list2)
    assert merged.val == 0
    assert merged.next is None
    
    # Test case 3: Both lists are empty
    list1 = None
    list2 = None
    merged = solution.mergeTwoLists(list1, list2)
    assert merged is None


if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
