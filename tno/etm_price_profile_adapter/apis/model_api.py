from flask import jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from tno.shared.log import get_logger
from tno.etm_price_profile_adapter.types import ModelRunInfo, ETMAdapterConfig
from tno.etm_price_profile_adapter.model.etm import ETM


etm = ETM()

logger = get_logger(__name__)

api = Blueprint("model", "model", url_prefix="/model")


@api.route("/request")
class Request(MethodView):

    @api.response(200, ModelRunInfo.Schema())
    def get(self):
        res = etm.request()
        return jsonify(res)


@api.route("/initialize/<model_run_id>")
class Initialize(MethodView):

    @api.arguments(ETMAdapterConfig.Schema())
    @api.response(201, ModelRunInfo.Schema())
    def post(self, config, model_run_id: str):
        res = etm.initialize(model_run_id=model_run_id, config=config)
        return jsonify(res)


@api.route("/run/<model_run_id>")
class Run(MethodView):

    @api.response(200, ModelRunInfo.Schema())
    def get(self, model_run_id: str):
        res = etm.run(model_run_id=model_run_id)
        return jsonify(res)


@api.route("/status/<model_run_id>")
class Status(MethodView):

    @api.response(200, ModelRunInfo.Schema())
    def get(self, model_run_id: str):
        res = etm.status(model_run_id=model_run_id)
        return jsonify(res)


@api.route("/results/<model_run_id>")
class results(MethodView):

    @api.response(200, ModelRunInfo.Schema())
    def get(self, model_run_id: str):
        res = etm.results(model_run_id=model_run_id)
        return jsonify(res)


@api.route("/remove/<model_run_id>")
class remove(MethodView):

    @api.response(200, ModelRunInfo.Schema())
    def get(self, model_run_id: str):
        etm.remove(model_run_id=model_run_id)
        return "REMOVED!", 200
