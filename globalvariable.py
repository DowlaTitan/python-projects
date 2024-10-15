def func1():
    x = 24 


    def func2():
        global x
        x = 20  


    print(" before calling the func2 ",x)
    print(" calling the func2 ")
    func2
    print(" after calling the func2 ",x)

