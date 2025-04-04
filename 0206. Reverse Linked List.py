def reverse_list(head):
    if head != None and head.next != None:
        if head.next.next != None:
            a1 = head
            a2 = head.next
            a3 = head.next.next
            a1.next = None

            while a3.next != None:
                a2.next = a1
                a1 = a2
                a2 = a3
                a3 = a3.next

            a2.next = a1
            a3.next = a2
            head = a3
        else:
            head.next.next = head
            head = head.next
            head.next.next = None

    return head