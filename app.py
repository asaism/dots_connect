from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    notyet = 10
    processing = 20
    processed = 30
    done = 40
    total = 100

    return render_template('index.html',
                           total=total,
                           notyet=notyet,
                           processing=processing,
                           processed=processed,
                           done=done)


if __name__ == '__main__':
    app.run()
