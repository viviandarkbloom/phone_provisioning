from testtest.models import Phone

def getnewphone():
	#get new phones from database
	newphone = Phone.objects.filter(isnew=True)
	return newphone

def getnewext():
	newext = Ext.objects.filter(isnew=True)
	return newext

def ftpconnect():
	#make ftp connection
	pass

def deletephone():
	#delete a record
	pass

def writeconfig():
	#writes to phone.cfg, mac.cfg
	pass
	
