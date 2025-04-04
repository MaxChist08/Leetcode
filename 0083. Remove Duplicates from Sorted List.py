def delete_duplicates(head):
    not_real_head = head

    if head != None:
        while not_real_head.next != None:
            if not_real_head.val == not_real_head.next.val:
                not_real_head.next = not_real_head.next.next
            else:
                not_real_head = not_real_head.next

    return head