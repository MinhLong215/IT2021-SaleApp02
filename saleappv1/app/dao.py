from app.models import Category, Product



def load_categories():
    return Category.query.all()
    # return [{
    #     'id' :  1,
    #     'name' : 'Mobile'
    # }, {
    #     'id' :  1,
    #     'name' : 'Tablet'
    # }]

def load_products(kw=None):
    products = [{
        "id": 1,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg"
    },{
        "id": 2,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg"
    },{
        "id": 1,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg"
    },{
        "id": 1,
        "name": "Ipad Pro Max",
        "price": 30000000,
        "image": "https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg"
    },{
        "id": 1,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.tgdd.vn//News/1546949//tong-hop-hinh-nen-iphone-15-pro-max-4k-iphone-15(5)-800x450.jpg"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products