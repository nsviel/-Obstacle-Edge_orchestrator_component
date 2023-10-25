#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS.client import https_client_fct
from src.connection.HTTPS.client import https_client_post
from src.connection import connection
from src.utils import parser_json
from src.utils import terminal


#Test Ground http connection
def test_connection_ground():
    [ip, port, connected] = https_client_fct.network_info("ground")
    connected = https_client_fct.send_https_ping(ip, port)
    param_edge.state_edge["interface"]["capture"]["http_connected"] = connected

    if(connected == True and test_connection_ground.edge_has_been_deco):
        test_connection_ground.edge_has_been_co = True
        test_connection_ground.edge_has_been_deco = False
        terminal.addConnection("ground", "on")
        https_client_post.post_state_ground("ground", param_edge.state_ground)
        https_client_post.post_state_ground("edge", param_edge.state_edge)
    elif(connected == False and test_connection_ground.edge_has_been_co):
        test_connection_ground.edge_has_been_co = False
        test_connection_ground.edge_has_been_deco = True
        terminal.addConnection("ground", "off")
        param_edge.state_ground["capture"]["socket"]["l1_connected"] = False
        param_edge.state_ground["capture"]["socket"]["l2_connected"] = False

test_connection_ground.edge_has_been_co = False
test_connection_ground.edge_has_been_deco = True

#Test SLAM http connection
def test_connection_slam():
    [ip, port, connected] = https_client_fct.network_info("slam")
    connected = https_client_fct.send_https_ping(ip, port)
    param_edge.state_edge["slam"]["http"]["connected"] = connected

    if(connected == True and test_connection_slam.edge_has_been_deco):
        test_connection_slam.edge_has_been_co = True
        test_connection_slam.edge_has_been_deco = False
        terminal.addConnection("slam", "on")
    elif(connected == False and test_connection_slam.edge_has_been_co):
        test_connection_slam.edge_has_been_co = False
        test_connection_slam.edge_has_been_deco = True
        terminal.addConnection("slam", "off")

test_connection_slam.edge_has_been_co = False
test_connection_slam.edge_has_been_deco = True

#Test AI http connection
def test_connection_ai():
    [ip, port, connected] = https_client_fct.network_info("ai")
    connected = https_client_fct.send_https_ping(ip, port)
    param_edge.state_edge["ai"]["http"]["connected"] = connected

    if(connected == True and test_connection_ai.edge_has_been_deco):
        test_connection_ai.edge_has_been_co = True
        test_connection_ai.edge_has_been_deco = False
        terminal.addConnection("slam", "on")
    elif(connected == False and test_connection_ai.edge_has_been_co):
        test_connection_ai.edge_has_been_co = False
        test_connection_ai.edge_has_been_deco = True
        terminal.addConnection("slam", "off")

test_connection_ai.edge_has_been_co = False
test_connection_ai.edge_has_been_deco = True
