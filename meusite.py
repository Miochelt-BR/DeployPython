from flask import Flask,render_template

app = Flask(__name__)
#decoreitory uma nova funcionalidade para funcao 
@app.route("/")
def homepage():
    return render_template ("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template ("contatos.html")


#criando um router dinamico para receber nomes do usuario pagina dinamica 
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return  render_template("usuarios.html",nome_usuario=nome_usuario)
    
    
if __name__ == "__main__":
   app.run(debug=True)