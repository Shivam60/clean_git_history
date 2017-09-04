import subprocess
print("")
p=subprocess.run('bash fat_objects.sh n5 -d -f'.split(' '),stdout=subprocess.PIPE))
out,err=p.communicate()
for i in out:
 print(i)
i=input("Enter y to clean the above mentioned from git history. anything else to stop.")
if i=='y':
 for i in out:
  p=subprocess.run('bash remove_objects.sh'.split(' ')+list(i))
else:
 print("Stop input read. bye")
