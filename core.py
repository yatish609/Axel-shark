from PyQt5 import QtCore
from scapy.all import *
from threading import Thread, Event

class SnifferThread(QtCore.QThread):
        connection = QtCore.pyqtSignal(list)

        def __init__(self,selected_iface):
            super(SnifferThread, self).__init__()
            self.selected_iface = selected_iface
        
        def print_packet(self,packet):
            ip_layer = packet.getlayer(IP)
            packet_length = str(len(packet))
            row_Data = [str(packet.time),str(ip_layer.src),str(ip_layer.dst)]
            
            if(packet.haslayer('TCP')):
                row_Data.append('TCP')
            elif(packet.haslayer('UDP')):
                row_Data.append('UDP')
            elif(packet.haslayer('ICMP')):
                row_Data.append('ICMP')
            elif(packet.haslayer('DNS')):
                row_Data.append('DNS')
            else:
                row_Data.append('Unknown Type')
                    
            row_Data.append(packet_length)
            if UDP in packet:
                packet_info = "sport = " + str(packet[UDP].sport) + ", dport = " + str(packet[UDP].dport)
            elif TCP in packet:
                packet_info = "sport = " + str(packet[TCP].sport) + ", dport = " + str(packet[TCP].dport)
            elif ICMP in packet:
                packet_info = "ICMP Packet"
            elif DNS in packet:
                packet_info = "sport = " + str(packet[DNS].sport) + ", dport = " + str(packet[DNS].dport)
            else:
                packet_info = "Unknown Type"

            row_Data.append(packet_info)
            row_Data.append(str(packet))

            full_data = str(packet.show(dump=True))
            row_Data.append(full_data)
            self.connection.emit(row_Data)
    
        def run(self):
            packets = sniff(iface=self.selected_iface, filter="ip", prn=self.print_packet)

        def stop(self):
            self._isRunning = False
            self.wait(100)
            self.terminate()
