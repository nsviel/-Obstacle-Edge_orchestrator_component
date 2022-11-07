#---------------------------------------------
from param import param_hu
from src import parser_json


def format_state_kpi():
    # Load kpi state file
    param_hu.state_kpi = parser_json.load_data_from_file(param_hu.path_state_kpi)

    # Add values
    param_hu.state_kpi["uplink_data_rate_Mbs"] = param_hu.state_perf["local_cloud"]["bandwidth"]["value"]
    param_hu.state_kpi["downlink_data_rate_Mbs"] = param_hu.state_perf["cloud_local"]["bandwidth"]["value"]

    param_hu.state_kpi["uplink_cloud_end_to_end_latency_ms"] = param_hu.state_perf["local_cloud"]["latency"]["value"]
    param_hu.state_kpi["downlink_cloud_end_to_end_latency_ms"] = param_hu.state_perf["cloud_local"]["latency"]["value"]

    param_hu.state_kpi["uplink_reliability_%"] = param_hu.state_perf["local_cloud"]["reliability"]["value"]
    param_hu.state_kpi["downlink_reliability_%"] = param_hu.state_perf["cloud_local"]["reliability"]["value"]

    param_hu.state_kpi["mobility_interruption_time_s"] = param_hu.state_perf["local_cloud"]["interruption"]["value"]
    param_hu.state_kpi["time_for_service_warning_ms"] = param_hu.state_perf["end_to_end"]["time_total"]

    # Upload kpi state file
    parser_json.upload_file(param_hu.path_state_kpi, param_hu.state_kpi)
