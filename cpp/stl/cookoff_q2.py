import sys
import math
from collections import defaultdict,Counter

# input=sys.stdin.readline
# def print(x):
#     sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP1/output.txt",'w')
# sys.stdin=open("CP1/input.txt",'r')
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
	newlines = 0

	def __init__(self, file):
		self._fd = file.fileno()
		self.buffer = BytesIO()
		self.writable = "x" in file.mode or "r" not in file.mode
		self.write = self.buffer.write if self.writable else None

	def read(self):
		while True:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			if not b:
				break
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines = 0
		return self.buffer.read()

	def readline(self):
		while self.newlines == 0:
			b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
			self.newlines = b.count(b"\n") + (not b)
			ptr = self.buffer.tell()
			self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
		self.newlines -= 1
		return self.buffer.readline()

	def flush(self):
		if self.writable:
			os.write(self._fd, self.buffer.getvalue())
			self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
	def __init__(self, file):
		self.buffer = FastIO(file)
		self.flush = self.buffer.flush
		self.writable = self.buffer.writable
		self.write = lambda s: self.buffer.write(s.encode("ascii"))
		self.read = lambda: self.buffer.read().decode("ascii")
		self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

mod=pow(10,9)+7
'''solution 1'''

t=int(input())
for i in range(t):
	a=input()
	b=input()
	eve=0
	odd=0
	ans=0
	for j in range(len(a)):
		if a[j]!=b[j]:
			if j%2==0:
				eve=1
			else:
				odd=1
		else:
			if j%2==0 and eve==1:
				ans+=1
				eve=0
			elif j&1 and odd==1:
				ans+=1
				odd=0
	print(ans+eve+odd)

''' solution 2'''
# t=int(input())
# for you in range(t):
#     a=input()
#     b=input()
#     n=len(a)
#     odd=[]
#     even=[]
#     for i in range(0,n,2):
#         if(a[i]!=b[i]):
#             even.append(i)
#     for i in range(1,n,2):
#         if(a[i]!=b[i]):
#             odd.append(i)
#     count=0
#     z=len(odd)
#     for i in range(1,z):
#         if(odd[i]-odd[i-1]!=2):
#             count+=1
#     if(z):
#         count+=1
#     for i in range(1,len(even)):
#         if(even[i]-even[i-1]!=2):
#             count+=1
#     if(len(even)):
#         count+=1
#     print(count)