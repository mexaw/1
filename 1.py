print('''

                     ./
                    -m`
                   +Nm
                 /dMMm
              `+mMMMNM-
              ::MMMN+om` -                      `/  --
              .hMMMoy/yh`m                    +:`d- :d`
             -mMsoMsyyoohM: `            `/ssssNosNy/md-
            /NMMooMm+soyhNm.s        `-++yNMMMMMMMMMNMMNy:
           :NMMMs+smdsyssshhN-       .hNdyyyhhhdNMMMNdmNMNds:`
          `mNMMMosyoNhoyyooyMN+`     so./hmNmyoosdMMMmmNNMMMdo+`
          `//MNy+yoyossyy+ooooyso/::/+ +Nd+hoo++++shMMh/sdNNmMMh+-
           `dM+ssy:msoyyyyyyso++/++/:`.NMs:mh/.``` :dNd-`.-..:sdm-
           yMdoyyy:NMyssyyy/.` `     .dMNoyy`       `.dN+`:/-.-s:.
          `MMoyyyy/oMMNhsyy+`/:+ys++smMM//``       ./sdMN/:/+ssss:--
          `MMh/syys.oNMo/yy/  .+dMMMMMMMmo.        `..-:::-` `-://-`
           sMMy/yyys-:dmssy-   `-:sdMMMMMMNdo:.````-/oy:
           `yMy.yyyys+:omso       `oooydmmNNNNNmmmmNMMNo+.
            `/hy/sy+ooo/:o`       `dMdo:+yyo+--/+//omN+y-:
              `+d/s ``            +dydMNdyshmo`     `d+`/
             `  :y.               .. `mMMMMmyo+`     ::
    -+sssss+::+` -                   .mdNMMMm/-.
   `+.```.-/yhdd--.                  -+`.dmoN/:
           `./yMNsoo`                    h+dhos
             `-+yNmNm/`                 .+dMhhy`ssso:  ` `    sso -ss/  ``  -so`os: ``  :s/.ss.:s:
              `.-/ohmNh:`           `.:+hMMMMMs+My/dM//dyy   :MNN:mNM/:yyhs  yMmm: +hdy`+MydNM+Nh`
                    `/hNh+.``:+.`   .:dMMMMNdN-dMo+mm-hM/.++ yMoMNsNN`mMyhy./ddNm.:dymM.:MNd/MNd`
                       -ohddhhMNds++oyNMNmN/:+ oooo/. oo `o+ oo`o+.o+ -oso.:o+`:o/-s+o+ `oo.`oo.
                         .:oyddddNNdyhms-s:
                              `-:-. `:` `
                Dr.MeXaW Script !
''')
print(' i hope to Enjoy  ')
import socket
import time
import os

print('u need install nmap Run this script on Kali :D ')
print('''





''')


f = input('Write the website : ')




fqdn = socket.gethostbyname(socket.getfqdn(f))

print ('The ip Website is ',fqdn)

print(' i will scanner the website !')
time.sleep(2)
options = '-F'

command = " nmap " + options + " " + f
procec =  os.popen(command)
results = str(procec.read())
print(results)
print(' Have a Nice Day :D !')
print('''

    Script To learn How
    to Do os command with nmap : !
    








''')
















