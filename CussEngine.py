from core.app_manager import AppManager
from core.device_router import DeviceRouter

class CussEngine:
    def __init__(self):
        self.device_router = DeviceRouter()
        self.app_manager = AppManager()

    def start_session(self, airline_code):
        print(f"[CUSS] Starting session for {airline_code}")
        app = self.app_manager.get_app(airline_code)
        app.on_start()

        while not app.is_complete():
            action = app.next_action()
            result = self.device_router.execute(action)
            app.on_device_result(result)

        app.on_end()
