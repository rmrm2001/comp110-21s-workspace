"""Unconditional love."""

how_much: int = int(input("Pick a number between 0-100."))

if how_much < 50:
    print ("I Love You.")
else:
    if how_much < 75:
        print("I Really Love You.")
    else:
        print("ILYSM!!!")

if how_much == 50:
    print("nah")
"""this second if is a separate operation to the first if"""

