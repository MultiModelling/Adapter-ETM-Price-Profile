from tno.etm_price_profile_adapter.model.etm import ETM
from tno.etm_price_profile_adapter.types import ETMConfig, ETMAdapterConfig

etm_config = ETMConfig(
    endpoint="https://engine.energytransitionmodel.com/api/v3/",
    path="scenarios/{}/curves/electricity_price.csv",
    scenario_ID="763305"
)

etm_adapter_config = ETMAdapterConfig(
    etm_config=etm_config,
    # output_file_path=None,
    # base_path=None,
)

etm = ETM()
model_run_info = etm.request()
model_run_info = etm.initialize(model_run_id=model_run_info.model_run_id, config=etm_adapter_config)
model_run_info = etm.run(model_run_id=model_run_info.model_run_id)
model_run_info = etm.results(model_run_id=model_run_info.model_run_id)

result = model_run_info.result
print(result)