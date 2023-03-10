from flask import Flask
import utils

app = Flask(__name__)

@app.route("/")
def index():
    candidates = utils.get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_by_pk(pk)
    if not candidate:
        return 'Кандидат не найден'

    result = f"<img src=\"{candidate['picture']}\">"
    result += '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return f'<pre> {result} </pre>'

@app.route("/candidate/<skill>")
def get_candidate_by_skill(skill):
    candidates = utils.get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'

if __name__ == '__main__':
    app.run(debug=True)
