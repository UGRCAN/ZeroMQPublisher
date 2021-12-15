import zmq
import time

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind("tcp://0.0.0.0:1234")


topic = "A"
while True:
    val = input("Enter your message: ")
    sock.send_string("%s%s" % (topic,  val))
    print("Sent message: %s ..." % val)
    time.sleep(1)
    ans = input("Would you like send new message? Pres Y/y or enter to exit").lower()
    if ans != 'y':
        break

sock.close()
ctx.term()