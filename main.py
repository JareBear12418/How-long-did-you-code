import tkinter as tk
from tkinter import simpledialog
import configparser
saved_times = []
config_parser = configparser.ConfigParser()
config_parser.read('config.cfg')
for sect in config_parser.sections():
   for _,v in config_parser.items(sect):
      langauges = v.split(', ')

root = tk.Tk()
# Have no idea what all this does, but it focuses the window to the dialogs which is what u need.
root.geometry('0x0+0+0')
root.attributes("-topmost", True)
root.overrideredirect(True)
root.update_idletasks()
root.deiconify()
root.lift()
root.focus_force()

# need to load the total_time.cfg file before we update it with new values.
total_time_parser = configparser.ConfigParser()
total_time_parser.read('total_time.cfg')
for sect in total_time_parser.sections():
   for _,v in total_time_parser.items(sect):
      saved_times.append(v)
try: total_time_parser.add_section('TOTAL_TIME')
except Exception: pass
fp=open('total_time.cfg','w')
for i, langauge in enumerate(langauges):
    answer = simpledialog.askfloat("Hours", f"How long did you code in {langauge}?",
                                parent=root,
                                minvalue=0.0, maxvalue=100000.0,
                                initialvalue='0')
    answer = 0 if answer is None else answer
    try: total_time_parser.set('TOTAL_TIME', langauge, f'{float(saved_times[i]) + answer}')
    except IndexError:  total_time_parser.set('TOTAL_TIME', langauge, f'{answer}')
total_time_parser.write(fp)
fp.close()
