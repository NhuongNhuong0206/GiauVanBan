message = 'hien vy'
cover_texts = 'What is Love I know this question exists in each human being’s mind including myself. If not it is still waiting to be discovered deeply in your heart. What do I think of love For me, I believe love is a priceless diamond, because a diamond has thousands of reflections, and each reflection represents a meaning of love. Love is patient, love is kind, and everlasting. With love I can accept a person’s imperfections without any condition, and able to transfer the way I love myself to another person who I am fancy at. With love I can have the power against loneliness, sadness, and illness, and to be able to change them into my happiness. As well as, having a key to open my heart to look at this world without a mask, to show people who I really am. Perhaps love is like religion- something we just need to believe in to have, or achieve. Perhaps it is just a thought. If we feel it in our hearts and believe it in our souls, then just maybe it will be there to feel and cherish. What will happen if people live without love In my point of view, without love I may lose my ability to survive in this world with no hope. Without love I can be defined as a rat living in the sewer, with no chance to see our beautiful land and with no chance to lighten up myself against the darkness. As well as, I may lose many opportunities of enjoyment both mentally and physically, when I do not know what love is.'

from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean
from app import app
from app import db


class khoa(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Chuc_nang(khoa):
    __tablename__ = 'chuc_nang'
    name = Column(String(20), nullable=True)

    def __str__(self):
        return self.name


class file(khoa):
    __tablename__ = 'file'
    name = Column(String(255), nullable=True)
    noi_dung = Column(String(500))

    def __str__(self):
        return self.name




if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        cn1 = Chuc_nang(name='Trang chủ')
        cn2 = Chuc_nang(name='Thư viện')
        cn3 = Chuc_nang(name='Đã gửi')
        cn4 = Chuc_nang(name='Đã nhận')
        db.session.add(cn1)
        db.session.add(cn2)
        db.session.add(cn3)
        db.session.add(cn4)

        db.session.commit()
