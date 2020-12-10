from flask import Flask, request, jsonify


app = Flask(__name__)


def main():
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)


@app.route("/movies")
def movies():
    query: str = request.args.get("q", request.args.get("query"))
    return f"{query.lower()}\n"


if __name__ == "__main__":
    main()
