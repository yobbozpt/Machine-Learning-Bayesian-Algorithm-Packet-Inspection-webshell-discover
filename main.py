# coding =utf-8
# 程序作者:vr_system
# 程序版本:v 1.0

import listen_traffic

if __name__ == '__main__':
    port_name = "VirtualBox Host-Only Ethernet Adapter"#写入自己网卡名称
    port_filter = "tcp port 80 8080"
    listen_traffic.ListenTraffic().run(port_name=port_name, port_filter=port_filter)

    
    #WARNING: Calling str(pkt) on Python 3 makes no sense!（想知道这个是什么问题）
    #ERROR: Could not compile filter expression tcp port 80 8080（）还有这个问题
