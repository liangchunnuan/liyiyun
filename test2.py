import network
sta_if=network.WLAN(network.STA_IF)
ap_if=network.WLAN(network.AP_IF)
ap_if.active(False)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect('红米手机','123212321')
    while not sta_if.isconnected():
        psaa
    print('network config:',sta_if.ifconfig())
    


