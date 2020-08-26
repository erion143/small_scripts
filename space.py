import os, sys

patt = "{:<3}: {}"

def up():
    os.chdir("..")

def down():
    ls = [d for d in os.listdir() if os.path.isdir(d)]
    if d:
        for ind, val in enumerate(d):
             l = patt.format(ind, val)
             print(l)
        choise = input("where?: ")
        os.chdir(d[int(choise)])
    else:
        print("none...")
    print()

def main():
    act = input(">>")
    os.write(sys.__stdout__, act)

main()