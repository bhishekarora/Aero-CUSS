from devices.camera_dsp import CameraDSP
from devices.printer_dsp import PrinterDSP
from devices.scanner_dsp import ScannerDSP

class DeviceRouter:
    def __init__(self):
        self.dsp_map = {
            'camera': CameraDSP(),
            'printer': PrinterDSP(),
            'scanner': ScannerDSP()
        }

    def execute(self, action):
        device = action['device']
        command = action['command']
        payload = action.get('payload')
        dsp = self.dsp_map.get(device)

        if not dsp:
            raise Exception(f"No DSP for {device}")
        return dsp.execute(command, payload)
