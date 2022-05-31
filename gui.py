from textwrap import fill
import tkinter
import customtkinter
from pip import main
import databases
from tkinter import ANCHOR, CENTER, ttk


class GUI(customtkinter.CTk):
    
    WIDTH = 600
    HEIGHT = 500

    def __init__(self) -> None:
        super().__init__()

        self.geometry(f"{GUI.WIDTH}x{GUI.HEIGHT}")
        self.resizable(False,False)
        self.title("VIDE-REM-4U")

        # ============ left side ============

        self.frame_left = customtkinter.CTkFrame(
                                                  self,
                                                  height=GUI.HEIGHT
                                                  )
        self.frame_left.place(
                              x=0, 
                              y=0,
                              anchor="nw"
                              )

        LEFT_FRAME_MIDLE_X = self.frame_left.current_width/2
        LEFT_FRAME_MIDLE_Y = self.frame_left.current_height/2

        self.type_selector = ttk.Combobox(
                                          self.frame_left ,
                                          values=databases.weapon_data("name"),
                                          background="cyan",
                                          state="readonly",
                                          justify="center"
                                          )

        self.type_selector.place(x=LEFT_FRAME_MIDLE_X,
                                 y=LEFT_FRAME_MIDLE_Y-50,
                                 anchor=CENTER
                                 )
        self.type_selector.current(0)

        self.left_button = customtkinter.CTkButton(
                                                   self.frame_left,
                                                   command=self.create_weapon_selection_window,
                                                   text="CONFIGURE"
                                                   )
        self.left_button.place(
            x = LEFT_FRAME_MIDLE_X,
            y = LEFT_FRAME_MIDLE_Y-10,
            anchor = tkinter.CENTER
            )



        # ============ midle side ============

        self.frame_midle = customtkinter.CTkFrame(
                                                  self,
                                                  height=GUI.HEIGHT*0.96,
                                                  width=180
                                                  )
        self.frame_midle.place(
                              x=GUI.WIDTH/2,
                              y=GUI.HEIGHT/2,
                              anchor=tkinter.CENTER
                              )

        


        # ============ rigth side ============

        self.frame_rigth = customtkinter.CTkFrame(self,height=GUI.HEIGHT)
        self.frame_rigth.place(
                               x=GUI.WIDTH,
                               anchor="ne"
                               )


    def create_weapon_selection_window(self):
                WIDTH = 300
                HEIGHT = 450

                window = customtkinter.CTkToplevel(self)
                window.geometry(f"{WIDTH}x{HEIGHT}")
                window.resizable(False,False)
                window.title('Fist Weapon')

                frame = customtkinter.CTkFrame(window,width=WIDTH-20,height=HEIGHT-20).place(
                    x=WIDTH/2,
                    y=HEIGHT/2,
                    anchor="center"
                    )











if __name__ == "__main__":
    app = GUI()
    app.mainloop()


