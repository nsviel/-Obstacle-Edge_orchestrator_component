#---------------------------------------------
from param import param_hu
from HTTPS import https_client_fct
from HTTPS import https_client_post


#Test Velodium HTTP connection
def test_ve_con():
    [ip, port, connected] = https_client_fct.network_info("ve")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        param_hu.state_hu["velodium"]["http_connected"] = True
    else:
        param_hu.state_hu["velodium"]["http_connected"] = False

#Test AI HTTP connection
def test_ai_con():
    [ip, port, connected] = https_client_fct.network_info("ai")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        param_hu.state_hu["ai"]["http_connected"] = True
    else:
        param_hu.state_hu["ai"]["http_connected"] = False

#Test Pywardium HTTP connection
def test_py_con():
    [ip, port, connected] = https_client_fct.network_info("py")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_py_open()
    else:
        connection_py_close()

def connection_py_open():
    param_hu.state_hu["pywardium"]["http_connected"] = True
    https_client_post.post_param_value("py", "hubium", "ip", param_hu.state_hu["self"]["ip"])

def connection_py_close():
    param_hu.state_hu["pywardium"]["http_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l1_connected"] = False
    param_hu.state_hu["pywardium"]["sock_l2_connected"] = False

#Test Pywardium HTTP connection
def test_ed_con():
    [ip, port, connected] = https_client_fct.network_info("ed")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_ed_open()
    else:
        connection_ed_close()

def connection_ed_open():
    param_hu.state_hu["edge"]["http_connected"] = True

def connection_ed_close():
    param_hu.state_hu["edge"]["http_connected"] = False
    param_hu.state_hu["edge"]["sock_l1_connected"] = False
    param_hu.state_hu["edge"]["sock_l2_connected"] = False
