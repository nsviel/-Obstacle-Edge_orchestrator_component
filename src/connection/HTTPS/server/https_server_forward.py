#---------------------------------------------
from src.connection.HTTPS.client import https_client_get
from src.connection.HTTPS.client import https_client_post


#---------------------------------------------
# Possible GET commands:
# - /slam_on
# - /slam_off
# - /view_top
# - /view_oblique
#---------------------------------------------
def forward_processing_post(option, value):
    if(option == "slam"):
        if(str(value) == "True"):
            https_client_get.send_command("slam", "/slam_on")
        if(str(value) == "False"):
            https_client_get.send_command("slam", "/slam_off")
    elif(option == "view"):
        if(value == "Top"):
            https_client_get.send_command("slam", "/view_top")
        if(value == "Oblique"):
            https_client_get.send_command("slam", "/view_oblique")
    elif(value == "reset"):
        if(value == "reset"):
            https_client_get.send_command("slam", "/reset")

#---------------------------------------------
# Possible POST commands:
# - /lidar_height
# - /threshold
#---------------------------------------------
def forward_ai_post(option, value):
    if(option == "lidar_height"):
        https_client_post.post_command("ai", "/lidar_height", value)
    if(option == "threshold"):
        https_client_post.post_command("ai", "/threshold", value)
