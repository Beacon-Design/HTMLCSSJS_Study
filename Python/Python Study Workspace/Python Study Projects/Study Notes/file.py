# coding=utf-8

print('''
------file------------------------------------------------------
the filename can be a full directory path if you need to access 
a file elsewhere on your computer.

***dir(f)***

''')
print("""

Operation                         Interpretation

output = open(r'C:\spam', 'w')         Create output file ('w' means write)
input = open('data', 'r')              Create input file ('r' means read)
input = open('data')                   Same as prior line ('r' is the default)
aString = input.read()                 Read entire file into a single string
aString = input.read(N)                Read up to next N characters (or bytes) into a string
aString = input.readline()             Read next line (including \n newline) into a string
aList = input.readlines()              Read entire file into list of line strings (with \n)
output.write(aString)                  Write a string of characters (or bytes) into file
output.writelines(aList)               Write all line strings in a list into file
output.close()                         Manual close (done for you when file is collected)
output.flush()                         Flush output buffer to disk without closing
anyFile.seek(N)                        Change file position to offset N for next operation
for line in open('data'): use line     File iterators read line by line
open('f.txt', encoding='latin-1')      Python 3.X Unicode text files (str strings)
open('f.bin', 'rb')                    Python 3.X bytes files (bytes strings)
codecs.open('f.txt', encoding='utf8')  Python 2.X Unicode text files (unicode strings)
open('f.bin', 'rb')                    Python 2.X bytes files (str strings)


afile = open(filename, mode)
afile.method()



""")
print(open(r'G:\Python Project\_TEST_\x.txt').readline())
print(open('G:\\Python Project\\_TEST_\\x.txt').readline())
print(open('G:/Python Project/_TEST_/x.txt').readline(),"\n")

X,Y,Z = 43,44,45
S = 'Spam'
D = {'a':1,'b':2}
L = [1,2,3]
A = open('datafile.txt','w')
A.write(S + '\n')
A.write('%s,%s,%s\n' % (X, Y, Z))
A.write(str(L) + '$' + str(D) + '\n')
A.close()


charts = open('datafile.txt').read()
print(charts)
F = open("datafile.txt")
line = F.readline()
print(line)



print('''-----------------------------------------------------------------------
------ Buffering ---------------------------------------------------------------
The open function takes a third (optional) parameter, which controls the 
buffering of the file. If the parameter is 0 (or False), input/output (I/O) is
unbuffered (all reads and writes go directly from/to the disk); if it is 1 (or True),
I/O is buffered (meaning that Python may use memory instead of disk space to 
make things go faster, and only update when you use flush or close see the 
section "Closing Files," later in this chapter). Larger numbers indicate the 
buffer size (in bytes), while �C1 (or any negative number) sets the buffer size
to the default.

''')



print(r'''Files can be opened in universal newline support mode, 
using the mode character U together with,for example, r. In this mode, 
all line-ending characters/strings (\r\n, \r, or \n) are then converted to newline
characters (\n), regardless of which convention is followed on the current platform
''')



p = '''\
File
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)



'''
f = open("p.txt","w")
f.write(p)
f.close()

f = open("p.txt","r")
while True:
    line = f.readline()
    print(line,end = "")
f.close()




