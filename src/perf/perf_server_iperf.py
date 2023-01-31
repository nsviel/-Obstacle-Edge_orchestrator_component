#---------------------------------------------
from src.param import param_hu
import iperf3


def process_perf_server(port):
    try:
        ip = param_hu.state_hu["self"]["ip"]
        server = iperf3.Server()
        server.bind_address = ip
        server.port = port
        server.verbose = False
        server.json_output = True
        result = server.run()
    except:
        pass

def print_result(result):
    try:
        if(result != None and result.error == None):
            print('  bytes transmitted  {0}'.format(result.bytes))
            print('')
            print('Test completed:')
            print('')
            print('  started at         {0}'.format(result.time))
            print('  jitter (ms)        {0}'.format(result.jitter_ms))
            print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

            print('Average transmitted data in all sorts of networky formats:')
            print('  bits per second      (bps)   {0}'.format(result.bps))
            print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
            print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
            print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
            print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
    except:
        pass
