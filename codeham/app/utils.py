from app import models
from app.models import Chuc_nang
from flask import Flask, render_template, redirect, url_for
import os
cover_text = models.cover_texts  # văn bản dùng để giấu tin, ấy nó bằng cách đọc file người dùng tải lên
ma = models.message  # thông tin cần giấu, dùng post để lất
stego_text = ''  # dùng để ghép chuỗi lại với nhau
encryp_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '!', '"', '#', '$', '%',
                '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
                '^', '_', '`', '{', '|', '}', '~']


def ma_hoa_thong_diep(thong_diep=None):
    if thong_diep:
        arr_thong_diep = list(
            thong_diep.upper())  # cắt 1 mảng chữ in hoa thành các kí tự, ví dụ: ['H', 'I', 'E', 'N', 'V', 'Y']
    else:
        'Ban chua nhap thong diep'
    s = ''
    for c in arr_thong_diep:
        if c in encryp_table:
            print(encryp_table.index(c))
            s += bin(encryp_table.index(c))[2:].zfill(8)  # tìm xem ký tự cần giấu nằm ở đâu trong chuỗi, lấy cái số index đó mã hoá nhị phân 8 bit

    return s  # trả về chuỗi gồm mã nhị phân, ví dụ: '00010110101011110000'


def tach_chuoi(text=None, key=None): # phải kiểm tra khoá >=2 ở 1 chỗ nào đó
    arr_tach_chuoi = list(text)  # cắt văn bản thành các kí tự
    arr_chuoi_con = []
    chuoicon = ''
    dem = 0
    for c in arr_tach_chuoi:
        chuoicon += c  # cộng các ký tự lại với nhau
        if c == ' ':
            dem = dem + 1
        if dem == key:  # cộng cho tới khi có key khoảng trống
            dem = 0
            arr_chuoi_con.append(
                chuoicon)  # ta gắn chuỗi đó trở thành 1 phần tử của mảng arr_chuoi_con, ví dụ: ['nguyen thi hien ', 'vy hoc nganh ', 'cong nghe thong ', 'tin']
            chuoicon = ''  # reset chuỗi con trở thành chuỗi rỗng để bắt đầu cộng tiếp
    return arr_chuoi_con  # trả về mảng gần các chuỗi con gồm key khoảng trống


def dieu_kien():  # hàm kiểm tra xem văn bản dùng để giấu thông tin có ủ điều kiện để giấu thông điệp không
    a = len(tach_chuoi(cover_text))
    b = len(ma_hoa_thong_diep(ma))
    if a > b: # phải lớn hơn vì chuỗi cuối cùng k kiểm soát chuỗi cuối có mấy khoảng trống, nếu ít hơn2 th k thể giấu
        return 'True'
    else:
        return 'False'


def nhung(chuoi_nhi_phan=None, chuoi_con=None):  # nhúng các bit nhị phân vào văn bản
    dem = 0
    for n in chuoi_nhi_phan: # chạy vòng lặp cho đến khi giấu hết bit nhị phân
        if n == '0': # nếu là bit 0
            dem2 = 0
            dem3 = 0
            for c in chuoi_con[dem]:
                if c == ' ':
                    dem2 += 1
                if dem2 == 2: # nếu đến khoảng trống thứ 2 thì thêm khoảng trống
                    chuoi_con[dem] = chuoi_con[dem][:dem3] + ' ' + chuoi_con[dem][dem3:]
                    break # thêm xong thì dừng luôn không cần chạy tiếp trong chuỗi
                dem3 += 1 # cái này dùng để đếm xem trong chuỗi con mấy kí tự thì đến khoảng trống sau đó cắt ra ghép lại tại đó
        elif n == '1': # nếu là bit 1
            dem4 = 0
            for c in chuoi_con[dem]:
                if c == ' ': # bit 1 thì đến khoảng trống đầu tiên thì thêm khoảng trống luôn rồi dừng vòng lặp luôn
                    chuoi_con[dem] = chuoi_con[dem][:dem4] + ' ' + chuoi_con[dem][dem4:]
                    break
                dem4 += 1
        dem += 1
   # print(''.join(chuoi_con)) # print tại màn hình console vì khi in lên màn web các khoảng trống bị reset lại thành cách nhau bằng 1 khoảng trống, dùng thư viện jinja2 import Markup để giữ nhưng chưa import được
    return ''.join(chuoi_con) # trả về chuỗi con đã được giấu thông điệp

def gia_ma_nhi_phan(text=None, key=None):
    arr_chuoi_con_gm = tach_chuoi(text, key + 1)
    dem = 0
    stri = ''
    # lỗi từ đây
    for t in arr_chuoi_con_gm:
        dem1 = 0
        for c in t:
            if c == ' ':
                dem += 1
                if dem == 1 and t[dem1 + 1] == ' ':
                    stri = stri + '1'
                    break
                else:
                    stri = stri + '0'
                    break
            dem1 += 1
        dem = 0
    return stri

def gia_thong_diep(stri=None):
    s = []
    s1 = ''
    for i in stri:
        s1 += i
        if len(s1) == 8:
            s.append(int(s1, 2))
            s1 = ''
    print(s)
    return

# các hàm load data
def load_chuc_nang():
    return Chuc_nang.query.all()

# def load_file():

# kết thúc các hàm load data

