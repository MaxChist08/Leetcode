def remove_elements(head, val):
    not_real_head = head

    if head != None:
        while not_real_head != None and not_real_head.val == val:
            head = not_real_head.next
            not_real_head = head

        while not_real_head != None and not_real_head.next != None:
            if not_real_head.next.val == val:
                not_real_head.next = not_real_head.next.next
            else:
                not_real_head = not_real_head.next

    return head 