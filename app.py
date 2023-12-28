from flask import Flask, request, jsonify

app = Flask(__name__)

# 用来存储数据的全局变量
received_data = []

@app.route('/post-data', methods=['POST'])
def post_data():
    data = request.form.to_dict()  # 获取表单数据
    received_data.append(data)  # 将数据添加到列表中
    # 返回一个简单的HTML页面，显示接收到的数据
    return f"<html><body><h1>Received Data:</h1><pre>{data}</pre></body></html>", 200

@app.route('/show-data')
def show_data():
    # 以HTML格式返回所有接收到的数据
    data_html = '<br>'.join([str(data) for data in received_data])
    return f"<html><body><h1>Received Data:</h1><pre>{data_html}</pre></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
