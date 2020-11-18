def my_gcd(a, b):
    mx = max(a, b)
    mn = min(a, b)
    r = mx % mn
    if(r == 0):
        return mn
    return my_gcd(mn, r)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

n = 86108002918518428671680621078381724386896258624262971787023054651438740237393
p = 286748798713412687878508722355577911069
q = 300290718931931563784555212798489747397
e = 0x10001

# 86108002918518428671680621078381724386309219106617627535359990716284672578928
phi = (p-1)*(q-1)

f = open("../problem/encrypted.txt", "r")
c = f.read()
# c = 74806200070710430428438847316507311847202230565058608921850842031191743309425
c = int(c.encode("hex"), 16)


d = modinv(e, phi)
m = pow(c, d, n)
print hex(m)[3:][:-3].decode("hex")[-18:]
