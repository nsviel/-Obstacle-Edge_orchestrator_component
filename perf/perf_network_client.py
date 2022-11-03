#---------------------------------------------
from param import param_py

import iperf3


def perf_network_client():
    client = iperf3.Client()
    client.duration = 1
    client.server_hostname = param_py.state_py["hubium"]["ip"]
    client.port = param_py.state_py["hubium"]["sock_server_l1_port"]
    client.protocol = 'udp'
    result = client.run()

def print_result(client, result):
    print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
    if result.error:
        print(result.error)
    else:
        print('')
        print('Test completed:')
        print('  started at         {0}'.format(result.time))
        print('  bytes transmitted  {0}'.format(result.bytes))
        print('  jitter (ms)        {0}'.format(result.jitter_ms))
        print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))

        print('Average transmitted data in all sorts of networky formats:')
        print('  bits per second      (bps)   {0}'.format(result.bps))
        print('  Kilobits per second  (kbps)  {0}'.format(result.kbps))
        print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps))
        print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s))
        print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
