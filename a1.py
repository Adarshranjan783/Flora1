from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flora.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


@app.route('/retrieve/color', methods=['GET', 'POST'])
def retereve():
    if request.method=='POST':
        color = request.form['color']
        c=Flora.query.filter_by(color=color).count()
        if c > 0:

            #todo = Flora.query.filter_by(color=color).all()
            #return render_template('result.html', todo=todo)
            
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
        
    #todo = Flora.query.filter_by(sno=sno).first()
    #return render_template('result.html', todo=todo)

@app.route('/retrieve/type', methods=['GET', 'POST'])
def reterevetype():
    if request.method=='POST':
        type = request.form['type']
        f=Flora.query.filter_by(type=type).count()

        if f > 0:
            #todo = Flora.query.filter_by(type=type).all()
            #return render_template('result.html', todo=todo)
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
        
    #todo = Flora.query.filter_by(sno=sno).first()
    #return render_template('result.html', todo=todo)

@app.route('/retrieve/price', methods=['GET', 'POST'])
def retereveprice():
    if request.method=='POST':
        min = request.form['min']
        max = request.form['max']
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

        
    #todo = Flora.query.filter_by(sno=sno).first()
    #return render_template('result.html', todo=todo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        color = request.form['color']
        type = request.form['type']
        price = request.form['price']
        todo = Flora.query.filter_by(sno=sno).first()
        todo.color = color
        todo.type = type
        todo.price = price
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = Flora.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Flora.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)