from flask import Flask, request, jsonify

app = Flask(__name__)

# 用来存储数据的全局变量
received_data = []

@app.route('/post-data', methods=['POST'])
def post_data():
    data = request.get_json()  # 获取 JSON 数据
    print(data)  # 打印数据到控制台
    received_data.append(data)  # 将数据添加到列表中
    return jsonify({"message": "Data received"}), 200

@app.route('/show-data')
def show_data():
    return jsonify(received_data)  # 返回保存的数据

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
