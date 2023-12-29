from flask import Flask, request, jsonify

app = Flask(__name__)

# 用来存储数据的全局变量
received_data = []

@app.route('/post-data', methods=['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        data = request.form.to_dict()  # 获取表单数据
        received_data.append(data)  # 将数据添加到列表中
        return f"<html><body><h1>Received Data:</h1><pre>{data}</pre></body></html>", 200
    else:
        # 返回一个简单的表单，用于提交数据
        return '''
            <html>
                <body>
                    <form method="post" action="/post-data">
                        Data: <input type="text" name="data"><br>
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>
        '''

@app.route('/show-data')
def show_data():
    # 以HTML格式返回所有接收到的数据
    data_html = '<br>'.join([str(data) for data in received_data])
    return f"<html><body><h1>Received Data:</h1><pre>{data_html}</pre></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

