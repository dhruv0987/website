from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/gge")
def gge():
    return "if you are seeing this message then we have hacked your account and going to take 1 lakh"

@app.route("/<name>")
def user(name):
	return render_template("base.html",name=name)

@app.route("/admin")	
def admin():
	return redirect(url_for("user", name="Admin!"))
@app.route("/")
def home():
	return render_template("base.html")
@app.route("/blog")
def blog():
	return render_template("blog.html")	
			
if __name__=="__main__":
    app.run(debug=True)
    
