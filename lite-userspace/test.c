//
// Created by root on 12/16/17.
//

#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdarg.h>
#include <pthread.h>
#include <time.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <sys/syscall.h>
#include <stdbool.h>
#include <malloc.h>
#include "lite-lib.h"


//to compile in shared library
//gcc -shared -Wl,-soname,test -o test.so -fPIC test.c

void derp(void);

void derp(){
    printf("Herpa derp");
}


void join(void);

void join(){
    printf("we are now running write experiments\n");
    userspace_liteapi_join("192.168.0.1", 18500, 1);
    printf("I've joined the cluster as LITE node %d\n", userspace_liteapi_get_node_id());
}

unsigned  int get_own_cluster_id(void);

unsigned  int get_own_cluster_id() {
    return userspace_liteapi_get_node_id();
}

unsigned int get_cluster_size(void);

unsigned int get_cluster_size(){
    return userspace_liteapi_get_total_node();
}

int main() {

    printf("Hello idiot");

    return 0;
}

