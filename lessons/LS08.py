"""An example function definition."""

def my_max (a: int, b:int) -> int:
    """Return the largest argument."""
    if a >= b:
        return a
    else:
        return b

print (my_max (10 + 1, 10))  

x : int = 6
y : int = 2 + 5
print (my_max(x , y))

"""same as below"""
x : int = 6
y : int = 2 + 5
z : int = my_max (x , y)
print (z)