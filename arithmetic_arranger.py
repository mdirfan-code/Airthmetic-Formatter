import re
def arithmetic_arranger(problems,ans=False):
    if(len(problems)>5):
        return "Error: Too many problems."
    if "*" in ("".join(problems)) or   "/" in ("".join(problems)):
        return "Error: Operator must be '+' or '-'."
    if re.search(r"[^0-9\s+-]",("".join(problems))):
        return "Error: Numbers must only contain digits."
    if re.search(r'\d{5,}',(" ".join(problems))):
        return "Error: Numbers cannot be more than four digits."
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
    if(ans):
        return "    ".join(fl)+"\n"+"    ".join(sl)+"\n"+"    ".join(ln)+"\n"+"    ".join(an)
    return "    ".join(fl)+"\n"+"    ".join(sl)+"\n"+"    ".join(ln)
       

        

    


    
  