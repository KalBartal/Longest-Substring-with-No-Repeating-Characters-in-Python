def max_len(s):
    pointerA = 0
    pointerB = 1
    maxLen = 0

    # loop through string
    for i in range(len(s)):
        # declare variables
        if s[pointerA] != s[pointerB]: # check if characters are the same
            pointerB += 1
        else:
            pointerA = 0
            pointerB = i + 1

            maxLen = max(maxLen, pointerB - pointerA) # check if maxLen should be updated

        # return maxLength value
    return maxLen
