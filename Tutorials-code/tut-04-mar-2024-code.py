class StrContainer:
    string = ""
    length = 0
    touched = False

def populate(x):
    strCont = StrContainer()
    strCont.string = x
    strCont.length = len(x)
    return strCont

strings = """
    haru no nioi mo
    mefuku hana mo 
    tachisukumu atashi ni 
    kimi wo tsurete wa konai
    """.split()

paddedStrs = map(lambda s : s+' ',strings)
strContainers = map(populate, paddedStrs)

strTups = map( lambda s : (s.string,s.length,s.touched), strContainers)
updatedStrTups = map( lambda t : (t[0][0:t[1]-1],t[1]-1,True), strTups)

print(list(map(lambda t: t[0],updatedStrTups)))
