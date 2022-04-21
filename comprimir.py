import os
import zipfile
ctf_flag = zipfile.ZipFile('flag0.zip', 'w')
ctf_flag.write('flag.zip', compress_type=zipfile.ZIP_DEFLATED)
ctf_flag.close()
i = 0
while (i <= 50):
    ctf_flag = zipfile.ZipFile('flag'+ str(i+1) + '.zip', 'w')
    ctf_flag.write('flag'+ str(i) + '.zip', compress_type=zipfile.ZIP_DEFLATED)
    ctf_flag.close()
    os.remove('flag' + str(i)  + '.zip')
    i += 1