def divide(a,b):
    try:
        return int(a)/int(b)
    except Exception as e:
        return "Exception: ", e

#print(divide(10,0))
