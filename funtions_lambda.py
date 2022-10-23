increment = lambda x : x + 1
full_name = lambda name, last_name : f"{name} {last_name}"
high_ord_function = lambda x, function: x + function(x)

print(increment(20))
print(full_name("Luis Miguel", "Gonzalez Giraldo"))
print(high_ord_function(2, lambda x : x + 2))
