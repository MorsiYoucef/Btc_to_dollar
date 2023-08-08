from forex_python.bitcoin import BtcConverter
b = BtcConverter()
n = int(input("enter the mount :"))
print(b.convert_to_btc(n,'USD'),"Btc")

