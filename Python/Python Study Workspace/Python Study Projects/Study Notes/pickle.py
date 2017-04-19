D = {"a":1, "b":2}
F = open("datefile.pkl","wb")
import pickle
pickle.dump(D,F)
F.close()

F = open("datafile.pkl","rb")
E = pickle.load(F)
print(E)
