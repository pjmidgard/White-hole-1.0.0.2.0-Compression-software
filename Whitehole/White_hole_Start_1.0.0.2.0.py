import os
import getpass
USER_NAME = getpass.getuser()



file_path="C:\\Program Files\\White_hole\\White_hole_Start_1.0.0.2.0.exe"
if file_path == "C:\\Program Files\\White_hole\\White_hole_Start_1.0.0.2.0.exe":
    file_path = os.path.dirname(os.path.realpath(__file__))
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
    bat_file.write(r'start "" %s' % file_path)


import subprocess, json

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId | ConvertTo-Json}\"")
j = json.loads(out)
for dev in j:
    print(dev['Status'], dev['Class'], dev['FriendlyName'], dev['InstanceId'] )
    os.system('F:\\Whitehole\\White_hole_1.0.0.2.0.exe')
    os.system('E:\\Whitehole\\White_hole_1.0.0.2.0.exe')
