from client.comm import BaseComm
from common.frame_enum import FrameType


class Module:
    def __init__(self, comm: BaseComm):
        self.comm = comm
        self.comm.listen_for([FrameType.UI_COMMAND])


    def process(self):

        while self.comm.has_data():

            frame = self.comm.get_data()

            if frame.request:
                continue

            if frame.type == FrameType.UI_COMMAND:
                data = frame.get_data()
                command = data[0]
                params = data[1]
                destination = data[2]
                print(command, params, destination)


    def stop(self):
        self.comm.stop()
