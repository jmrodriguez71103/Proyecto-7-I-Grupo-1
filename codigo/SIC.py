from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.pickers import MDDatePicker
import webbrowser



KV = """
<LoginWindow>:
    name: "main"

	MDCard:
		size_hint: None, None
		size: 400, 500
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		padding: 15
		spacing: 25
		orientation: 'vertical'
		md_bg_color: 0.85, 0.8, 0.72, 1

		MDLabel:
			id: prueba
			text: "Sistema Integral de Clientes"
			font_size: 40
			halign: 'center'
			size_hint_y: None
			padding_y: 10

		Image:
			source: "logo.jpeg"
			size_hint : None, None
			pos_hint: {"center_x": 0.5}

		MDTextField:
			id: nombre
			hint_text: "Usuario"
			icon_right: "account"
			size_hint: None, None
			width: 200
			font_size: 16
			pos_hint: {"center_x": 0.5}

		MDTextField:
			id: psw
			hint_text: "Contraseña"
			icon_right: "lock"
			size_hint: None, None
			width: 200
			font_size: 16
			pos_hint: {"center_x": 0.5}

		MDRoundFlatButton:
			id: boton1
			text: "Ingresar"
			size_hint: None, None
			width: 100
			pos_hint: {"center_x": 0.5}
			on_release:
                app.change_screen("Pantalla Principal")

<pantallaPrincipal>:
	name: "Pantalla Principal"


	MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: flayout
			padding: 5



			Image:
				source: "logo.jpeg"
				size_hint : None, None
				pos_hint: {"center_x": 0.5, "center_y": 0.93}

			MDRoundFlatButton:
				id: botonUsuario
				markup: True
				text: "[color=#315582][b]Usuario[/b][/color]"
				size_hint: None, None
				width: 100
				pos_hint: {"center_x": .95, "center_y": 0.95}
				md_bg_color: 0.85, 0.8, 0.72, 0

			MDLabel:
				markup: True
				text: "[color=#315582][i]Sistema Integral[/i][/color]"
				font_size: 26
				pos_hint: {"center_x": 0.89, "center_y": 0.80}

			MDLabel:
				markup: True
				text: "[color=#315582][i]de clientes[/i][/color]"
				font_size: 26
				pos_hint: {"center_x": 0.92, "center_y": 0.75}


			MDRoundFlatButton:
				markup: True
				id: botonClientes
				text: "[color=#315582][b]Clientes[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.65}
				on_release:
                    app.change_screen("Clientes")
                    app.add_datatable()
				md_bg_color: 0.93, 0.69, 0.63, 0.2

			MDRoundFlatButton:
				id: botonEtapas
				markup: True
				text: "[color=#315582][b]Etapas[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.55}
				on_release: app.change_screen("etapas")
				md_bg_color: 0.93, 0.69, 0.63, 0.2

			MDRoundFlatButton:
				id: botonPJN
				markup: True
				text: "[color=#315582][b]Poder Judicial[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.45}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.abrirPJN()

			MDRoundFlatButton:
				id: botonMEV
				markup: True
				text: "[color=#315582][b]MEV[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.35}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.abrirMEV()

			MDRoundFlatButton:
				id: botonCalendario
				markup: True
				text: "[color=#315582][b]Calendario[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.25}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("calendario")

			MDRoundFlatButton:
				id: botonBuscar
				markup: True
				text: "[color=#315582][b]Buscar[/b][/color]"
				size_hint: None, None
				width: 100
				pos_hint: {"center_x": 0.05, "center_y": 0.95}
				md_bg_color: 0.93, 0.69, 0.63, 0.2



<ClientWindow>:
    name: "Clientes"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: flayout
			padding: 5
    		Image:
    			source: "logo.jpeg"
    			size_hint : None, None
    			pos_hint: {"center_x": 0.5, "center_y": 0.93}

    		MDRoundFlatButton:
    			id: botonUsuario
    			markup: True
    			text: "[color=#315582][b]Usuario[/b][/color]"
    			size_hint: None, None
    			width: 100
    			pos_hint: {"center_x": .95, "center_y": 0.95}
    			md_bg_color: 0.85, 0.8, 0.72, 0

    		MDLabel:
    			markup: True
    			text: "[color=#315582][i]Sistema Integral[/i][/color]"
    			font_size: 26
    			pos_hint: {"center_x": 0.89, "center_y": 0.80}

    		MDLabel:
    			markup: True
    			text: "[color=#315582][i]de clientes[/i][/color]"
    			font_size: 26
    			pos_hint: {"center_x": 0.92, "center_y": 0.75}

        	MDLabel:
        		markup: True
        		id: labelClientes
        		text: "[color=#315582][u][b][i]Clientes[/b][/i][/u][/color]"
        		font_size: 24
        		halign: 'center'
        		pos_hint: {"center_x": .5, "center_y": .57}
        		padding_y: 10

    		MDRoundFlatButton:
    			id: botonBuscar
    			markup: True
    			text: "[color=#315582][b]Buscar[/b][/color]"
    			size_hint: None, None
    			width: 100
    			pos_hint: {"center_x": 0.05, "center_y": 0.95}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2

            AnchorLayout:
                id: data_layout
                pos_hint: {"center_x": .5, "center_y": .3}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<etapas>:
	name: "etapas"

	MDLabel:
		markup: True
		text: "[i]Pantalla en progreso[/i]"
		font_size: 16
		pos_hint: {"center_x": 0.5, "center_y": 0.95}

	MDRoundFlatButton:
		id: boton100000
		text: "[color=#315582][b]Volver pantalla principal[/b][/color]"
		size_hint: None, None
		width: 100
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		md_bg_color: 0.93, 0.69, 0.63, 0.2
		on_release: app.change_screen("Pantalla Principal")

<calendario>:
	name: "calendario"



	MDRoundFlatButton:
		id: abrir_calendario
		text: "[color=#315582][b]Abrir Calendario[/b][/color]"
		size_hint: None, None
		width: 100
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		md_bg_color: 0.93, 0.69, 0.63, 0.2
		on_release: root.show_date_picker()

	MDLabel:
		id: text_calendario
		text: ""
		size_hint: None, None
		pos_hint: {"center_x": 0.5, "center_y": 0.35}

	MDRoundFlatButton:
		id: boton100000
		text: "[color=#315582][b]Volver pantalla principal[/b][/color]"
		size_hint: None, None
		width: 100
		pos_hint: {"center_x": 0.5, "center_y": 0.2}
		md_bg_color: 0.93, 0.69, 0.63, 0.2
		on_release: app.change_screen("Pantalla Principal")


WindowManager:
    LoginWindow:

    pantallaPrincipal:

    calendario:

    etapas:

    ClientWindow:
        id: data_scr
"""


