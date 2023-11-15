from flask import Flask, render_template
from app import app
from app import utils
from app import models

# from jinja2 import Markup

text = models.cover_texts
ma = models.message

# methods=['POST']
@app.route('/')
def home():
    b = utils.ma_hoa_thong_diep(ma)
    # dk = utils.dieu_kien()
    #
    # if dk == 'True':
    c = utils.tach_chuoi(text, key=3)
    e = utils.nhung(chuoi_nhi_phan=b, chuoi_con=c)
    f = utils.gia_ma_nhi_phan(text=e, key=3)
    utils.gia_thong_diep(f)
    # gọi hàm lấy data chức năng header
    chuc_nang = utils.load_chuc_nang()
    return render_template('index.html', b=b, c=c, e=e, chuc_nang=chuc_nang)


if __name__ == '__main__':
    app.run(debug=True)
