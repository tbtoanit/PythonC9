#Toi muon sua source code
# from tkinter import *
#
# window = Tk()
# window1 = Tk()
#
# btn_add = Button(window, text = 'Add Two Number')
# btn_add.pack()
#
# window.mainloop()
from nhan_vien_demo import Nhan_Vien

#Gán/assign thông tin dữ liệu cho 1 đối tượng nv1
nv1 = Nhan_Vien(ma_nv = "NV01", ten_nv = "Nguyen Van 456", luong_nv = 2000) #tạo đối tượng nv1

#Gán thông tin dữ liệu cho 1 đối tượng nv2
nv2 = Nhan_Vien()
nv2.ma_nhan_vien = "NV02"
nv2.ten_nhan_vien = "Tran Van 456"
nv2.luong_nhan_vien = 3000

nv3 = Nhan_Vien("NV03", "NGUYEN VAN 456", 4000)

nv4 = Nhan_Vien("NV04", "NGUYEN VAN 789", 4000)

ds_nhan_vien = [nv1,nv2,nv3,nv4]

#dùng vòng lặp để truy suất
for i in range(0,len(ds_nhan_vien)):
    print(ds_nhan_vien[i].ten_nhan_vien)

def xoa_nhan_vien():
    flag = 0
    ten_xoa = input("vui long nhap vao ten nv can xoa: ")
    ds_con_lai = []
    for i in range(0,len(ds_nhan_vien)):
        if ten_xoa not in ds_nhan_vien[i].ten_nhan_vien:
            ds_con_lai.append(ds_nhan_vien[i])
        else:
            flag = 1
    if flag == 0:
        print("Không tìm thấy",ten_xoa)

    return ds_con_lai


ds_con_lai = xoa_nhan_vien()
for i in range(0,len(ds_con_lai)):
    print(ds_con_lai[i].ten_nhan_vien)
