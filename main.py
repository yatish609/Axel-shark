from tkinter import *
import tkinter as tk
import pcapy
import logging

root = Tk()
root.geometry('720x480')
root.title('Packet Sniffer')

logging.basicConfig(filename="sniffer.log", format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

capture_devices = pcapy.findalldevs()

capture_devices_list = StringVar(root)
capture_devices_list.set(capture_devices[0]) # default value

devices_menu = OptionMenu(root, capture_devices_list, *capture_devices)
devices_menu.pack()

# defining capture parameters
packet_size = 65536
promiscous_mode = 1     # 0 for no/false and 1 for yes/true
timeout = 0

output = tk.Text(root)
output.pack()

def capture_packets():
    try:
        cap = pcapy.open_live(capture_devices_list.get(),packet_size, promiscous_mode,timeout)
        count = 1
        while count:
            (header,payload) = cap.next()
            output.insert(tk.END, header)
            output.insert(tk.END, payload)
            count+=1
        root.update_idletasks()
        logger.info('Packets captured successfully!')
    except pcapy.PcapError:
        logger.error('Problem with capture device!')
        output.insert(tk.END,'\n Problem with capture device!')
    except:
        logger.error('Some other error')
        output.insert(tk.END,'\n Some unknown error!')

capture_packets_button = Button(root, text="Capture", command=capture_packets)
capture_packets_button.pack()

button = tk.Button(root, text = 'Exit', command=root.destroy)
button.pack()

mainloop()