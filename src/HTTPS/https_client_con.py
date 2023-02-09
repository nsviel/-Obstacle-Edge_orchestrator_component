#---------------------------------------------
from src.param import param_hu
from src.HTTPS import https_client_fct
from src.HTTPS import https_client_post
from src.misc import connection
from src.misc import terminal


#Test Velodium HTTP connection
def test_ve_con():
    [ip, port, connected] = https_client_fct.network_info("ve")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_ve_con.hu_has_been_deco):
        test_ve_con.hu_has_been_co = True
        test_ve_con.hu_has_been_deco = False
        terminal.addConnection("ve", "on")
        param_hu.state_hu["velodium"]["http_connected"] = True
    elif(connected == False and test_ve_con.hu_has_been_co):
        test_ve_con.hu_has_been_co = False
        test_ve_con.hu_has_been_deco = True
        terminal.addConnection("ve", "off")
        param_hu.state_hu["velodium"]["http_connected"] = False

test_ve_con.hu_has_been_co = False
test_ve_con.hu_has_been_deco = True

#Test AI HTTP connection
def test_ai_con():
    [ip, port, connected] = https_client_fct.network_info("ai")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_ai_con.hu_has_been_deco):
        test_ai_con.hu_has_been_co = True
        test_ai_con.hu_has_been_deco = False
        terminal.addConnection("ve", "on")
        param_hu.state_hu["ai"]["http_connected"] = True
    elif(connected == False and test_ai_con.hu_has_been_co):
        test_ai_con.hu_has_been_co = False
        test_ai_con.hu_has_been_deco = True
        terminal.addConnection("ve", "off")
        param_hu.state_hu["ai"]["http_connected"] = False

test_ai_con.hu_has_been_co = False
test_ai_con.hu_has_been_deco = True

#Test Pywardium HTTP connection
def test_py_con():
    [ip, port, connected] = https_client_fct.network_info("py")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_py_con.hu_has_been_deco):
        test_py_con.hu_has_been_co = True
        test_py_con.hu_has_been_deco = False
        terminal.addConnection("py", "on")
        connection_py_open()
    elif(connected == False and test_py_con.hu_has_been_co):
        test_py_con.hu_has_been_co = False
        test_py_con.hu_has_been_deco = True
        terminal.addConnection("py", "off")
        connection_py_close()

test_py_con.hu_has_been_co = False
test_py_con.hu_has_been_deco = True

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
    if(connected == True and test_ed_con.hu_has_been_deco):
        test_ed_con.hu_has_been_co = True
        test_ed_con.hu_has_been_deco = False
        terminal.addConnection("ve", "on")
        connection_ed_open()
    elif(connected == False and test_ed_con.hu_has_been_co):
        test_ed_con.hu_has_been_co = False
        test_ed_con.hu_has_been_deco = True
        terminal.addConnection("ve", "off")
        connection_ed_close()

test_ed_con.hu_has_been_co = False
test_ed_con.hu_has_been_deco = True

def connection_ed_open():
    param_hu.state_hu["edge"]["http_connected"] = True

def connection_ed_close():
    param_hu.state_hu["edge"]["http_connected"] = False
    param_hu.state_hu["edge"]["sock_l1_connected"] = False
    param_hu.state_hu["edge"]["sock_l2_connected"] = False
