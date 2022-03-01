# def Check(O):
#   if O[0]>0 and O[0]<O[1]:
#     return False
#   if O[3]>0 and O[3]<O[4]:
#     return False
#   return True

step = []

def Children(O):
  res = []

  # rồi
  if O[0] == 0:
    if O[1] <= O[3]:
        child = [O[1], 0, O[2], O[3], O[4], O[5], O[6], O[7], O[8]]
    else:
        child = [O[3], O[1], O[2], 0, O[4], O[5], O[6], O[7], O[8]]
    res.append(child)

  # rồi
  elif O[1] == 0:
    Min = min(O[0], O[2], O[4])
    if Min == O[0]:
        child = [0, O[0], O[2], O[3], O[4], O[5], O[6], O[7], O[8]]
    elif Min == O[2]:
        child = [O[0], O[2], 0, O[3], O[4], O[5], O[6], O[7], O[8]]
    else:
        child = [O[0], O[4], O[2], O[3], 0, O[5], O[6], O[7], O[8]]
    res.append(child)

  # rồi
  elif O[2] == 0:
    if O[1] <= O[5]:
        child = [O[0], 0, O[1], O[3], O[4], O[5], O[6], O[7], O[8]]
    else:
        child = [O[0], O[1], O[3], 0, O[4], O[5], O[6], O[7], O[8]]
    res.append(child)
  
  # rồi
  elif O[3] == 0:
    Min = min(O[0], O[4], O[6])
    if Min == O[0]:
        child = [0, O[1], O[2], O[0], O[4], O[5], O[6], O[7], O[8]]
    elif Min == O[4]:
        child = [O[0], O[1], O[2], O[4], 0, O[5], O[6], O[7], O[8]]
    else:
        child = [O[0], O[1], O[2], O[6], O[4], O[5], 0, O[7], O[8]]
    res.append(child)

  # chưa
  elif O[4] == 0:
    Min = min(O[1], O[3], O[5], O[7])
    if Min == O[1]:
        child = [O[0], 0, O[2], O[3], O[1], O[5], O[6], O[7], O[8]]
    elif Min == O[3]:
        child = [O[0], O[1], O[2], 0, O[3], O[5], O[6], O[7], O[8]]
    elif Min == O[5]:
        child = [O[0], O[1], O[2], O[3], O[5], 0, O[6], O[7], O[8]]
    else:
        child = [O[0], O[1], O[2], O[3], O[7], O[5], O[6], 0, O[8]]
    res.append(child)

  # rồi
  elif O[5] == 0:
    Min = min(O[2], O[4], O[8])
    if Min == O[2]:
        child = [O[0], O[1], 0, O[3], O[4], O[2], O[6], O[7], O[8]]
    elif Min == O[4]:
        child = [O[0], O[1], O[2], O[3], 0, O[4], O[6], O[7], O[8]]
    else:
        child = [O[0], O[1], O[2], O[3], O[4], O[8], O[6], O[7], 0]
    res.append(child)

  # rồi
  elif O[6] == 0:
    if O[3] <= O[7]:
        child = [O[0], O[1], O[2], 0, O[4], O[5], O[3], O[7], O[8]]
    else:
        child = [O[0], O[1], O[2], O[3], O[4], O[5], O[7], 0, O[8]]
    res.append(child)

  # rồi
  elif O[7] == 0:
    Min = min(O[4], O[6], O[8])
    if Min == O[4]:
        child = [O[0], O[1], O[2], O[3], 0, O[5], O[6], O[4], O[8]]
    elif Min == O[6]:
        child = [O[0], O[1], O[2], O[3], O[4], O[5], 0, O[6], O[8]]
    else:
        child = [O[0], O[1], O[2], O[3], O[4], O[5], O[6], O[8], 0]
    res.append(child)

  # rồi
  elif O[8] == 0:
    if O[5] <= O[7]:
        child = [O[0], O[1], O[2], O[3], O[4], 0, O[6], O[7], O[5]]
    else:
        child = [O[3], O[1], O[2], 0, O[4], O[5], O[6], 0, O[7]]
    res.append(child)

  return res


# Số người ở trái, Số quỷ bên trái, vị trí thuyền, Người bên phải, Quỷ bên phải
Start = [1, 4, 3, 5, 2, 6, 8, 7, 0]
#Start = [1, 0, 2, 3, 4, 5, 6, 7, 8]
Goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

OK = False

# 1.Cho đỉnh xuất phát vào open. 
Open = [Start]
Closed = []
# 2. Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
# 6. Trở lại bước 2.
while len(Open) > 0:
  # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
  #O_TT = Open.pop()
  O = Open.pop()
  Closed.append(O)
  # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
  if O == Goal:
    OK = True
    break
  # 5. Tìm tất cả các đỉnh con của ʘ không thuộc open và closed cho vào cuối của open
  for child in Children(O):
    if child not in Open and child not in Closed:
      #Open.append(child, O_TT)
      Open.append(child)


print(OK)
#print(O_TT)
