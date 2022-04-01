from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Plots"

@app.route("/muestra-empresas")
def muestra_empresas():
    return render_template("muestra-empresas.html")

@app.route("/firms-falabella-mallplaza")
def firms_falabella_mallplaza():
    return render_template("firms-falabela-mallplaza.html")

@app.route("/firms-txd")
def firms_txd():
    return render_template("firms-TxD.html")

@app.route("/firms-hi")
def firms_hi():
    return render_template("firms-HI.html")

@app.route("/firms-sm")
def firms_sm():
    return render_template("firms-SM.html")

@app.route("/firms-ecommerce")
def firms_ecommerce():
    return render_template("firms-Ecommerce.html")

@app.route("/firms-mall")
def firms_mall():
    return render_template("firms-Mall.html")

@app.route("/firms-banco")
def firms_banco():
    return render_template("firms-Banco.html")

@app.route("/firms-digital")
def firms_digital():
    return render_template("firms-Digital.html")

if __name__ == "__main__":
    app.run(debug=True)