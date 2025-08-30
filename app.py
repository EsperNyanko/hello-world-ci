from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return '<h1>Hello, World! from a CI/CD pipeline!</h1>'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
  
