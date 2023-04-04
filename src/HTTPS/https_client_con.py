#---------------------------------------------
from src.param import param_edge
from src.HTTPS import https_client_fct
from src.HTTPS import https_client_post
from src.misc import connection
from src.misc import terminal


#Test Velodium HTTP connection
def test_processing_con():
    [ip, port, connected] = https_client_fct.network_info("processing")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_processing_con.edge_has_been_deco):
        test_processing_con.edge_has_been_co = True
        test_processing_con.edge_has_been_deco = False
        terminal.addConnection("processing", "on")
        param_edge.state_edge["component_process"]["http_connected"] = True
    elif(connected == False and test_processing_con.edge_has_been_co):
        test_processing_con.edge_has_been_co = False
        test_processing_con.edge_has_been_deco = True
        terminal.addConnection("processing", "off")
        param_edge.state_edge["component_process"]["http_connected"] = False

test_processing_con.edge_has_been_co = False
test_processing_con.edge_has_been_deco = True

#Test AI HTTP connection
def test_ai_con():
    [ip, port, connected] = https_client_fct.network_info("component_ai")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_ai_con.edge_has_been_deco):
        test_ai_con.edge_has_been_co = True
        test_ai_con.edge_has_been_deco = False
        terminal.addConnection("processing", "on")
        param_edge.state_edge["component_ai"]["http_connected"] = True
    elif(connected == False and test_ai_con.edge_has_been_co):
        test_ai_con.edge_has_been_co = False
        test_ai_con.edge_has_been_deco = True
        terminal.addConnection("processing", "off")
        param_edge.state_edge["component_ai"]["http_connected"] = False

test_ai_con.edge_has_been_co = False
test_ai_con.edge_has_been_deco = True

#Test module_capture HTTP connection
def test_capture_con():
    [ip, port, connected] = https_client_fct.network_info("capture")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_capture_con.edge_has_been_deco):
        test_capture_con.edge_has_been_co = True
        test_capture_con.edge_has_been_deco = False
        terminal.addConnection("capture", "on")
        connection_capture_open()
    elif(connected == False and test_capture_con.edge_has_been_co):
        test_capture_con.edge_has_been_co = False
        test_capture_con.edge_has_been_deco = True
        terminal.addConnection("capture", "off")
        connection_capture_close()

test_capture_con.edge_has_been_co = False
test_capture_con.edge_has_been_deco = True

def connection_capture_open():
    param_edge.state_edge["module_capture"]["http_connected"] = True
    https_client_post.post_param_value("capture", "module_edge", "ip", param_edge.state_edge["self"]["ip"])

def connection_capture_close():
    param_edge.state_edge["module_capture"]["http_connected"] = False
    param_edge.state_edge["module_capture"]["sock_l1_connected"] = False
    param_edge.state_edge["module_capture"]["sock_l2_connected"] = False

#Test module_capture HTTP connection
def test_ed_con():
    [ip, port, connected] = https_client_fct.network_info("edgenext")
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected == True and test_ed_con.edge_has_been_deco):
        test_ed_con.edge_has_been_co = True
        test_ed_con.edge_has_been_deco = False
        terminal.addConnection("processing", "on")
        connection_ed_open()
    elif(connected == False and test_ed_con.edge_has_been_co):
        test_ed_con.edge_has_been_co = False
        test_ed_con.edge_has_been_deco = True
        terminal.addConnection("processing", "off")
        connection_ed_close()

test_ed_con.edge_has_been_co = False
test_ed_con.edge_has_been_deco = True

def connection_ed_open():
    param_edge.state_edge["edge_next"]["http_connected"] = True

def connection_ed_close():
    param_edge.state_edge["edge_next"]["http_connected"] = False
    param_edge.state_edge["edge_next"]["sock_l1_connected"] = False
    param_edge.state_edge["edge_next"]["sock_l2_connected"] = False