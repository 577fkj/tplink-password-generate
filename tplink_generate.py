# tplink密码生成
def orgAuthPwd(pwd):
    strDe = "RDpbLfCPsJZ7fiv"
    dic = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3fQ1xtXcPcf1aT303wAQhv66qzW"
    return securityEncode(pwd, strDe, dic)

def securityEncode(pwd, strDe, dic):
    dictionary = dic
    output = ""
    cl = 187
    cr = 187

    len1 = len(pwd)
    len2 = len(strDe)
    lenDict = len(dictionary)
    if len1 > len2:
        lena = len1
    else:
        lena = len2
    index = 0
    while index < lena:
        cl = 187
        cr = 187
        
        if (index >= len1):
            cr = ord(strDe[index])
        elif (index >= len2):
            cl = ord(pwd[index])
        else:
            cl = ord(pwd[index])
            cr = ord(strDe[index])

        output += dictionary[(cl ^ cr) % lenDict]

        index += 1
    return output
