from tkinter import *
import pcapy

root = Tk()
root.geometry('720x480')
root.title('Packet Sniffer')

capture_devices = pcapy.findalldevs()

capture_devices_list = StringVar(root)
capture_devices_list.set(capture_devices[0]) # default value

devices_menu = OptionMenu(root, capture_devices_list, *capture_devices)
devices_menu.pack()

# defining capture parameters
packet_size = 65536
promiscous_mode = 1     # 0 for no/false and 1 for yes/true
timeout = 0

def capture_packets():
    cap = pcapy.open_live(capture_devices_list.get(),packet_size, promiscous_mode,timeout)
    count = 1
    while count<2:
        (header,payload) = cap.next()
        print(count + '\n' + header + '\n')
        print(payload + '\n \n')
        count+=1

capture_packets_button = Button(root, text="Capture", command=capture_packets)
capture_packets_button.pack()

mainloop()