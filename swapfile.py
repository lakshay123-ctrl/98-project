def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    fline = open(file1, 'r') as a:
     data_a = a.read()

	fline2 = open(file2, 'r') as b:
     data_b = b.read()

    fline3 = open(file1, 'w') as a:
     a.write(data_b)

    fline4 = open(file2, 'w') as b:
     b.write(data_a)

swapFileData()