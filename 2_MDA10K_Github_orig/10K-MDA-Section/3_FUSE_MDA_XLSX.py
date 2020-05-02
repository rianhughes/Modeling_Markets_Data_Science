import sys
import csv
import os
# File_XLSX and File_MDAT Need to use the same ID system
File_XLSX   = "0_2__XLXS_PD_Search_and_Write_DATA.csv"  
File_MDAT   = "MDA_Tone.csv"
FILE_NEW    = "0_3__FUSE_MDA_XLSX_DATA.csv" 

# Remove new file if it exists. Keep it fresh.
if os.path.exists(FILE_NEW):
    os.remove(FILE_NEW)

with open(FILE_NEW,"a+") as newfile:
    print("Saving Data to " + FILE_NEW)
    writer=csv.writer(newfile)
    x = open(File_XLSX, "r")
    t = open(File_MDAT, "r")
    xx=csv.writer(x)
    tt=csv.writer(t)
    # Header
    xRead=next(csv.reader(x), None)
    tRead=next(csv.reader(t), None)
    
    #It's ugly, I know!
    #newfile.write(str(xRead + [str(tRead[0]) , str(tRead[1]), str(tRead[3]), str(tRead[4]), str(tRead[6]), str(tRead[7]), str(tRead[8]), str(tRead[9]), str(tRead[10]), str(tRead[11]) ] ) + "\n")
    print(xRead)
    print(tRead)
    writer.writerow(xRead + tRead)
    for line in x:
        xRead=next(csv.reader(x))
        tRead=next(csv.reader(t))
        xID=int(xRead[0])
        tID=int(tRead[0])
        print("-----STARTING")
        print([xID, tID])
        # It's unlikely that more than 100 consecutive urls had txt files but no xlsx files
        for ii in range(0,200):
            if xID==tID:
                # do stuff
                writer.writerow(xRead + tRead)
                #newfile.write(str(xRead + [str(tRead[0]) , str(tRead[1]), str(tRead[3]), str(tRead[4]), str(tRead[6]), str(tRead[7]), str(tRead[8]), str(tRead[9]), str(tRead[10]), str(tRead[11]) ] ) + "\n")
#                newfile.write(str(xRead) + str(tRead[0])+ str(tRead[1])+ str(tRead[3])+ str(tRead[4])+ str(tRead[6])+ str(tRead[7])+ str(tRead[8])+ str(tRead[9])+ str(tRead[10])+ str(tRead[11]) + "\n")
                print("EQUAL")
                print([xID, tID])
                break
            else:
                print("UNEQuA")
                print([xID, tID])
                tRead=next(csv.reader(t))
                tID=int(tRead[0])

        #if xID>10:
        #    x.close()
        #    t.close()
        #    sys.exit()

    x.close()
    t.close()
