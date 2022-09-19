#---------------------------------------------
from HTTP import http_client_get
from HTTP import http_client_post


#---------------------------------------------
# Possible GET commands:
# - /slam_on
# - /slam_off
# - /view_top
# - /view_oblique
#---------------------------------------------
def forward_ve_post(option, value):
    if(option == "slam"):
        if(str(value) == "True"):
            http_client_get.send_command("ve", "/slam_on")
        if(str(value) == "False"):
            http_client_get.send_command("ve", "/slam_off")
    elif(option == "view"):
        if(value == "Top"):
            http_client_get.send_command("ve", "/view_top")
        if(value == "Oblique"):
            http_client_get.send_command("ve", "/view_oblique")

#---------------------------------------------
# Possible POST commands:
# - /lidar_height
# - /threshold
#---------------------------------------------
def forward_ai_post(option, value):
    if(option == "lidar_height"):
        http_client_post.post_command("ai", "/lidar_height", value)
    if(option == "threshold"):
        http_client_post.post_command("ai", "/threshold", value)
