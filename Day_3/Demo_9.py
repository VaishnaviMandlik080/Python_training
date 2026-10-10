def file_read():
    fobj = open('r1.log', 'r')
    s = fobj.read()
    fobj.close()
    print("File content: \n")
    print(s)
    print("End of file content")

def calculate_sales_cost():
    total = 0
    for var in [10,20,30,40,50]:
        total += var
    print("Total sales cost:", total)

print ("This is the Main block")
file_read()
print("")
calculate_sales_cost()
print("")
if(True):
    file_read()
print("End of the script")