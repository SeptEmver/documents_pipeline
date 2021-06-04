import os
import json
import traceback
from flask import Flask, render_template, request, flash, send_from_directory, jsonify

from tools.ExceptionsWithCodes import RequestError
from main import handle_multi_doc

# максимальный размер .tiff 2**32 байта, ограничим до 200 мб
MAX_FILE_SIZE = 200 * 1024 * 1024

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


@app.route("/", methods=["GET"])
def main_page():
    return render_template("main_page.html")


@app.route("/", methods=["POST"])
def upload_doc():
    try:
        file = request.files["document"]
        result = json.dumps(handle_multi_doc(file), indent=4) #, sort_keys=True
        return render_template("main_page.html", args={"result_json": result})
    except RequestError as e:
        flash(str(e), category="error")
        return render_template("main_page.html"), e.get_status_code()
    except Exception as e:
        flash(traceback.format_exc(), category="error")
        return render_template("main_page.html"), 500


# api rjnjhjuj ytn
# api = Api(app)
# api.route(PersonList, 'person_list', '/persons')
# @app.route("/api/v1/all_tasks", methods=["POST"])
# def api_get_all_tasks_json():
#     try:
#         file = request.files["document"]
#         return jsonify(handle_multi_doc(file))
#     except RequestError as e:
#         return jsonify({"exception": str(e)}), e.get_status_code()
#     except Exception as e:
#         return jsonify({"exception": str(e), "traceback": traceback.format_exc()}), 500


# @app.route("/api/v1/task_1", methods=["POST"])
# def handle_task_1():
#     return


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=True)
