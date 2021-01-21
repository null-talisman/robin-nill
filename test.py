# testing 

def stringTest():
    x = "['114.400000']"
    x_len = len(x)
    print("Stock Price (Unformatted): " + str(x))
    print("Stock Price Length: " + str(x_len))
    print("Formatted Price: " + x[2:x_len-6])

stringTest()


