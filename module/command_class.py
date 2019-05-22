from common.frame_enum import FrameType


class command():
    def __init__(self, command_type, parameters :[str], destination: [str]):
        self.parameters :[str] = parameters
        self.destinations :[str] = destination
        self.intelligent :str
        self.cmd_id :int
        self.status :int
        self.output_frames :FrameType

    def check_command_type(self):
        pass

    def check_frame_type(self):
        pass

    def update_status(self):
        pass

    def send_frame_to_destinations(self):
        pass

    def convert_parameters_to_frame(self):
        pass

    def log_command(self):
        pass

    def log_status(self):
        pass