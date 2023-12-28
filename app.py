from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json  # 获取JSON数据
    print(data)  # 打印数据到控制台，或进行其他处理
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)






