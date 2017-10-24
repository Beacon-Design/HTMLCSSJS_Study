
t1 = 'I think %s is a prefectly normal thing to do in public'
def sub1(s):
    return t1 % s
print(sub1("running"))


t2 = 'I think %s and %s are prefectly normal things to do in public'
def sub2(s1, s2):
    return t2 % (s1, s2)
print(sub2("running", "jumping"))


t3 = "I'm %(nickname)s. My real name is %(name)s."
def sub_m(name, nickname):
	return t3 % {'name': name, 'nickname': nickname}
print(sub_m('jimmy', 'jim'))



