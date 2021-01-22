#!/usr/bin/env python

import socket
import binascii as ba
from binascii import hexlify, unhexlify

TCP_IP = '127.0.0.1'
TCP_PORT = 8882
BUFFER_SIZE = 1024

# sample BSMs: select one for testing
# txt=b"001480CF4B950C400022D2666E923D1EA6D4E28957BD55FFFFF001C758FD7E67D07F7FFF8000000002020218E1C1004A40196FBC042210115C030EF1408801021D4074CE7E1848101C5C0806E8E1A50101A84056EE8A1AB4102B840A9ADA21B9010259C08DEE1C1C560FFDDBFC070C0222210018BFCE309623120FFE9BFBB10C8238A0FFDC3F987114241610009BFB7113024780FFAC3F95F13A26800FED93FDD51202C5E0FE17BF9B31202FBAFFFEC87FC011650090019C70808440C83207873800000000001095084081C903447E31C12FC0"

txt=b"0014251d59d162dad7de266e9a7d1ea6d4220974ffffffff8ffff080fdfa1fa1007fff0000640fa0"

# txt=b"0012815338033020204bda0d4cdcf8143d4dc48811860224164802280008002297d4bc80a0a0a9825825923a90b2f2e418986f41b7006480602403812020084015480010004521d9f001414160c7c42a1879858619502a42a060e927100662000400105be6bf41c8aded5816ebc050507dcb860ec57aead5079e02828900890001000417223a50728b750f9c6ea9e8ae480a0a0f68746ad447c002828900a0880704404020803b9000200062b68d5305d1f9269a725027d8352f72867d6c82403340004000c53f5b761abbb7d35d3c0813ec1a3baac16bfc048050240301202008402208001000310fe55f849acd608d8ace136b440000dfe4808880008002086365c0017d1612eb34026067404895390907bd848050440302201c100024000200000090026180a0a0f2852600140001000000169fc1585bd1da000b00008000000a3bb2f439459a80060000400000046d55c416c67f40"

hexed = hexlify(txt)
print(hexed)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(hexed)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)