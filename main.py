import json

q = open("output.txt","w+")
w = json.load(open("input.json",'r'))
for i in w:
    for j in w[i]:
        a = j['course']
        b = j['chart']
        q.write("course: {}\n".format(a))
        for r in b:
            q.write("[{},{:.6f}]\n".format(r[0],r[1]))
        q.write("\n")
