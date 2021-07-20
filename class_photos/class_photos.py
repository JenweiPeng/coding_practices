# sort both arrays
# find the "indicator" by A[0] - B[0]
# since each student in the back must be strictly taller, that means we need to return False if the indicator is equal to 0
# otherwise, iterate through both arrays, and check if the "trend" ever changes
# the different at i index between the two arrays should always be greater than zero or smaller than zero
def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()
    indicator = red_shirt_heights[0] - blue_shirt)heights[0]

    if indicator == 0:
        # same height
        return False

    for idx in range(1, len(red_shirt_heights)):
        if (red_shirt_heights[idx] - blue_shirt_heights[idx]) * indicator <= 0:
            # same height or the trend changed
            return False
    return True
