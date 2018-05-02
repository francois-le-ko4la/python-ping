
class monobj(object):
    def __init__(self):
        self.montest=3

def test(obj, objtype):
    if isinstance(obj, monobj): return True
    return False

a = monobj()
b = monobj()

print(test(a, b))

print(test("zseflj", b))


