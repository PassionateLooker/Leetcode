# # 21. Merge Two Sorted Lists
# #
# # Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
# #
# # Example:
# #
# # Input: 1->2->4, 1->3->4
# # Output: 1->1->2->3->4->4
#
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
#
# class Solution:
#     def mergeTwoLists(self, l1, l2) -> ListNode:
#         temp = dummy = ListNode(0)
#         if (l1 is None):
#             return l2
#         if (l2 is None):
#             return l1
#         while (l1 and l2):
#             if (l1.val < l2.val):
#                 temp.next = l1
#                 l1 = l1.next
#             else:
#                 temp.next = l2
#                 l2 = l2.next
#             temp = temp.next
#         if (l1):
#             temp.next = l1
#         if (l2):
#             temp.next = l2
#         return dummy.next
#
# # -----------OR-----------------
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def mergeTwoLists(self, l1, l2) :
#         head =ListNode(0)
#         ptr =head
#         while True:
#             if l1 is None and l2 is None:
#                 break
#             elif l1 is None:
#                 ptr.next =l2
#                 break
#             elif l2 is None:
#                 ptr.next =l1
#                 break
#             else:
#                 smallerVal =0
#                 if l1.val <l2.val:
#                     smallerVal =l1.val
#                     l1 =l1.next
#                 else:
#
#                     smallerVal =l2.val
#                     l2 =l2.next
#                 newNode =ListNode(smallerVal)
#                 ptr.next =newNode
#                 ptr =ptr.next
#         return head.next
#
# s=Solution()
# ll='''
# [1,2,4]
# [1,3,4]
# '''
# print(s.mergeTwoLists(ll))
#
#
mylist = ["a", "b", "a", "c", "c"]
print(type(len(set(mylist))))