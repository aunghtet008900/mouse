class command:
    def __init__(self):
        self.name = "getvol"
        self.description = "Get volume level."
    
    def run(self,session,cmd_data):
        print("Current volume: "+session.send_command(cmd_data))
