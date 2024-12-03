def fun(x):
    # Step 1: Initialize variables
    n = len(x)
    y = ""  # Result string
    i = 0  # Index variable

    # Step 2: While loop to iterate through the string
    while i < n:
        y += x[i]  # Add the current character to y
        z = 1  # Counter for consecutive characters

        # Step 3: For loop to count consecutive characters
        for j in range(i + 1, n):
            if x[j] == x[i]:
                z += 1  # Increment counter if characters match
            else:
                break  # Exit loop if a different character is found

        # Step 4: Add count to y if greater than 1
        if z > 1:
            y += str(z)

        # Step 5: Move to the next group of characters
        i += z

    # Step 6: Return the result
    return y
