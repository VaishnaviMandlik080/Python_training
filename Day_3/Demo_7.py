fobj = open('r1.log', 'r')
wobj = open('r3.log', 'w')
for line in fobj.readlines():
    wobj.write(line)
fobj.close()
wobj.close()