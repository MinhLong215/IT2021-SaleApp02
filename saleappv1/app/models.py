from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    from app import app
    with app.app_context():
        # c1 = Category(name='Ipad')
        # c2 = Category(name='Iphone')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='iPad Pro 2022', price=24000000,
                     image="https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg", category_id=2)
        p2 = Product(name='iPhone 13', price=21000000,
                     image="https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg", category_id=1)
        p3 = Product(name='Galaxy S24', price=24000000,
                     image="https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg", category_id=1)
        p4 = Product(name='Note 22', price=22000000,
                     image="https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg", category_id=1)
        p5 = Product(name='Galaxy Tab S10', price=24000000,
                     image="https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg", category_id=2)

        db.session.add_all([p1,p2,p3,p4,p5])
        db.session.commit()

        # db.create_all()



