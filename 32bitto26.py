card32 = bin(1372617403)
card32 = card32[-26:]
card32l = card32[-13:]
card32f = card32[:-13]


if card32l.count('1') % 2 == 0:
    card32l += '1'
else:
    card32l += '0'
card32fin = card32f + card32l
print(int(card32fin, 2))



        




