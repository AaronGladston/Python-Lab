flag = 0
with open("31_file.txt","r") as file:
    with open("31_res.txt","r") as myfile:
        myfile = open("31_res.txt","w")
        for line in file:
            if flag%2==0:
                myfile.write(line)
            flag += 1