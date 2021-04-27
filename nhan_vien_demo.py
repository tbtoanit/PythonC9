#Long test sua nhanviendemo

class Nhan_Vien():
    #tạo những thông tin về thuộc tính/ properties
    ma_nhan_vien = ""
    ten_nhan_vien = ""
    luong_nhan_vien = 0

    #Hàm tạo (mặc định)/ có tham số
    def __init__(self,ma_nv = "", ten_nv = "", luong_nv = 0):
        print("Ham tao duoc goi den")
        self.ma_nhan_vien = ma_nv
        self.ten_nhan_vien = ten_nv
        self.luong_nhan_vien = luong_nv

    #hành vi, chức năng/ behavior
    def xoa_mot_nhan_vien(self):
        print("nguoi dung muon xoa di mot nhan vien")

    def them_mot_nhan_vien(self):
        print("nguoi dung muon them moi mot nhan vien")
