# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,request,session,jsonify

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

app.secret_key = 'Prash2610'
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def getData():
    # import contactGeneration as cg

    # Final=cg.contactGenerate(500,9000)
    # print(Final)
    return render_template('index.html')
# ‘/’ URL is bound with hello_world() function.
Final_Wh=list()
# @app.route('/handle_data', methods=['POST','GET'])
# def handle_data():
#     minPrice = request.form['minPrice']
#     maxPrice = request.form['maxPrice']

#     headings=('','NAME','MOBILE NO','OUTSTANDING')
#     import contactGeneration as cg
#     Final=cg.contactGenerate(int(minPrice),int(maxPrice))
#     # print(Final)
#     session['data']=Final
#     return render_template('index.html',headings=headings,FinalResult=Final)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    data=request.get_json()
    print(data)
    import contactGeneration as cg
    Final=cg.contactGenerate(int(data[0]["minPrice"]),int(data[1]["maxPrice"]))
    # print(int(data[0]["minPrice"]),int(data[1]["maxPrice"]))
    # print(Final)
    session['data']=Final
    return jsonify(list_data=Final)


    # minPrice = request.form['minPrice']
    # maxPrice = request.form['maxPrice']

    # headings=('','NAME','MOBILE NO','OUTSTANDING')
    # import contactGeneration as cg
    # Final=cg.contactGenerate(int(minPrice),int(maxPrice))
    # # print(Final)
    # session['data']=Final
    # return render_template('index.html',headings=headings,FinalResult=Final)

@app.route('/my-flask-endpoint', methods=['POST'])
def my_flask_endpoint():
    my_list = request.json['my_list']
    print("List received from client:", my_list)
    data=session.get('data')
    for i in my_list:
         print(data[int(i)-1])
    # process the list as needed
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

# @app.route("/<name>")
# def welcome(name):
#     return render_template("index.html", name=name)
 
 
# @app.route('', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=user))
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
