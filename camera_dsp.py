class CameraDSP:
    def execute(self, command, payload):
        if command == "captureImage":
            # Simulate base64 image capture
            return "data:image/png;base64,iVBORw0KGgoAAAANS..."
        else:
            raise Exception("Unknown camera command")
