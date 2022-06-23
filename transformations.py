
def find_transformations():
    #txt = in_n_out.split()
    finalstr =""
    originalstr = "Bling"
    encriptedstr = "GlibN"
    for i in range(len(originalstr)) :
        for j in range(len(encriptedstr)):
            if originalstr[i] == encriptedstr[j].lower():
                if originalstr[i].islower() and encriptedstr[j].isupper():
                    if j-i >0:
                        k = j-i
                    elif j-i ==0:
                        k=i
                    else :
                        k = abs(j-i)
                    finalstr =  finalstr+str(k) + "U"
                elif originalstr[i].isupper() and encriptedstr[j].islower():
                    if j-i >0:
                        k = j-i
                    elif j-i ==0:
                        k=i
                    else :
                        k = abs(j-i)
                    finalstr =finalstr+ str(k) + "L"
                else:
                    if j-i >0:
                        k = j-i
                    elif j-i ==0:
                        k=i
                    else :
                        k = abs(j-i)
                    finalstr = finalstr+str(k)+ "O"
    return finalstr

#abc = input()
result = find_transformations()
print(result)