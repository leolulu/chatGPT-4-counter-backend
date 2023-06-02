from flask import Flask, request
from flask_cors import CORS
from model.status import ChatGPTStatus

from utils.env_util import get_env_var

app = Flask(__name__)
CORS(app)  # 这将使所有路由都支持跨域请求

cs = ChatGPTStatus()

@app.route('/usage_audit', methods=['POST'])
def usage_audit():
    data = request.get_json()
    action_type = data['action_type']
    if action_type == 'report_new_submit':
        cs.receive_new_request()
    elif action_type == 'query_status':
        pass # TODO: cover只查数据不记录的情况
    # TODO: 增加持久化日志的功能，以便于以后进行行为数据分析
    return cs.get_usage_status(), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(get_env_var('PORT', 5000)))
