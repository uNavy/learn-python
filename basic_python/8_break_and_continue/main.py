# BREAK STATEMENT - STOPPING A LOOP BASED ON A CONDITION
# THIS LOOP RUNS INDEFINITELY UNTIL THE USER ENTERS A NUMBER THAT IS NOT DIVISIBLE BY 3
#%%
while True:
    n = int(input("ENTER A NUMBER DIVISIBLE BY 3: "))  # USER INPUT
    if n % 3 != 0:
        break  # TERMINATE THE LOOP WHEN THE NUMBER IS NOT DIVISIBLE BY 3
    print("%d IS DIVISIBLE BY 3" % (n))  # PRINT CONFIRMATION IF NUMBER IS VALID
#%%
# CONTINUE STATEMENT - SKIPPING AN ITERATION BASED ON A CONDITION
# THIS LOOP ITERATES FROM 0 TO 9, BUT SKIPS VALUES LESS THAN 3 OR GREATER THAN 7
for i in range(10):
    if i < 3 or i > 7:
        continue  # SKIP THE REMAINING CODE IN THIS ITERATION AND MOVE TO THE NEXT VALUE
    print(i)  # ONLY PRINTS NUMBERS FROM 3 TO 7 (3, 4, 5, 6, 7)
#%%
# SIMULATING A LABELED LOOP USING A FLAG VARIABLE
# THIS CREATES A PATTERN OF STARS (*) WITH A LIMIT ON THE INNER LOOP USING A FLAG
max_rows = int(input("Number of Stars: "))  # USER INPUT TO DEFINE THE MAXIMUM NUMBER OF ROWS
continue_outer_loop = True  # FLAG TO CONTROL THE OUTER LOOP

for current_row in range(max_rows):  # OUTER LOOP - CONTROLS THE NUMBER OF ROWS
    if not continue_outer_loop:
        break  # IF FLAG IS FALSE, TERMINATE THE OUTER LOOP

    for current_star_count in range(current_row + 1):  # INNER LOOP - CONTROLS THE NUMBER OF COLUMNS IN EACH ROW
        print("*", end=" ")  # PRINT A STAR WITHOUT MOVING TO A NEW LINE
        if current_star_count >= 7:  # LIMIT THE INNER LOOP TO A MAXIMUM OF 8 STARS
            continue_outer_loop = False  # SET FLAG TO FALSE TO STOP THE OUTER LOOP
            break  # TERMINATE THE INNER LOOP WHEN THE STAR COUNT REACHES 8
    print()  # MOVE TO THE NEXT LINE AFTER PRINTING A ROW OF STARS


#%%
# SIMULATING A LABELED LOOP USING A FLAG VARIABLE
# THIS CREATES A PATTERN OF STARS (*) WITH A LIMIT ON THE INNER LOOP USING A FLAG

max_rows = int(input("Number of Stars: "))  # USER INPUT TO DEFINE THE MAXIMUM NUMBER OF ROWS
continue_outer_loop = True  # FLAG TO CONTROL THE OUTER LOOP

print("\nDEBUG: Starting the outer loop...\n")

for rows in range(max_rows):  # OUTER LOOP - CONTROLS THE NUMBER OF ROWS

    print("\nDEBUG: Outer Loop Continue: ", continue_outer_loop)
    if (not continue_outer_loop):
        print("\nDEBUG: Outer loop stopped. Exiting...\n")  # ✅ This will now always be printed before breaking
        break  # EXIT OUTER LOOP
    print(f"DEBUG: Current row -> {rows}")
    
    star_row = ""  # Collect stars for proper formatting
    for columns in range(rows + 1):  # INNER LOOP - CONTROLS THE NUMBER OF COLUMNS IN EACH ROW
        print(f"DEBUG: Printing star {columns + 1} in row {rows}")
        star_row += "* "  # Append stars to a string for proper printing
        
        if columns >= 7:  # LIMIT THE INNER LOOP TO A MAXIMUM OF 8 STARS
            continue_outer_loop = False  # SET FLAG TO FALSE TO STOP THE OUTER LOOP
            print("DEBUG: Star limit reached (8 stars). Flag set to False. Breaking inner loop...\n")
            break  # TERMINATE THE INNER LOOP WHEN THE STAR COUNT REACHES 8
    
    print(star_row)  # PRINT STARS AFTER THE DEBUG LOGS

   

print("\nDEBUG: Program execution completed.\n")


#%%
# INPUT JUMLAH BARIS 
print("\nDEBUG: Memulai outer loop...\n")

while True:  # Loop luar
    user_input = input("Loop 1 - Masukkan perintah (break/continue): ").strip().lower()

    if user_input == "break":
        print("DEBUG: Perintah 'break' diterima di loop luar. Program berhenti total.\n")
        break  # Menghentikan semua loop

    elif user_input == "continue":
        print("DEBUG: Perintah 'continue' diterima di loop luar. Masuk ke loop dalam...\n")

        while True:  # Loop dalam
            print("Berjalan di loop dalam")
            nested_input = input("Loop 2 - Masukkan perintah (break/continue): ").strip().lower()

            if nested_input == "break":
                print("DEBUG: Perintah 'break' diterima di loop dalam. Kembali ke loop luar...\n")
                break  # Keluar dari loop dalam, kembali ke loop luar

            elif nested_input == "continue":
                print("DEBUG: Perintah 'continue' diterima di loop dalam.\n")
                continue  # Langsung kembali ke loop luar

            print(f"DEBUG: Loop dalam masih berjalan. Input: {nested_input}\n")

    print("DEBUG: Loop luar masih berjalan...\n")

# %%
