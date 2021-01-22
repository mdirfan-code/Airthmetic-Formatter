import re
ans=True
problems=["34 + 78","798 + 6777","987 + 78","89 + 678","1234 - 79"]
if(len(problems)>5):
    print("Error: Too many problems.")
elif "*" in ("".join(problems)) or   "/" in ("".join(problems)):
    print("Error: Operator must be '+' or '-'.")
elif re.search(r"[^0-9\s+-]",("".join(problems))):
    print("Error: Numbers must only contain digits.")
elif re.search(r'\d{5,}',(" ".join(problems))):
    print("Error: Numbers cannot be more than four digits.")
else:
    print("alright")
fl=[]
sl=[]
ln=[]
an=[]
for prbl in problems:
    op1,opr,op2=prbl.split()
    sz=max(len(op1),len(op2))
    ln.append("-"*(sz+2))
    fl.append("  "+" "*(sz-len(op1))+op1)
    sl.append(opr+" "+" "*(sz-len(op2))+op2)
    if(ans): an.append("{msg: >{fill}}".format(msg=eval(prbl),fill=sz+2))
print("    ".join(fl)+"\n"+"    ".join(sl)+"\n"+"    ".join(ln)+"\n"+"    ".join(an)+"\n" )   