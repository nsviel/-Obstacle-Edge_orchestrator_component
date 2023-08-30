#---------------------------------------------
from src.param import param_edge
from src.connection.HTTPS.server import https_server
from src.connection.SOCK import sock_client
from src.connection import connection
from src.state import state
from src.utils import data
from src.utils import terminal
from src import daemon
import time


class Loop():
    def start(self):
        # Init variables
        self.init()

        # Start main loop program
        while param_edge.run_loop:
            self.loop()

        # Join threads
        self.end()

    def init(self):
        data.check_directories()
        state.load_configuration()
        sock_client.create_socket()
        self.daemons = daemon.Daemons()
        self.daemons.start_daemons()
        https_server.start_server()
        terminal.addLog("OK", "Program initialized...")
        terminal.addLine()

    def loop(self):
        time.sleep(param_edge.tic_loop)

    def end(self):
        terminal.shutdown()
        state.upload_states()
        self.daemons.stop_daemons()
        https_server.stop_server()
        terminal.delai()


loop = Loop()
