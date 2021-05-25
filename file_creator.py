import QT_PlutoSDR
import time

channel_to_freq  = {'channel1':2407000000, 'channel2':2412000000, 'channel3':2417000000, 'channel4':2422000000
				   ,'channel5':2427000000, 'channel6':2432000000, 'channel7':2437000000, 'channel8':2442000000
				   ,'channel9':2447000000, 'channel10':2452000000, 'channel11':2457000000, 'channel12':2462000000
				   ,'channel13':24670000}
input_file_channel = 'channel1_bin.txt'

for i in range(1,14):
    dict_index = 'channel' + str(i)
    input_file_channel = input_file_channel.split("_")[0][:7] + str(i) + "_" + input_file_channel.split("_")[1]
    flowgraph = QT_PlutoSDR.QT_PlutoSDR()
    flowgraph.set_freq(channel_to_freq[dict_index])
    flowgraph.set_filename(input_file_channel)
    flowgraph.start()
    time.sleep(0.05)
    flowgraph.stop()
    print("Frequency "+str(i)+" created")
    
print('exited')
exit()