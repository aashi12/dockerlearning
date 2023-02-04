from flask import  Flask
import  redis


app= Flask(__name__)

@app.route('/getdata')
def getname():
    response = "Hello, Wworld!"
    rcache=redis.Redis(host='myredis',port=6379,db=0)
    rcache.lpush("namee","helloworld")
    print(rcache.lrange("namee",0,-1))
    return  response
if __name__ == "__main__":
    app.run(port=5001)