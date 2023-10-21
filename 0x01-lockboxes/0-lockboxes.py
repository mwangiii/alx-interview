#!/usr/bin/python3
def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""
    if not boxes:
        return False

    num_of_boxes = len(boxes)
    # will return false
    visited = num_of_boxes * [False]
    visited[0] = True
    # stack should have value
    stack = [0]

    # while loop to make sure it iterates in all boxes
    while stack:
        # pop removes the last element in the array and returns it
        current_box = stack.pop()

        for key in boxes[current_box]:
            # if key is not greater than number of boxes
            # if key is not less than 0 ju first box is open
            # if the box is not open - open the box and set it to true
            if key >= 0 and key < num_of_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
