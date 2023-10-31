from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    datos = request.form
    first_name = datos["first_name"]
    last_name = datos["last_name"]
    strawberry = int(datos["strawberry"])
    apple = int(datos["apple"])
    raspberry = int(datos["raspberry"])
    total_fruits = strawberry + apple + raspberry
    print(f"Cobrando a {first_name}{last_name} por {total_fruits} frutas")
    return render_template("checkout.html", datos=datos)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    