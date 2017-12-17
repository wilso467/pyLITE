
import ctypes




testlib = ctypes.CDLL('./test.so')

def join_cluster():

    testlib.join()



# a function that returns information about the LITE cluster

def get_LITE_cluster_info():

    print("This node has id", testlib.get_own_cluster_id())
    print("This cluster has "+  str(testlib.get_cluster_size())+  " nodes.")



# a function that sends an array

# a function that receives an array and prints it out