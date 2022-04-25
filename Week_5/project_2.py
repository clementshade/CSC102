lis1 = ["hello","bye","care","abc"]
let = list(input("required letters"))
def uses_all(a):
    use_all = True
    for i in let:
        if i in list(a):
            pass
        else:
            use_all = False
    print(a,use_all)

for a in lis1:
    uses_all(a)
