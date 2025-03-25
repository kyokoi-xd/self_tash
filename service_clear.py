import win32service
import win32serviceutil
import win32event
import time
import schedule
import os 
import sqlite3
import subprocess

chrome_history_path = os.path.expanduser(r'C:\Users\Dima\AppData\Local\Google\Chrome\User Data\Default\History')

class ClearBrowserDataService(win32serviceutil.ServiceFramework):
    _svc_name = "ClearBrowserDataService"
    _svc_display_name = "Clear Browser Data Service"
    _svc_description = "Service to clear GoogleChrome browsing data on schedule"

    def __init__(self, args):
        super().__init__(args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def SvcDoRun(self):
        self.main()
    
    def close_chrome():
        subprocess.call("taskkill /im chrome.exe /f", shell=True)

    def clear_history(self):
        try:
            conn = sqlite3.connect(chrome_history_path)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM urls")
            conn.commit()
            print("История просмотра успешно очищена")

        except sqlite3.Error as e:
            print(f'Ошибка: {e}')

        finally:
            if conn:
                conn.close()

        def main(self):
            schedule.every().day.at("12:40").do(self.clear_history)

            while self.is_running:
                schedule.run_pending()
                time.sleep(60)




if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(ClearBrowserDataService)
            
    