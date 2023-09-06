# maf2fas
a single python script for converting multiple alignment file(MAF) to FASTA sequence file.

## Usage

```bash
python maf2fas.py <maf> [output fasta]
    <maf>           Input maf/maf.gz file
    [output fasta]  Optional. The output file name.
                    If empty, the program will use maf file's name + ".fas" as default name.
```

(For Linux&maxOS user) Besides, you can also move this script to any directory under system `$PATH` and rename script file as `maf2fas`, and add excutable permission(`chmod +x maf2fas`). Therefore, you can call this program by command `maf2fas` anywhere in your system.

## Features

+ Automatic completion sequence by gap("-")
+ Output aligned fasta
+ Easily deal with gzipped file




