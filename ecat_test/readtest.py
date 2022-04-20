from pyEtherCAT import MasterEtherCAT #ライブラリの読出し
nic = "eth0" # ネットワークカードのアドレスを記載
cat = MasterEtherCAT.MasterEtherCAT(nic)  

ADP = 0x0000 #1台目
ADDR = 0x0E08 #コアレジスタのアドレス
cat.APRD(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=[0,0,0,0,0,0,0,0]) #DATAは０を８個(64bit分)の枠を指示
(DATA, WKC) = cat.socket_read() #結果を読出し
print("[0x{:04X}]= 0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x}".format(ADDR, DATA[7],DATA[6],DATA[5],DATA[4],DATA[3],DATA[2],DATA[1],DATA[0]))
#読み出したデータを表示する
print('\n' + str(DATA))