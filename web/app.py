from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)
FORBIDDEN_STR = ('~','//','..')

@app.route("/<path:path>")
def returning(path):
    if any(word in path for word in FORBIDDEN_STR) or path.startswith('/'):
        abort(403)
    try:
        return render_template(path), 200
    except TemplateNotFound:
        abort(404)

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error_403(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
