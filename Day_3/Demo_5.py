wobj = open("r1.log", "w")
wobj.write("Sample data\n")
wobj.write("Product name is pA and cost is 4565\n")
pname = 'pB'
pcost = 345344.23
wobj.write(f"Product name is {pname} and cost is {pcost}\n")
wobj.write('------------------- x ---------------------\n')
wobj.close()