from flask import Flask,render_template,jsonify,request,redirect,url_for

app = Flask(__name__)

user = [{"name":"Deepak","Age":20,"Grade":"2024-09-09 12:00:00"},{"name":"Raj","Age":21,"Grade":8.7}]

@app.route('/get_details',methods=['GET'])
def get_details():
    return jsonify(user),200

@app.route('/get_details/<name>',methods=['GET'])
def get_specific_id(name):
    try:
        spec_user = next((i for i in user if i['name'] == name),None)
        return jsonify(spec_user)
    except Exception as e:
        return jsonify(e)
    

@app.route('/post_details',methods = ['POST'])
def post_details():
    new_data = request.get_json()
    
    if 'name' not in new_data or 'age' not in new_data:
        return jsonify('You have missed either one of col')
    user.append(new_data)
    return jsonify(user),201

@app.route('/update_details<name>',methods=['PUT'])
def update_details():
    is_name = user.query.filter_by(id=id).first()
    if is_name:
        update_data = request.get_json()
        user.name = update_data["name"]
        user.Age = update_data["Age"]
        user.Grade = update_data["Grade"]
    return jsonify(user)

@app.route('/<name>')
def add_name(name):
    return render_template('welcome.html',name=name)

@app.route('/')
def index():
    return redirect(url_for('contact'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)