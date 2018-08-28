##ASSIGNMENT-10

#Question-1

x = open('test.txt','r')
data = x.read()
print(data)
x.close()

#Question-2
x = open('test.txt','r')
data = x.read()
g=input("")
y = data.count(g)
print(y)
x.close()

#Question-3

x = open('test.txt','r')
data = x.read()
y=open('test1.txt','w')
y.write(data)
x.close()

#Question-4

x = open('test.txt','r')
y = open('cor.txt','r')
z = open('newdoc.txt','w+')
a = x.readlines()
b = y.readlines()
for i,j in zip(a,b):
    z.write(i)
    z.write(j)
l = z.read()
print(l)


#Question-5

x=open('test.txt')
y=open('file.txt','w+')
a=x.readlines()
a.sort()
y.write(str(a))
z=y.read()
print(z)
