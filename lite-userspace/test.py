
import ctypes


testlib = ctypes.CDLL('./test.so')

lite_lib = ctypes.CDLL('./lite-lib.so')

def join_cluster():

    #testlib.join()
    print("This node id is", lite_lib.userspace_liteapi_get_node_id())

# a function that returns information about the LITE cluster

def get_LITE_cluster_info():

    print("This node has id", lite_lib.userspace_liteapi_get_node_id())
    print("This cluster has "+ str(lite_lib.userspace_liteapi_get_total_node())  +" nodes.")



# a function that sends an array

# a function that receives an array and prints it out

#join_cluster()
get_LITE_cluster_info()

a=ctypes.c_int(1)
b=ctypes.c_int(2)
c = testlib.test(ctypes.pointer(a), ctypes.pointer(b))

print(c)

