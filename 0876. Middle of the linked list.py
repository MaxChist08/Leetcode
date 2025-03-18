def middle_node(head):
    x = head
    x1 = head
    while x1.next and x1.next.next:
        x = x.next
        x1 = x1.next.next
    if x1.next:
        return x.next
    else:
        return x