from tkinter import Frame, BOTH
import Project.Building


class GuiElevator(Frame):

    def __init__(self, Building: Project.Building):
        super(GuiElevator, self).__init__()
        self.buildding = Building



