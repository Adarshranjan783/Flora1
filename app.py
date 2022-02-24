from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flora.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cache.init_app(app)



db = SQLAlchemy(app)
ma = Marshmallow(app)

class Flora(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.color}- {self.type}- {self.price}"


class UserSchema(ma.Schema):
    class Meta:
        fields = ("color", "type", "price")

#@app.route('/')
#def index():
#    users = Flora.query.all()
#    user_schema = UserSchema(many=True)
#    output = user_schema.dump(users).data
#    return jsonify({'user' : output})


@app.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def hello_world():
    if request.method=='POST':
        color = request.form['color']
        type = request.form['type']
        price = request.form['price']
        flora = Flora(color=color, type=type, price=price)
        db.session.add(flora)
        db.session.commit()
        
    floralist = Flora.query.all()
    return render_template('index.html', floralist=floralist)


@app.route('/retrieve', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def select():
    if request.method=='POST':
        color = request.form['color']
        type = request.form['type']
        price = request.form['price']
        flora = Flora(color=color, type=type, price=price)
        db.session.add(flora)
        db.session.commit()
        
    floralist = Flora.query.all() 
    return render_template('retrieve.html', floralist=floralist)


@app.route('/retrieve/color/<string:color>')
def retereve1(color):

    c=Flora.query.filter_by(color=color).count()
    if c > 0:

        #flower = Flora.query.filter_by(color=color).all()
        #return render_template('result.html', flower=flower)
            
        user_schema = UserSchema()
        user_schema = UserSchema(many=True)
        users = Flora.query.filter_by(color=color).all()
        output = user_schema.dump(users)
        print(output)
        return jsonify({'flower' : output})
        
    else:
        #floralist = Flora.query.all() 
        #return render_template('noresult.html', floralist=floralist)
        user_schema = UserSchema()
        user_schema = UserSchema(many=True)
        users = Flora.query.all() 
        output = user_schema.dump(users)
        print(output)
        return jsonify({'flower' : output})

@app.route('/retrieve/color', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def retereve():
    if request.method=='POST':
        color = request.form['color']
        return redirect(f"/retrieve/color/{color}")
        

@app.route('/retrieve/type/<string:type>')
def reterevetype2(type):

    c=Flora.query.filter_by(type=type).count()
    if c > 0:

        #flower = Flora.query.filter_by(color=color).all()
        #return render_template('result.html', flower=flower)
            
        user_schema = UserSchema()
        user_schema = UserSchema(many=True)
        users = Flora.query.filter_by(type=type).all()
        output = user_schema.dump(users)
        print(output)
        return jsonify({'flower' : output})
        
    else:
        #floralist = Flora.query.all() 
        #return render_template('noresult.html', floralist=floralist)
        user_schema = UserSchema()
        user_schema = UserSchema(many=True)
        users = Flora.query.all() 
        output = user_schema.dump(users)
        print(output)
        return jsonify({'flower' : output})

@app.route('/retrieve/type', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def reterevetype():
    if request.method=='POST':
        type = request.form['type']
        return redirect(f"/retrieve/type/{type}")


@app.route('/retrieve/price/<int:min>/<int:max>')
def reterevepric2(min,max):

    c=Flora.query.filter(Flora.price <= max).\
            filter(Flora.price >= min).count()
    m = Flora.query.filter(Flora.price <= max).\
            filter(Flora.price >= min).count()
    if m > 0:
        #todo =Flora.query.filter(Flora.price <= max).\
        #filter(Flora.price >= min).all()
        #return render_template('result.html', todo=todo)
        user_schema = UserSchema()
        user_schema = UserSchema(many=True)
        users = Flora.query.filter(Flora.price <= max).\
        filter(Flora.price >= min).all()
        output = user_schema.dump(users)
        print(output)
        return jsonify({'flower' : output})


    else:
        #floralist = Flora.query.all() 
        #return render_template('noresult.html', floralist=floralist)
        user_schema = UserSchema()
        user_schema = UserSchema(many=True)
        users = Flora.query.all() 
        output = user_schema.dump(users)
        print(output)
        return jsonify({'flower' : output})

@app.route('/retrieve/price', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def retereveprice():
    if request.method=='POST':
        min = request.form['min']
        max = request.form['max']
        return redirect(f"/retrieve/price/{min}/{max}")

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        color = request.form['color']
        type = request.form['type']
        price = request.form['price']
        update = Flora.query.filter_by(sno=sno).first()
        update.color = color
        update.type = type
        update.price = price
        db.session.add(update)
        db.session.commit()
        return redirect("/")
        
    update = Flora.query.filter_by(sno=sno).first()
    return render_template('update.html', update=update)

@app.route('/delete/<int:sno>')
def delete(sno):
    update = Flora.query.filter_by(sno=sno).first()
    db.session.delete(update)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
