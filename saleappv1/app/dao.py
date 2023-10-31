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
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    },{
        "id": 2,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    },{
        "id": 1,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    },{
        "id": 1,
        "name": "Ipad Pro Max",
        "price": 30000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    },{
        "id": 1,
        "name": "Iphone 15 Pro Max",
        "price": 30000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products