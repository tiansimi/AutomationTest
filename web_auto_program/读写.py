from web_auto_program.common.filePath import path

filecasepath = path + 'report/test.txt'
print(filecasepath)
f = open(filecasepath, 'w')
f.write('666')
f.close()



