import tkinter as tk
from tkinter import messagebox
import db  # Integrates with your database module

class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, padx=20, pady=20)
        self.parent = parent
        self.parent.title("Player Management") 
        self.pack()

        # StringVars to manage entry data
        self.player_id = tk.StringVar()
        self.bat_order = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.position = tk.StringVar()
        self.at_bats = tk.StringVar()
        self.hits = tk.StringVar()
        self.batting_avg = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        # Player ID row with "Get Player" button
        tk.Label(self, text="Player ID:").grid(column=0, row=0, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.player_id).grid(column=1, row=0, padx=5)
        tk.Button(self, text="Get Player", command=self.get_player).grid(column=2, row=0, padx=5) 

        # Data Fields
        #  bat order text
        tk.Label(self, text="Bat Order:").grid(column=0, row=1, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.bat_order).grid(column=1, row=1)

# first name text 
        tk.Label(self, text="First Name:").grid(column=0, row=2, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.first_name).grid(column=1, row=2)

# last name text
        tk.Label(self, text="Last Name:").grid(column=0, row=3, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.last_name).grid(column=1, row=3)

# position text field
        tk.Label(self, text="Position:").grid(column=0, row=4, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.position).grid(column=1, row=4)

#  at bats feild 
        tk.Label(self, text="At Bats:").grid(column=0, row=5, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.at_bats).grid(column=1, row=5)


#  hits field
        tk.Label(self, text="Hits:").grid(column=0, row=6, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.hits).grid(column=1, row=6)
        
        # Batting Average (Read-only)
        tk.Label(self, text="Batting Avg:").grid(column=0, row=7, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.batting_avg, state="readonly").grid(column=1, row=7)

       # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.grid(column=1, row=8, pady=15, sticky=tk.W)
        
        #  save chnages button
        tk.Button(btn_frame, text="Save Changes", command=self.save_changes).pack(side=tk.LEFT, padx=5)
        #  DELETE BUTTON
        tk.Button(btn_frame, text="Delete Player", command=self.delete_player).pack(side=tk.LEFT, padx=5)
        
        # cancel button
        tk.Button(btn_frame, text="Cancel", command=self.cancel_changes).pack(side=tk.LEFT)

    def get_player(self):
        try:
            
            p_id = int(self.player_id.get())
            player = db.get_player(p_id) 
            
            if player:
                # Map tuple indices to fields based on Player table structure
                self.bat_order.set(player[1])
                self.first_name.set(player[2])
                self.last_name.set(player[3])
                self.position.set(player[4])
                self.at_bats.set(player[5])
                self.hits.set(player[6])
                
                ab = int(player[5])
                h = int(player[6])
                avg = h / ab if ab > 0 else 0.0
                self.batting_avg.set(f"{avg:.3f}")
            else:
                messagebox.showerror("Error", "Player ID not found.") 
                self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric Player ID.")

    def save_changes(self):
        try:
            p_id = int(self.player_id.get())
# check if player exsits
            existing_player = db.get_player(p_id)

            b_order = int(self.bat_order.get())
            f_name = self.first_name.get()
            l_name = self.last_name.get()
            pos = self.position.get()
            ab = int(self.at_bats.get())
            h = int(self.hits.get())
            
            if existing_player:
#  update exsisting player
                db.update_player(p_id, b_order, f_name, l_name, pos, ab, h)
                messagebox.showinfo("Success", "Player updated.")
            else:
                db.add_player(p_id, b_order, f_name, l_name, pos, ab, h)
                messagebox.showinfo("Success", "New player added to database.")
                
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Please ensure ID, Bat Order, At Bats, and Hits are numbers.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save to database: {e}")

    #  function to delete player 
    def delete_player(self):
        """Deletes the player currently identified by the Player ID field"""
        try:
            p_id_str = self.player_id.get()
            if not p_id_str:
                messagebox.showerror("Error", "Please enter a Player ID to delete.")
                return

            p_id = int(p_id_str)
            
            # Confirm with the user before deleting
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Player ID {p_id}?")
            
            if confirm:
                # Check if player exists first
                player = db.get_player(p_id)
                if player:
                    db.delete_player(p_id)
                    messagebox.showinfo("Success", "Player deleted from database.")
                    self.clear_fields()
                else:
                    messagebox.showerror("Error", "Player ID not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Player ID. Please enter a number.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete: {e}")

    def cancel_changes(self):
        if self.player_id.get():
            self.get_player() 
        else:
            self.clear_fields()

    def clear_fields(self):
        for var in [self.player_id, self.first_name, self.last_name, 
                    self.position, self.at_bats, self.hits, 
                    self.bat_order, self.batting_avg]:
            var.set("")