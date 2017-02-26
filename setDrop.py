import dropbox
dbx = dropbox.Dropbox('1uCFpS5a_WAAAAAAAAAADm8HRJFdJ6o-qi62nyHJX-N0h4k8OyjOj9Ypel1HO1Zz')
dbx.users_get_current_account()

metadat=dbx.files_download_to_file('/home/pi/Desktop/data.txt','/Amazon_Alexa/amazon_alexa_shopping.txt')
#print(metadat)
file = open('/home/pi/Desktop/data.txt','r')
lineList = file.readlines()
file.close()
cleanfile = str(lineList[-1:])
split = [] 
for x in range(5):
  split.append(' ')
#square = []
#for x in range(5):
#  square.append(x**2)
#print(square)

try:
 simple = str(cleanfile[2:len(cleanfile)-4]) 
 split = simple.split('by ')
 split[0]
 split[1]
except Exception as e:
 split[0]='Never gonna give you up'
 split.append('Rick Astly')
print(split[0])
print(split[1])
