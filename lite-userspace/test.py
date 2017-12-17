
import ctypes


#testlib = ctypes.CDLL('./test.so')

lite_lib = ctypes.CDLL('./lite-lib.so')

def join_cluster():

    #testlib.join()
    print("This node id is", lite_lib.userspace_liteapi_get_node_id())



# a function that returns information about the LITE cluster

def get_LITE_cluster_info():

    #print("This node has id", testlib.get_own_cluster_id())
    #print("This cluster has "+  str(testlib.get_cluster_size())+  " nodes.")
    print("Duppity do")



# a function that sends an array

# a function that receives an array and prints it out


#
join_cluster()
get_LITE_cluster_info()