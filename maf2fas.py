#!/usr/bin/env python
#coding=utf-8
# Convert maf file to fasta file
# 2023-9-6.
# @author: zhangwanyu
import json
import os
def run(fpath,outfpath,gz=True):
    # Open file
    if(gz):
        import gzip
        f = gzip.open(fpath,'rt')
    else:
        f = open(fpath,'r')
    # File parse
    seqid_ls = []
    sequn_dt = {}
    temp_dt  = {}
    refid    = ''
    for line in f:
        if(line[0]=='#'):   continue
        a = line.strip().split()
        if(len(a)<1):       continue
        if(a[0] not in ['a','s']): continue
        if(a[0]=='a'): # handle the information in the last block
            for i in seqid_ls:
                if(i not in sequn_dt.keys()): sequn_dt[i] = "-"*(len(sequn_dt[refid])-len(temp_dt[refid]) if refid in sequn_dt.keys() else 0)
                if(i in temp_dt.keys()): sequn_dt[i] += temp_dt[i]
                else:                    sequn_dt[i] += "-"*len(temp_dt[refid])
            temp_dt = {} # reset this dict and wait for next loop.
        else: # in-block processing
            seqid = a[1]
            sequn = a[-1]
            if(seqid not in seqid_ls): seqid_ls.append(seqid)
            if(refid==''): refid = seqid
            #print(refid) #debug
            temp_dt[seqid] = sequn
        #print("temp_dt=",  json.dumps(temp_dt, indent="\t")) #debug
        #print("sequn_dt=", json.dumps(sequn_dt,indent="\t")) #debug
        #os.system("pause")
    for i in seqid_ls:
        if(i in temp_dt.keys()): sequn_dt[i] += temp_dt[i]
        else:                    sequn_dt[i] += "-"*len(temp_dt[refid])
    f.close()
    # Write to output file
    maxLineLen = 70 # maximum of the line length. in other words, how many characters can one line contain.
    outf = open(outfpath,'w')
    for i in seqid_ls:
        outf.write(">{}\n".format(i))
        sequn = sequn_dt[i]
        sequnLen = len(sequn)
        lineNum  = int(sequnLen/maxLineLen)
        for j in range(lineNum):
            outf.write("{}\n".format(sequn[j*maxLineLen:(j+1)*maxLineLen]))
        outf.write("{}\n\n".format(sequn[lineNum*maxLineLen:])) # this is the last line of one seq. so add addition "\n" at the end.
    outf.close()

if(__name__=='__main__'):
    import sys
    Usage = """
    python maf2fas <maf> [output fasta]
    <maf>           Input maf/maf.gz file
    [output fasta]  Optional. The output file name.
                    If empty, the program will use maf file's name + ".fas" as default name.
    """.strip()
    if(len(sys.argv)<2 or sys.argv[1] in ["-h","--help","/?","/help","/h"]):
        print(Usage)
        sys.exit(1)
    else:
        fpath = sys.argv[1]
        if(fpath[-3:]==".gz"): gz = True
        else:                  gz = False
        if(len(sys.argv)==3):  outfpath = sys.argv[2]
        else:                  outfpath = fpath+".fas"
        run(fpath,outfpath,gz)
    





            




