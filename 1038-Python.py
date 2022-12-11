produto, quantidade = input().split()

if (produto =="1"):
     pagar = float(int(quantidade)*4)
     print("Total: R$ %0.2f" %pagar)
elif (produto =="2"):
     pagar = float(int(quantidade)*4.5)
     print("Total: R$ %0.2f" %pagar)
elif (produto =="3"):
     pagar = float(int(quantidade)*5)
     print("Total: R$ %0.2f" %pagar)
elif (produto =="4"):
     pagar = float(int(quantidade)*2)
     print("Total: R$ %0.2f" %pagar)
elif (produto =="5"):
     pagar = float(int(quantidade)*1.5)
     print("Total: R$ %0.2f" %pagar)