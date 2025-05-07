def swap_pairs(head):
    element = None

    if head is not None and head.next is not None:
        elem = head.next
        if head.next.next is not None:
            element = head
        head.next = elem.next
        elem.next = head
        head = elem

    while element is not None and element.next is not None and element.next.next is not None:
        elem = element.next
        element.next = element.next.next
        elem.next = element.next.next
        element.next.next = elem
        element = element.next.next

    return head