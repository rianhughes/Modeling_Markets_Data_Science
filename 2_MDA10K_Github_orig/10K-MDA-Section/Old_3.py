import sys
import csv

# File_XLSX and File_MDAT Need to use the same ID system
File_XLSX   = "0_2__XLXS_PD_Search_and_Write_DATA.csv"  
File_MDAT   = "MDA_Tone.csv"
FILE_NEW    = "0_3__FUSE_MDA_XLSX_DATA.csv" 

with open(FILE_NEW,"a+") as newfile:
    #newfile.write([])
    x = open(File_XLSX, "r")
    t = open(File_MDAT, "r")

    # Header
    xRead=next(csv.reader(x), None)
    tRead=next(csv.reader(t), None)
    newfile.write(str(xRead + tRead))
    for line in x:
        xRead=next(csv.reader(x))
        tRead=next(csv.reader(t))
        xID=int(xRead[0])
        tID=int(tRead[0])
        print("-----STARTING")
        print([xID, tID])
        # It's unlikely that more than 5 consec urls had txt files but no xlsx files
        for ii in range(0,5):
            if xID==tID:
                # do stuff
                newfile.write(str(xRead + tRead))
                print("EQUAL")
                print([xID, tID])
                print(tRead)
#                print(str(xRead) + str(tRead[1])+ str(tRead[2])+ str(tRead[4])+ str(tRead[5])+ str(tRead[7])+ str(tRead[8])+ str(tRead[9])+ str(tRead[10])+ str(tRead[11])+ str(tRead[12]))
                break
            else:
                print("UNEQuA")
                print([xID, tID])
                tRead=next(csv.reader(t))
                tID=int(tRead[0])

        if xID>10:
            x.close()
            t.close()
            sys.exit()
    x.close()
    t.close()
