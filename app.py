import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  print('Hello world from console')
  return 'Hello from the other side of docker!'

# Im editing in github as well
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
