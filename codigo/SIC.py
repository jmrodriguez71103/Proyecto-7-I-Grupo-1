from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
import webbrowser



KV = """
<LoginWindow>:
    name: "main"
	MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, .8
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

            MDIconButton:
    			id: botonVolver
                icon: "arrow-left-bold"
    			size_hint: None, None
    			pos_hint: {"center_x": 0.05, "center_y": 0.88}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("Pantalla Principal")

    		MDIconButton:
    			id: botonBorrar
                icon: "trash-can"
    			size_hint: None, None
    			pos_hint: {"center_x": 0.8, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2

    		MDIconButton:
    			id: botonEditar
                icon: "pencil"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.73, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2

    		MDIconButton:
    			id: botonArchivar
                icon: "folder"
    			size_hint: None, None
    			pos_hint: {"center_x": 0.87, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2


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

	MDLabel:
		markup: True
		text: "[i]Pantalla en progreso[/i]"
		font_size: 16
		pos_hint: {"center_x": 0.5, "center_y": 0.95}

	MDRoundFlatButton:
		id: abrir_calendario
		text: "[color=#315582][b]Seleccionar Fecha[/b][/color]"
		size_hint: None, None
		width: 100
		pos_hint: {"center_x": 0.65, "center_y": 0.5}
		md_bg_color: 0.93, 0.69, 0.63, 0.2
		on_release: root.show_date_picker()
	MDRoundFlatButton:
		id: abrir_reloj
		text: "[color=#315582][b]Seleccionar Horario[/b][/color]"
		size_hint: None, None
		width: 100
		pos_hint: {"center_x": 0.85, "center_y": 0.5}
		md_bg_color: 0.93, 0.69, 0.63, 0.2
		on_release: root.show_time_picker()

	MDLabel:
		id: R1
		text: "Reuniones"
		size_hint: None, None
		pos_hint: {"center_x": 0.25, "center_y": 0.75}

	MDLabel:
		id: fecha_R1
		text: "-"
		size_hint: None, None
		pos_hint: {"center_x": 0.35, "center_y": 0.5}

	MDLabel:
		id: hora_R1
		text: "-"
		size_hint: None, None
		pos_hint: {"center_x": 0.5, "center_y": 0.5}

	MDRoundFlatButton:
		id: boton100000
		text: "[color=#315582][b]Volver pantalla principal[/b][/color]"
		size_hint: None, None
		width: 100
		pos_hint: {"center_x": 0.5, "center_y": 0.2}
		md_bg_color: 0.93, 0.69, 0.63, 0.2
		on_release: app.root.current = "Pantalla Principal"


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
	def save_date(self,instance, value, date_range):
		self.ids.fecha_R1.text = str(value)
	#	self.ids.fecha_R1.text = f'{str(date_range[0])} - {str(date_range[-1])}'

	def save_time(self, intance, time):
		self.ids.hora_R1.text = str(time)

	def cancel_date(self, instance, value):
		self.ids.fecha_R1.text = "-"

	def cancel_time(self, instance, value):
		self.ids.hora_R1.text = "-"

	def show_date_picker(self):
		picker = MDDatePicker()
		picker.bind(on_save=self.save_date, on_cancel=self.cancel_date)
		picker.open()

	def show_time_picker(self):
		time_picker = MDTimePicker()
		time_picker.bind(time=self.save_time, on_cancel=self.cancel_time)
		time_picker.open()


class WindowManager(ScreenManager):
    pass


class SIC(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def add_datatable(self):
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,

            column_data=[
                ("Nombre", dp(20)),
                ("Apellido", dp(20)),
                ("DNI", dp(20)),
                ("Direccion", dp(30)),
                ("Telefono", dp(20)),
                ("Email", dp(30)),
                ("Tipo de caso", dp(20)),
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