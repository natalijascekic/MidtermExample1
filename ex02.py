#da li string moze da se konvertuje u broj
def  moze_li_u_float(string_broj):
    if not isinstance(string_broj,str):
        return False

    dozvoljeni_karakteri = ['0','1','2','3','4','5','6','7','8','9','.','-']

    for karakter in string_broj:
        if karakter not in dozvoljeni_karakteri:
           return False

    return True

print(moze_li_u_float("15264"))