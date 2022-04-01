from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Plots"

@app.route("/muestra-empresas")
def muestra_empresas():
    return render_template("muestra-empresas.html")

# FALABELLA y MP

@app.route("/portfolio-falabella-mallplaza-c-re")
def portfolio_falabella_mallplaza_c_re():
    return render_template("portfolio-falabella-mallplaza-c-re.html")

@app.route("/portfolio-falabella-mallplaza-s-re")
def portfolio_falabella_mallplaza_s_re():
    return render_template("portfolio-falabella-mallplaza-s-re.html")

@app.route("/firms-falabella-mallplaza")
def firms_falabella_mallplaza():
    return render_template("firms-falabella-mallplaza.html")

# TxD

@app.route("/portfolio-txd-c-re")
def portfolio_txd_c_re():
    return render_template("portfolio-TxD-c-re.html")

@app.route("/portfolio-txd-s-re")
def portfolio_txd_s_re():
    return render_template("portfolio-TxD-s-re.html")

@app.route("/firms-txd")
def firms_txd():
    return render_template("firms-TxD.html")

# HI

@app.route("/portfolio-hi-c-re")
def portfolio_hi_c_re():
    return render_template("portfolio-HI-c-re.html")

@app.route("/portfolio-hi-s-re")
def portfolio_hi_s_re():
    return render_template("portfolio-HI-s-re.html")

@app.route("/firms-hi")
def firms_hi():
    return render_template("firms-HI.html")

# SM

@app.route("/portfolio-sm-c-re")
def portfolio_sm_c_re():
    return render_template("portfolio-SM-c-re.html")

@app.route("/portfolio-sm-s-re")
def portfolio_sm_s_re():
    return render_template("portfolio-SM-s-re.html")

@app.route("/firms-sm")
def firms_sm():
    return render_template("firms-SM.html")

# Ecommerce

@app.route("/portfolio-ecommerce-c-re")
def portfolio_ecommerce_c_re():
    return render_template("portfolio-Ecommerce-c-re.html")

@app.route("/portfolio-ecommerce-s-re")
def portfolio_ecommerce_s_re():
    return render_template("portfolio-Ecommerce-s-re.html")

@app.route("/firms-ecommerce")
def firms_ecommerce():
    return render_template("firms-Ecommerce.html")

# Mall

@app.route("/portfolio-mall-c-re")
def portfolio_mall_c_re():
    return render_template("portfolio-Mall-c-re.html")

@app.route("/portfolio-mall-s-re")
def portfolio_mall_s_re():
    return render_template("portfolio-Mall-s-re.html")

@app.route("/firms-mall")
def firms_mall():
    return render_template("firms-Mall.html")

# Banco

@app.route("/portfolio-banco-c-re")
def portfolio_banco_c_re():
    return render_template("portfolio-Banco-c-re.html")

@app.route("/portfolio-banco-s-re")
def portfolio_banco_s_re():
    return render_template("portfolio-Banco-s-re.html")

@app.route("/firms-banco")
def firms_banco():
    return render_template("firms-Banco.html")

# Digital

@app.route("/portfolio-digital-c-re")
def portfolio_digital_c_re():
    return render_template("portfolio-Digital-c-re.html")

@app.route("/portfolio-digital-s-re")
def portfolio_digital_s_re():
    return render_template("portfolio-Digital-s-re.html")

@app.route("/firms-digital")
def firms_digital():
    return render_template("firms-Digital.html")

if __name__ == "__main__":
    app.run(debug=True)