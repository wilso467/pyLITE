A Python Interface for LITE Local Indirection TiEr
====

For a detailed look at LITE and for LITE build and installation instructions, please see https://github.com/WukLab/LITE.

To use pyLITE, execute the following in pyLITE/lite-userspace:

gcc -shared -o lite-lib.so -fpic lite-lib.c
gcc -shared -Wl, -soname, test -o testso -fPIC test.c

This should produce the shared object files pyLITE requires.







## To cite LITE, please use:

>\@inproceedings{SOSP17-LITE\,  
> author = {Shin-Yeh Tsai and Yiying Zhang},  
> title = {LITE Kernel RDMA Support for Datacenter Applications},  
> booktitle = {Proceedings of the 26th Symposium on Operating Systems Principles (SOSP '17)},  
> year = {2017},  
> address = {Shanghai, China},  
> month = {October}  
>}
 
