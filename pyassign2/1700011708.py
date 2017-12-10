from urllib.request import urlopen

def exchange(currency_from,currency_to,amount_from):
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    for fh in '{":,}':
        jstr=jstr.replace(fh,"")
    for zfc in jstr.split():
        if zfc.find(".")==1 and float(zfc)!=amount_from:
            jieg=float(zfc)    
    return(jieg)

def test_it():
    assert(exchange('USD','EUR',2.5)==exchange('USD','EUR',2.5))

frm=input()
tto=input()
amt=input()

def testAll():
    test_it()
    print("All tests passed")

print(exchange(frm,tto,amt))