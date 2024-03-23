import os
import json


while 1:
    print("請選擇模式:")
    print("1. chart.json - > output.txt")
    print("2. input.tja + hw0105.exe -> output.txt")
    cmd = input()
    if cmd == '1':
        q = open("output.txt", "w+")
        w = json.load(open("chart.json", 'r'))
        for i in w:
            for j in w[i]:
                a = j['course']
                b = j['chart']
                q.write("course: {}\n".format(a))
                for r in b:
                    q.write("[{},{:.6f}]\n".format(r[0], r[1]))
                q.write("\n")
        print("轉換完成！")
    elif cmd == '2':
        os.system("hw0105.exe <input.tja> output.txt")
        print("轉換完成！")
    else:
        print("指令輸入錯誤！")
