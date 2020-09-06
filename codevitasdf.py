# # def two(s, r, n):
# #     if n == 1:
# #         t = 1 - s.count(chr(r))
# #         return t
# #     a = s[:n//2]
# #     b = s[n//2:]
# #     t = n//2-a.count(chr(r))+two(b, r+1, n//2)
# #     m = n//2-b.count(chr(r))+two(a, r+1, n//2)
# #     return min(t, m)
# # for _ in range(int(input())):
# #     n = int(input())
# #     s = input()
# #     r = 97
# #     print(two(s, r, n))
# # def foom():
# # 	testcase = int(input())
# # 	bride = list(input())
# # 	groom = list(input())
# # 	match = 0
# # 	for i in range(len(bride)):
# # 		for j in range(len(groom)):
# # 			if groom == bride:
# # 				return 0
# # 			if match>len(groom)+1:
# # 				return len(groom)
# # 			else:
# # 				if bride[0] == groom[0]:
# # 					bride.remove(bride[0])
# # 					groom.remove(groom[0])
# # 				else:
# # 					a = groom[0]
# # 					groom.remove(groom[0])
# # 					groom.append(a)
# # 					match +=1
# # 	return len(groom)
# # print(foom())
# # testcase = int(input())
# # ls = list(map(int, input().split()))
# # answer =[]
# # for j in ls:
# # 	#if len(j)>2:
# # 	l =int(max(str(j)))*11
# # 	print(l)
# # 	s = int(min(str(j)))*7
# # 	print(s)
# # 	c = str(l+s)
# # 	ap = c[len(c)-2::]
# # 	answer.append(int(ap))
# # print(answer)
# # def swamwar():
# # 	testcase = int(input())
# # 	f =  input()
# # 	m = input()
# # 	cr = m.count("r")
# # 	cm = m.count("m")
# # 	ls = [i for i  in f]

# # 	for i in f:
# # 		if i =="r":
# # 			if cr ==0:
# # 				return len(ls)
# # 			cr -=1
# # 			ls.pop(0)
# # 		elif i == "m":
# # 			if cm ==0:
# # 				return len(ls)
# # 			cm -=1
# # 			ls.pop(0)
# # 	else:
# # 		print(0, end='')

# # print(swamwar())

# # 4
# # rrmm
# # mrmr
# # 4
# # rmrm
# # mmmr

# def PetrolPump():
# 	vl = sorted(list(map(int, input().split())))
# 	print(vl)
# 	print(sum(vl))
# 	check = sum(vl) //2
# 	front =True
# 	bb =[]
# 	summ = 0
# 	summ2 =0
# 	a=0
# 	b =1
# 	for i in range(len(vl)):
# 		print(f"sum is {summ}")
# 		if summ >check:
# 			summ2 = check-summ
# 			print(bb)
# 			print(f"part 1:{summ}, part2 : {check}")
# 			if summ2>check:
# 				return sum(bb)
# 			else:
# 				return check
# 		if front:
# 			bb.append(vl[a])
# 			summ+=vl[a]
# 			a+=1
# 	#		bb.append(summ)
# 			front= False
# 		else:
# 			bb.append(vl[len(vl)-(b)])
# 			summ+=vl[len(vl)-b]
# 			b+=1
# 	#		bb.append(summ)
# 			front =True
	

	
# print(PetrolPump())
#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


def main():
	def monkey(a):
		y = a
		x = [0]*len(a)
		count = 0
		while x!=a:
			count+=1
			x= [0]*len(a)
			for i in range(len(a)):
				x[a[i]-1] =y[i]
			y =x
		return count
	
	t = int(input())
	for j in range(t):
		n = int(input())
		mon = list(map(int, input().split()))
		res = monkey(mon)
		print(res)


# region fastio

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


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()



