def mul(z):
	for i in range(len(z)):
		for j in range(len(z[0])):
			print(z[i][j])
			
	for h in z:
		print(h)
r1=int(input("enter the no of rows"))
c1=int(input("enter the no of column"))
r2=int(input("enter the no of rows"))
c2=int(input("enter the no of column"))
m1=[[0 for j  in range (0,c1)]for i in range(0,r1)]
m2=[[0 for j in range (0,c2)]for i in range(0,r2)]
r=[[0 for j in range (0 ,c2)]for i in range(0 ,r1)]
if(c1!=r2):
	print("given matrixs not obey multiplication")
	exit();
	
print("enter m1")
for i in range(0 ,r1):
	for j in range(0 ,c1):
		m1[i][j]=int(input("enter elements for m1"))
print("enter m2")
for i in range(0 ,r2):
	for j in range(0 ,c2):
		m2[i][j]=int(input("enter elements for m2"))
print("first matrix")
mul(m1)
print("second matrix")
mul(m2)
for i in range(0 ,r1):
	for j in range(0 ,c2):
		for k in range(0 ,r2):
			r[i][j]+=m1[i][k]*m2[k][j]
print("result matrix")
mul(r)	

