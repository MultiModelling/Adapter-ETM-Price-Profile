from dataclasses import dataclass
from typing import Optional

import requests

from tno.etm_price_profile_adapter.model.model import Model, ModelState
from tno.etm_price_profile_adapter.types import ETMAdapterConfig, ModelRunInfo


class ETM(Model):

    def process_results(self, result):
        if self.minio_client:
            return result
        else:
            curve_lines_str = result.split('\n')
            curve_lines = [line.split(',') for line in curve_lines_str]
            curve_lines.pop(0)
            if curve_lines[-1] == ['']:
                curve_lines.pop(-1)
            curve_values = [[v[0], float(v[1])] for v in curve_lines]
            return curve_values

    def run(self, model_run_id: str):
        res = Model.run(self, model_run_id=model_run_id)

        if model_run_id in self.model_run_dict:
            config: ETMAdapterConfig = self.model_run_dict[model_run_id].config

            url = config.etm_config.endpoint + config.etm_config.path.format(config.etm_config.scenario_ID)
            response = requests.get(url)

            if response.ok:
                curve_str = response.text
                model_run_info = Model.store_result(self, model_run_id=model_run_id, result=curve_str)
                return model_run_info
            else:
                return ModelRunInfo(
                    model_run_id=model_run_id,
                    state=ModelState.ERROR,
                    reason=f"Error in ETM.run(): ETM API returned: {response.status_code} {response.reason}"
                )
        else:
            return ModelRunInfo(
                model_run_id=model_run_id,
                state=ModelState.ERROR,
                reason="Error in ETM.run(): model_run_id unknown"
            )

