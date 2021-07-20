def remove_duplicates_from_linked_list(linked_list):
    current_node = linked_list
    while current_node is not None:
        next_node = current_node.next
        # as long as next_node is not None, traverse until we find the next distinct value
        while next_node is not None and next_node.value == current_node.value:
            # same value, move on
            next_node = next_node.next
        
        # found the node with distinct value
        # update the linked list connection
        current_node.next = next_node
        current_node = next_node
    return linked_list
