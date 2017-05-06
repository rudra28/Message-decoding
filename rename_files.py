import os
def decode_secret():

    #get all message name from the message list
    msg_list = os.listdir(r"C:\Users\rudra\Documents\Udacity\rename")

    #print msg_list
    print msg_list
    
    msg_path = os.getcwd()
    print("Current working directory is:" + msg_path)
    os.chdir(r"C:\Users\rudra\Documents\Udacity\rename")

    #for each message, rename message list
    for msg in msg_list:
        print("Old name -" + msg)
        print("New Name -" + msg.translate(None, "0123456789"))
        os.rename(msg, msg.translate(None, "0123456789"))
        #os.chdir(msg_path)

decode_secret()
