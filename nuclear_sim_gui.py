import tkinter as tk
from tkinter import messagebox
import time

from tkinter import*
import pygame

class NuclearTerminalApp:

    pygame.init()
    pygame.mixer.init()
    

    '''def play(self):
        pygame.mixer.music.load("alert sound.mp3")
        pygame.mixer.music.play(loops=0)
        time.sleep(20)'''
        

    def __init__(self, root):
        self.root = root
        self.root.title("Nuclear Weapons Terminal Simulation")
        self.root.geometry("1000x800")
        
        self.tries = 0
        self.retries = 3

        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Underground Nuclear Facility 'North Point'", font=("Helvetica", 25))
        self.title_label.pack(pady=40)

        self.warning_label = tk.Label(self.root, text="**** WARNING! Unauthorized access will initiate lockdown protocol 1104 ****", fg="red", font=("Helvetica", 16))
        self.warning_label.pack(pady=5)
        
        self.code_label = tk.Label(self.root, text="Enter the designated station's nuclear key:", font=("Helvetica", 16))
        self.code_label.pack(pady=5)

        self.code_entry = tk.Entry(self.root, font=("Helvetica", 13))
        self.code_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_code, font=("Helvetica", 18))
        self.submit_button.pack(pady=5)

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack(pady=5)

        self.message_label1 = tk.Label(self.root, text="")
        self.message_label1.pack(pady=5)

        '''self.code_label2 = tk.Label(self.root, text="ENTER THE DESIGNATED TARGET :")
        self.code_label2.pack(pady=5)

        self.code_entry2 = tk.Entry(self.root)
        self.code_entry2.pack(pady=5)

        self.submit_button2 = tk.Button(self.root, text="Confirm")
        self.submit_button2.pack(pady=5)'''

        self.launch_button = tk.Button(self.root, text="Initiate Launch Protocol", command=self.initiate_launch, state=tk.DISABLED, font=("Helvetica", 18))
        self.launch_button.pack(pady=5)

    def check_code(self):
        try:
            code = int(self.code_entry.get())
        except ValueError:
            self.message_label.config(text="Invalid input. Please enter a number.", font=("Helvetica", 13), fg="red")
            return
        
        if code != 9012:
            self.tries += 1
            self.retries -= 1
            self.message_label.config(text=f"INVALID CODE. REMAINING TRIES: {self.retries}", font=("Helvetica", 13), fg="red")
            if self.retries == 0:
                messagebox.showerror("Lockdown", "UNAUTHORIZED ACCESS DETECTED! INITIATING LOCKDOWN PROTOCOL 1104")
                self.root.quit()
        else:
            self.message_label.config(text="ACCESS GRANTED!", fg="green", font=("Helvetica", 13))
            self.launch_button.config(state=tk.NORMAL)
    
    def initiate_launch(self):

        sounda=pygame.mixer.Sound("alerts.mp3")
        sounda.play(loops=4)
        time.sleep(1)

        self.message_label.config(text="NUCLEAR LAUNCH PROTOCOL DELTA INITIATED. EVACUATE LAUNCH AREA!", fg="black")
        self.run_diagnostics()
    
    def run_diagnostics(self):
        self.message_label.config(text="RUNNING DIAGNOSTICS ON THE LAUNCH SYSTEMS...")
        self.root.after(5000, self.diagnostics_complete)
    
    def diagnostics_complete(self):
        self.message_label.config(text="ALL LAUNCH SYSTEMS NOMINAL\nPREPARING NUCLEAR WARHEADS...")
        self.root.after(6000, self.prepare_warheads)
    
    def prepare_warheads(self):
        self.message_label.config(text="WARHEAD 1 STATUS: READY")
        self.root.after(2000, self.warhead2_status)
    
    def warhead2_status(self):
        self.message_label.config(text="WARHEAD 2 STATUS: READY")
        self.root.after(2000, self.warhead3_status)
    
    def warhead3_status(self):
        self.message_label.config(text="WARHEAD 3 STATUS: READY")
        self.root.after(2000, self.awaiting_status_analysis)
    
    def awaiting_status_analysis(self):
        self.message_label.config(text="AWAITING STATUS ANALYSIS...")
        self.root.after(5000, self.status_analysis_complete)
    
    def status_analysis_complete(self):
        self.message_label.config(text="ATTENTION! NUCLEAR WARHEADS 1, 2, AND 3 ARMED AND ON STANDBY!")
        self.confirmation_label = tk.Label(self.root, text="*** AWAITING LAUNCH CONFIRMATION ***", font=("Helvetica", 13))
        self.confirmation_label.pack(pady=5)
        self.confirm_button = tk.Button(self.root, text="Confirm Launch", command=self.start_countdown)
        self.confirm_button.pack(pady=5)
    
    def start_countdown(self):
        self.confirmation_label.destroy()
        self.confirm_button.destroy()
        self.message_label.config(text="COMMENCING LAUNCH COUNTDOWN...")
        self.countdown(10, self.launch)
    
    def countdown(self, t, callback):
        if t > 0:
            self.message_label1.config(text=f"----- {t} -----")
            self.root.after(1000, self.countdown, t-1, callback)
        else:
            callback()
    
    def launch(self):
        self.message_label.config(text="Nuclear Warhead launching...\nTOUCHDOWN ON TARGET AREA IN...")
        self.countdown(18, self.confirm_impact)
    
    def confirm_impact(self):
        self.message_label.config(text="* CONFIRMING IMPACT WITH TARGET AREA *")
        self.message_label1.config(text="------------")
        self.root.after(5000, self.operation_successful)
    
    def operation_successful(self):
        self.message_label.config(text="###### Operation successful. Shutting down systems ######")
        self.message_label1.config(text="")
        self.root.after(5000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    app = NuclearTerminalApp(root)
    root.mainloop()
