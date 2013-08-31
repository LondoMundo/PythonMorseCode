while 1==1:
    want = raw_input("Do you want to encode[e] or decode[d]?")
    if want == "e":
        i = raw_input("What do you want to convert to morse code?")
        numberOf = len(i)
        f = open('output.txt', 'w')
        for i in i:
            if i == "a":
                print ".-"
                f.write(".-\n")
            elif i == "b":
                print "-..."
                f.write("-...\n")
            elif i == "c":
                print "-.-."
                f.write("-.-.\n")
            elif i == "d":
                print "-.."
                f.write("-..\n")
            elif i == "e":
                print "."
                f.write(".\n")
            elif i == "f":
                print "..-."
                f.write("..-.\n")
            elif i == "g":
                print "--."
                f.write("--.\n")
            elif i == "h":
                print "...."
                f.write("....\n")
            elif i == "i":
                print ".."
                f.write("..\n")
            elif i == "j":
                print ".---"
                f.write(".---\n")
            elif i == "k":
                print "-.-"
                f.write("-.-\n")
            elif i == "l":
                print ".-.."
                f.write(".-..\n")
            elif i == "m":
                print "--"
                f.write("--\n")
            elif i == "n":
                print "-."
                f.write("-.\n")
            elif i == "o":
                print "---"
                f.write("---\n")
            elif i == "p":
                print ".--."
                f.write(".--.\n")
            elif i == "q":
                print "--.-"
                f.write("--.-\n")
            elif i == "r":
                print ".-."
                f.write(".-.\n")
            elif i == "s":
                print "..."
                f.write("...\n")
            elif i == "t":
                print "-"
                f.write("-\n")
            elif i == "u":
                print "..-"
                f.write("..-\n")
            elif i == "v":
                print "...-"
                f.write("...-\n")
            elif i == "w":
                print ".--"
                f.write(".--\n")
            elif i == "x":
                print "-..-"
                f.write("-..-\n")
            elif i == "y":
                print "-.--"
                f.write("-.--\n")
            elif i == "z":
                print "--.."
                f.write("--..\n")
            elif i == " ":
                print " "
                f.write(" \n")
        f.close()

    elif want == "d":
        FilePath = raw_input("Type the name of the file you want to decode")
        f=open(FilePath, "r")
        lines = f.readlines()
        i=0
        newfile = open('decoded.txt', 'w+')
        while 1==1:
            try:
                if lines[i].rstrip() == ".-":
                    print "a"
                    newfile.write("a")
                elif lines[i].rstrip() == "-...":
                    print "b"
                    newfile.write("b")
                elif lines[i].rstrip() == "-.-.":
                    print "c"
                    newfile.write("c")
                elif lines[i].rstrip() == "-..":
                    print "d"
                    newfile.write("d")
                elif lines[i].rstrip() == ".":
                    print "e"
                    newfile.write("e")
                elif lines[i].rstrip() == "..-.":
                    print "f"
                    newfile.write("f")
                elif lines[i].rstrip() == "--.":
                    print "g"
                    newfile.write("g")
                elif lines[i].rstrip() == "....":
                    print "h"
                    newfile.write("h")
                elif lines[i].rstrip() == "..":
                    print "i"
                    newfile.write("i")
                elif lines[i].rstrip() == ".---":
                    print "j"
                    newfile.write("j")
                elif lines[i].rstrip() == "-.-":
                    print "k"
                    newfile.write("k")
                elif lines[i].rstrip() == ".-..":
                    print "l"
                    newfile.write("l")
                elif lines[i].rstrip() == "--":
                    print "m"
                    newfile.write("m")
                elif lines[i].rstrip() == "-.":
                    print "n"
                    newfile.write("n")
                elif lines[i].rstrip() == "---":
                    print "o"
                    newfile.write("o")
                elif lines[i].rstrip() == ".--.":
                    print "p"
                    newfile.write("p")
                elif lines[i].rstrip() == "--.-":
                    print "q"
                    newfile.write("q")
                elif lines[i].rstrip() == ".-.":
                    print "r"
                    newfile.write("r")
                elif lines[i].rstrip() == "...":
                    print "s"
                    newfile.write("s")
                elif lines[i].rstrip() == "-":
                    print "t"
                    newfile.write("t")
                elif lines[i].rstrip()== "..-":
                    print "u"
                    newfile.write("u")
                elif lines[i].rstrip() == "...-":
                    print "v"
                    newfile.write("v")
                elif lines[i].rstrip() == ".--":
                    print "w"
                    newfile.write("w")
                elif lines[i].rstrip() == "-..-":
                    print "x"
                    newfile.write("x")
                elif lines[i].rstrip() == "-.--":
                    print "y"
                    newfile.write("y")
                elif lines[i].rstrip() == "--..":
                    print "z"
                    newfile.write("z")
                elif lines[i].rstrip() == "":
                    print " "
                    newfile.write(" ")
                i+=1
            except:
                break
        newfile.close()
        f.close()
        





        
    
