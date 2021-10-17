def ItsMe(fn):
    def wrapped():
        return fn() + "it's me"
    return wrapped

def AddU(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@AddU
@ItsMe
def Hi():
    return "Hi, "

print(Hi())
