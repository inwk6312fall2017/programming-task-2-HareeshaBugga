
with open(r"Crime.csv",'r') as infile:
        data=infile.read()
        print(data)
        for line in data:
                parts = [p for p in line.split("\t")]
                if line=="Assault":
                        print (line)
                        spamreader = data.reader(data, delimiter=' ', quotechar$
                        for row in spamreader:
                                print (', '.join(row))

                                for num in row:
                                        if num==int:
                                                print (num)
