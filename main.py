def swapFileData():
    File1=input("Enter file 1 ")
    File2=input("Enter file 2 ")
    with open(File1,'r') as f:
        words_a=f.read()
    with open(File2,'r') as e:
        words_b=e.read()
    with open(File1,'w') as f:
        f.write(words_b)
    with open(File2,'w') as e:
        e.write(words_a)
    print("Message has been swapped")
swapFileData()        