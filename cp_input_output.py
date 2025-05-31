from sys import stdin,stdout
n = int(stdin.readline().strip())
l = list(map(int,stdin.readline().strip().split()))[:n]
stdout.write(str(l))
