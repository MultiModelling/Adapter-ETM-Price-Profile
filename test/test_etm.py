from tno.etm_price_profile_adapter.model.etm import ETM, ETMConfig

config = ETMConfig(
    endpoint="https://engine.energytransitionmodel.com/api/v3/",
    path="scenarios/{}/curves/electricity_price.csv",
    scenario_ID="763305"
)

etm = ETM(config=config)
result = etm.call()

print(result)