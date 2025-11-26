import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from functools import partial
import os

# Assuming crud.operations handles the database logic
from crud.operations import crear, leer, actualizar, eliminar

from kivy.lang import Builder

# Apply a global gray theme
Builder.load_string('''
<Label>:
    color: (1, 1, 1, 1)  # White text

<Button>:
    background_color: (0.3, 0.3, 0.3, 1)  # Dark gray background
    color: (1, 1, 1, 1)  # White text for contrast

<TextInput>:
    background_color: (0.9, 0.9, 0.9, 1)  # Light gray background
    foreground_color: (0.2, 0.2, 0.2, 1)  # Dark gray text

<Popup>:
    background_color: (0.4, 0.4, 0.4, 1) # Dark gray for popup background
    
<BoxLayout>:
    background_color: (0.5, 0.5, 0.5, 1)

''')

DEFAULT_IMAGE_PATH = "contactimg.png"

class CrudApp(App):
    def build(self):
        self.title = "Agenda de Contactos"
        Window.clearcolor = (0.5, 0.5, 0.5, 1)
        Window.size = (600, 700)

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input layout - COMPACTO
        input_layout = GridLayout(cols=2, spacing=5, size_hint_y=None, height=110)

        input_layout.add_widget(Label(text="ID:", size_hint_x=0.3))
        self.id_input = TextInput(multiline=False, size_hint_x=0.7, height=35, size_hint_y=None)
        input_layout.add_widget(self.id_input)

        input_layout.add_widget(Label(text="Nombre:", size_hint_x=0.3))
        self.name_input = TextInput(multiline=False, size_hint_x=0.7, height=35, size_hint_y=None)
        input_layout.add_widget(self.name_input)

        input_layout.add_widget(Label(text="Teléfono:", size_hint_x=0.3))
        self.phone_input = TextInput(multiline=False, size_hint_x=0.7, height=35, size_hint_y=None)
        input_layout.add_widget(self.phone_input)

        main_layout.add_widget(input_layout)

        # Button layout - COMPACTO
        button_layout = BoxLayout(spacing=5, size_hint_y=None, height=40)
        
        create_button = Button(text="Crear")
        create_button.bind(on_press=self.create_contact)
        button_layout.add_widget(create_button)

        read_button = Button(text="Listar")
        read_button.bind(on_press=self.read_contacts)
        button_layout.add_widget(read_button)

        update_button = Button(text="Actualizar")
        update_button.bind(on_press=self.update_contact)
        button_layout.add_widget(update_button)

        delete_button = Button(text="Eliminar")
        delete_button.bind(on_press=self.delete_contact)
        button_layout.add_widget(delete_button)
        
        main_layout.add_widget(button_layout)

        # Display area - OCUPA TODO EL ESPACIO RESTANTE
        self.contact_list_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.contact_list_layout.bind(minimum_height=self.contact_list_layout.setter('height'))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.contact_list_layout)
        main_layout.add_widget(scroll_view)

        # Load contacts on start
        self.read_contacts()

        return main_layout

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="Cerrar", size_hint_y=None, height=40)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def show_contact_details(self, contact, instance):
        """Shows a popup with the full details of a contact."""
        contact_id, name, phone, image_path = contact
        
        popup_content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # SIEMPRE usa la imagen por defecto
        contact_image = Image(source=DEFAULT_IMAGE_PATH, size_hint_y=0.6)
        popup_content.add_widget(contact_image)

        # Add Details
        details_layout = GridLayout(cols=2, size_hint_y=0.3)
        details_layout.add_widget(Label(text="ID:", color=(1, 1, 1, 1)))
        details_layout.add_widget(Label(text=str(contact_id), color=(1, 1, 1, 1)))
        details_layout.add_widget(Label(text="Nombre:", color=(1, 1, 1, 1)))
        details_layout.add_widget(Label(text=name, color=(1, 1, 1, 1)))
        details_layout.add_widget(Label(text="Teléfono:", color=(1, 1, 1, 1)))
        details_layout.add_widget(Label(text=phone, color=(1, 1, 1, 1)))
        popup_content.add_widget(details_layout)

        # Close button
        close_button = Button(text="Cerrar", size_hint_y=0.1)
        popup_content.add_widget(close_button)
        
        popup = Popup(title="Detalles del Contacto", content=popup_content, size_hint=(0.8, 0.7))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def create_contact(self, instance):
        cid = self.id_input.text
        name = self.name_input.text
        phone = self.phone_input.text
        if not cid or not name or not phone:
            self.show_popup("Error de Validación", "Todos los campos son obligatorios para crear.")
            return
        
        # SIEMPRE usa la imagen por defecto
        crear(cid, name, phone, DEFAULT_IMAGE_PATH)
        
        self.clear_inputs()
        self.read_contacts()

    def read_contacts(self, instance=None):
        # Clear existing widgets
        self.contact_list_layout.clear_widgets()
        
        contacts = leer()
        for contact in contacts:
            contact_id, name, phone, image_path = contact
            
            # Create a button container
            contact_button = Button(size_hint_y=None, height=60)
            
            # Create layout inside button using canvas
            item_layout = BoxLayout(spacing=10, size_hint_y=None, height=60, pos=contact_button.pos, size=contact_button.size)
            
            # SIEMPRE usa la imagen por defecto
            img = Image(source=DEFAULT_IMAGE_PATH, size_hint_x=None, width=50, allow_stretch=True, keep_ratio=True)
            item_layout.add_widget(img)
            
            # Name Label
            name_label = Label(text=name, halign='left', valign='middle')
            name_label.bind(size=name_label.setter('text_size'))
            item_layout.add_widget(name_label)
            
            # Update item_layout position when button moves
            contact_button.bind(pos=item_layout.setter('pos'), size=item_layout.setter('size'))
            
            # Add layout to button
            contact_button.add_widget(item_layout)
            
            # Bind the button to show details
            contact_button.bind(on_press=partial(self.show_contact_details, contact))
            
            self.contact_list_layout.add_widget(contact_button)

    def update_contact(self, instance):
        cid = self.id_input.text
        name = self.name_input.text
        phone = self.phone_input.text
        if not cid:
            self.show_popup("Error de Validación", "El campo 'ID' es obligatorio para actualizar.")
            return
        if not name and not phone:
            self.show_popup("Error de Validación", "Debe proporcionar un nuevo nombre o teléfono para actualizar.")
            return
        if actualizar(cid, name or None, phone or None):
            self.clear_inputs()
            self.read_contacts()
        else:
            self.show_popup("Error", f"No se encontró ningún contacto con el ID '{cid}'.")

    def delete_contact(self, instance):
        cid = self.id_input.text
        if not cid:
            self.show_popup("Error de Validación", "El campo 'ID' es obligatorio para eliminar.")
            return
        if eliminar(cid):
            self.clear_inputs()
            self.read_contacts()
        else:
            self.show_popup("Error", f"No se encontró ningún contacto con el ID '{cid}'.")

    def clear_inputs(self):
        self.id_input.text = ""
        self.name_input.text = ""
        self.phone_input.text = ""

if __name__ == "__main__":
    CrudApp().run()