import os
number='+79277501432'
command = 'sendsms'
text = 'hello word'


def send(number, text):
    os.system(f"gammu sendsms TEXT {number} -unicode  -text '{text}'")

def read():
    # os.system(f"gammu getsmsc")
    re = add.os.system(f"gammu getallsms")
#     os.system("gammu deleteallsms 1")

if __name__ == "__main__":
    #send(number,text)
    read()
