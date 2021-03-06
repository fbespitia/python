import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class StackWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Stack Demo")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        

        checkbutton = Gtk.CheckButton("check button")
        stack.add_titled(checkbutton, "check", "check button")

        
        label = Gtk.Label()
        label.set_markup("<big> A fancy label </big>")
        stack.add_titled(label,"label", "A label")

        button = Gtk.Button(label="Hello")
        stack.add_titled(button,"My button", "example")
        
        
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        
win = StackWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
        
        
