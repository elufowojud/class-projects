def fun_modified(x):
    n = len(x)
    y = ""
    i = 0

    # Use one loop to iterate through the string
    while i < n:
        char = x[i]
        z = 1

        # Count consecutive occurrences of the same character
        while i + z < n and x[i + z] == char:
            z += 1

        y += char  # Add the character to y
        if z > 1:
            y += str(z)  # Add the count if greater than 1

        i += z  # Move to the next group of characters

    return y
