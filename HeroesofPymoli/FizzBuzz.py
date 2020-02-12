# %%
fizz = int(input("Pick a number, one (1) to ten (10): "))
buzz = int(input("Now, pick another one: "))
maximum = int(input("How high shall we count? "))+1
series = range(1, maximum)

# %%
for num in series:
    readout = ""
    if (num % fizz) == 0:
        readout += "Fizz"
    if (num % buzz) == 0:
        readout += "Buzz"
    print(str(num)+": "+readout)

# %%
