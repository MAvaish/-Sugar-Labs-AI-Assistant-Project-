from gi.repository import Gtk
from ai_assistant import AIAssistant

class Toolbar:
    def __init__(self, activity):
        self._activity = activity
        self.ai = AIAssistant()
        ai_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_LIGHTBULB)
        ai_button.set_tooltip_text("AI Help")
        ai_button.connect("clicked", self._on_ai_clicked)
        self.insert(ai_button, -1)

    def insert(self, tool_button, position):
        # Assuming this method is part of the Toolbar class
        # Add the tool_button to the toolbar at the specified position
        pass

    def _on_ai_clicked(self, button):
        buffer = self._activity.textview.get_buffer()
        start, end = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        
        suggestion = self.ai.get_suggestion(text)
        
        dialog = Gtk.MessageDialog(
            parent=self._activity,
            buttons=Gtk.ButtonsType.OK,
            text=suggestion
        )
        dialog.run()
        dialog.destroy()