class LoginWindow(Screen):
    pass


class ClientWindow(Screen):
    pass


class pantallaPrincipal(Screen):
    pass

class etapas(Screen):
    pass

class calendario(Screen):
#	def get_date(self, date):
#		self.ids.ejemplo_id.text
#		print(date)

	#Click OK
	def on_save(self,instance, value, date_range):
		self.ids.text_calendario.text = str(value)
	#	self.ids.text_calendario.text = f'{str(date_range[0])} - {str(date_range[-1])}'

	#Click Cancel
	def on_cancel(self, instance, value, date_range):
		self.ids.text_calendario.text = "--"

	def show_date_picker(self):
		picker = MDDatePicker()
		picker.bind(on_save=self.on_save, on_cancel=self.on_cancel)
		picker.open()


class WindowManager(ScreenManager):
    pass


class SIC(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def build(self):
        return Builder.load_string(KV)

    def add_datatable(self):
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",

            column_data=[
                ("Nombre", dp(20)),
                ("Apellido", dp(20)),
                ("DNI", dp(10)),
                ("Direccion", dp(30)),
                ("Telefono", dp(20)),
                ("Email", dp(30)),
                ("Tipo de caso", dp(15)),
                ("Motivo", dp(30))
            ],
            row_data=[
                (
                    "Juan",
                    "Rodriguez",
                    "45320127",
                    "Calle 1 N1",
                    "1135432564",
                    "juan@gmail.com",
                    "Divorcio",
                    "Pelea",

                ),
                (
                    "Pepe",
                    "Rodriguez",
                    "45322127",
                    "Calle 2 N2",
                    "1135489764",
                    "pepe@gmail.com",
                    "Denuncia",
                    "Choque"
                ),
            ]
        )
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)

    def change_screen(self, screen: str):
        self.root.current = screen


SIC().run()
