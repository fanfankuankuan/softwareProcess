'''
Created on Oct 2, 2015

@author: KevinFAN
'''
class hexe(object):
    x= 1
    a = x*10
    a = int(a)
    b = hex(a)
    tempStr = 'x'
    c = b.find(tempStr)
    d = b[(b.find(tempStr)+1):]
    if x>=1.6 and x<25.6:
        d = "00"+d
        print d
    elif x>=0 and x<1.6:
        d ="000"+d
        print d
    elif x>=25.6 and x<409.6:
        d = "0"+d
        print d
    elif x>=409.6:
        print d
    elif x<0 and x>=-383.9:
        b = hex(4095+a)
        c = b.find(tempStr)
        d = b[(b.find(tempStr)+1):]
        d = "f"+d
        print d
    else:
        raise ValueError("")
    minBright = d
    try:
        if minBright=="18696":
            return None
        return minBright
    except:
        return None
        raise ValueError("")   