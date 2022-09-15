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
                on_release: app.change_screen("menucliente")

            MDIconButton:
    			id: botonAgregar
                icon: "account-plus"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.66, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("NuevoClientes")


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
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: MenuClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("Pantalla Principal")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                markup:True
        		text: "[color=#315582][b]Reuniones[/b][/color]"
                font_size: 30
        		pos_hint: {"center_x": 0.92, "center_y": 0.75}

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




<menucliente>
    name: "menucliente"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: MenuClayout
			padding: 5




            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("Clientes")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:tituloMenuCliente
                markup: True
                text: "[color=#315582][i]Menu Cliente[/i][/color]"
				font_size: 26
				pos_hint: {"center_x": 0.90, "center_y": 0.75}

    		MDRoundFlatButton:
				id: botonEditarDatosPersonales
				markup: True
				text: "[color=#315582][b]Editar Datos Personales[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.60}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("EditarClientes")

            MDRoundFlatButton:
				id: botonCasoCliente
				markup: True
				text: "[color=#315582][b]Caso[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.50}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release:
                    app.change_screen("DatosCasos")
                    app.add_datatable1()


<NuevoCliente>
    name:"NuevoClientes"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: NuevoClayout
			padding: 5


            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("Clientes")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloNC1
                markup: True
                text: "Nuevo Cliente"
                pos_hint: {"center_x": .90, "center_y": .75}
                font_size: 30

            MDLabel:
                id:NombreNC1
                markup: True
                text: "Nombre"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputNombreNC1
                pos_hint: {"center_x": .18, "center_y": .60}
                size_hint: None, None
                width: 350



            MDLabel:
                id:ApellidoNC1
                markup: True
                text: "Apellido"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputApellidoNC1
                pos_hint: {"center_x": .18, "center_y": .50}
                size_hint: None, None
                width: 350


            MDLabel:
                id:DNINC1
                markup: True
                text: "DNI"
                pos_hint: {"center_x": .5, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputDNINC1
                pos_hint: {"center_x": .18, "center_y": .40}
                size_hint: None, None
                width: 350

            MDLabel:
                id:DireccionNC1
                markup: True
                text: "Direccion"
                pos_hint: {"center_x": .5, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputDireccionNC1
                pos_hint: {"center_x": .18, "center_y": .30}
                size_hint: None, None
                width: 350

            MDLabel:
                id:TelefonoNC1
                markup: True
                text: "Telefono"
                pos_hint: {"center_x": .5, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputTelefonoNC1
                pos_hint: {"center_x": .18, "center_y": .20}
                size_hint: None, None
                width: 350

            MDLabel:
                id:EmailNC1
                markup: True
                text: "Email"
                pos_hint: {"center_x": .5, "center_y": .15}
                font_size: 16

            MDTextField:
                id: InputEmailNC1
                pos_hint: {"center_x": .18, "center_y": .10}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosNC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.05}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


<DatosCasos>
    name: "DatosCasos"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: PantallaCasoslayout
			padding: 5
            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("menucliente")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
        		id: labelCasos
        		text: "[color=#315582][u][b][i]Casos[/b][/i][/u][/color]"
        		font_size: 24
        		halign: 'center'
        		pos_hint: {"center_x": .5, "center_y": .57}
        		padding_y: 10


    		MDIconButton:
    			id: botonBorrarCasos
                icon: "trash-can"
    			size_hint: None, None
    			pos_hint: {"center_x": 0.8, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2

    		MDIconButton:
    			id: botonEditarCasos
                icon: "pencil"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.73, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("MenuCaso")

            MDIconButton:
    			id: botonAgregarCasos
                icon: "account-plus"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.66, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("NuevoCaso")


    		MDIconButton:
    			id: botonArchivarCasos
                icon: "folder"
    			size_hint: None, None
    			pos_hint: {"center_x": 0.87, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2

            AnchorLayout:
                id: data_layout1
                pos_hint: {"center_x": .5, "center_y": .3}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<NuevoCaso>
    name: "NuevoCaso"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("DatosCasos")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloCC1
                markup: True
                text: "[color=#315582][b]Nuevo Caso[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30

            MDLabel:
                id:TipoCC1
                markup: True
                text: "Tipo"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputTipoEC1
                pos_hint: {"center_x": .18, "center_y": .60}
                size_hint: None, None
                width: 350

            MDLabel:
                id:FechaInicioCC1
                markup: True
                text: "Fecha de Inicio"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaInicioCC1
                pos_hint: {"center_x": .18, "center_y": .50}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 350


            MDLabel:
                id:FechaFinCC1
                markup: True
                text: "Fecha de Finalización"
                pos_hint: {"center_x": .5, "center_y": .40}
                font_size: 16

            MDTextField:
                id: InputFechaFinCC1
                pos_hint: {"center_x": .18, "center_y": .35}
                size_hint: None, None
                helper_text: "Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 350


            MDLabel:
                id:MotivoCC1
                markup: True
                text: "Motivo"
                pos_hint: {"center_x": .5, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputMotivoCC1
                pos_hint: {"center_x": .18, "center_y": .20}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosCC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.15}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<MenuCaso>
    name: "MenuCaso"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("DatosCasos")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Menu Caso[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30


            MDRoundFlatButton:
				id: botonEditarDatosCaso
				markup: True
				text: "[color=#315582][b]Editar Datos del Caso[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.60}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Caso")

            MDRoundFlatButton:
				id: botonEditaEtapa1
				markup: True
				text: "[color=#315582][b]Etapa 2[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.50}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Etapa2")

            MDRoundFlatButton:
				id: botonEtapa2
				markup: True
				text: "[color=#315582][b]Etapa 3[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.40}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Etapa3")

            MDRoundFlatButton:
				id: botonEtapa4
				markup: True
				text: "[color=#315582][b]Etapa 4[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.30}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Etapa4")

<Etapa2>
    name:"Etapa2"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("MenuCaso")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Etapa 2[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30


            MDLabel:
                id:FirmaEC2
                markup: True
                text: "Firma"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputFirmaEC2
                pos_hint: {"center_x": .18, "center_y": .60}
                size_hint: None, None
                width: 350

            MDLabel:
                id:FechaFirmaEC2
                markup: True
                text: "Fecha de la Firma"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaFirmaEC2
                pos_hint: {"center_x": .18, "center_y": .50}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:LugarFirmaEC2
                markup: True
                text: "Lugar de la Firma"
                pos_hint: {"center_x": .5, "center_y": .40}
                font_size: 16

            MDTextField:
                id: InputLugarFirmaEC2
                pos_hint: {"center_x": .18, "center_y": .35}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosEC2
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.15}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<Etapa3>
    name:"Etapa3"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("MenuCaso")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Etapa 3[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30

            MDLabel:
                id:FechaInicioEC3
                markup: True
                text: "Fecha de inicio de la Etapa 3"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputFechaInicioEC3
                pos_hint: {"center_x": .18, "center_y": .61}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaComisionMedicaEC3
                markup: True
                text: "Fecha de Comision Medica"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaComisionMedicaEC3
                pos_hint: {"center_x": .18, "center_y": .51}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaFinEC3
                markup: True
                text: "Fecha del fin de la Etapa 3"
                pos_hint: {"center_x": .5, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputFechaInicioEC3
                pos_hint: {"center_x": .18, "center_y": .40}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:ProntoDespachoEC3
                markup: True
                text: "¿Presenta Pronto Despacho?"
                pos_hint: {"center_x": .5, "center_y": .30}
                font_size: 16

            MDTextField:
                id: InputProntoDespachoEC3
                pos_hint: {"center_x": .18, "center_y": .25}
                size_hint: None, None
                width: 350
                helper_text:"Si o No"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaDictamenEC3
                markup: True
                text: "Fecha de Dictamen"
                pos_hint: {"center_x": .5, "center_y": .15}
                font_size: 16

            MDTextField:
                id: InputFechaDictamenEC3
                pos_hint: {"center_x": .18, "center_y": .10}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaConciliacionEC3
                markup: True
                text: "Fecha de Conciliacion"
                pos_hint: {"center_x": .95, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputFechaConciliacionEC3
                pos_hint: {"center_x": .62, "center_y": .61}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDRoundFlatButton:
                id: botonGuardarDatosEC3
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.05}
                md_bg_color: 0.93, 0.69, 0.63, 0.2



<Etapa4>
    name:"Etapa4"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("MenuCaso")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Etapa 4[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30

            MDLabel:
                id:EtapaInicioEC4
                markup: True
                text: "Etapa Inicial"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16



            MDLabel:
                id:FechaEtapaInicioEC4
                markup: True
                text: "Fecha de inicio de la etapa inicial"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaEtapaInicioEC4
                pos_hint: {"center_x": .18, "center_y": .51}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:EtapaIntermediaEC4
                markup: True
                text: "Etapa Intermedia"
                pos_hint: {"center_x": .5, "center_y": .43}
                font_size: 16



            MDLabel:
                id:FechaEtapaIntermediaEC4
                markup: True
                text: "Fecha de inicio de la etapa intermedia"
                pos_hint: {"center_x": .5, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputFechaEtapaIntermediaEC4
                pos_hint: {"center_x": .18, "center_y": 31}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:EtapaFinalEC4
                markup: True
                text: "Etapa Final"
                pos_hint: {"center_x": .5, "center_y": .25}
                font_size: 16




            MDLabel:
                id:FechaEtapaFinalEC4
                markup: True
                text: "Fecha de inicio de la etapa Final"
                pos_hint: {"center_x": .5, "center_y": .15}
                font_size: 16

            MDTextField:
                id: InputFechaEtapaFinalEC4
                pos_hint: {"center_x": .18, "center_y": .11}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"


<Caso>
    name: "Caso"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("MenuCaso")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloCC1
                markup: True
                text: "[color=#315582][b]Caso[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30

            MDLabel:
                id:TipoCC1
                markup: True
                text: "Tipo"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputTipoEC1
                pos_hint: {"center_x": .18, "center_y": .60}
                size_hint: None, None
                width: 350

            MDLabel:
                id:FechaInicioCC1
                markup: True
                text: "Fecha de Inicio"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaInicioCC1
                pos_hint: {"center_x": .18, "center_y": .50}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 350


            MDLabel:
                id:FechaFinCC1
                markup: True
                text: "Fecha de Finalización"
                pos_hint: {"center_x": .5, "center_y": .40}
                font_size: 16

            MDTextField:
                id: InputFechaFinCC1
                pos_hint: {"center_x": .18, "center_y": .35}
                size_hint: None, None
                helper_text: "Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 350


            MDLabel:
                id:MotivoCC1
                markup: True
                text: "Motivo"
                pos_hint: {"center_x": .5, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputMotivoCC1
                pos_hint: {"center_x": .18, "center_y": .20}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosCC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.15}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<EditarClientes>
    name:"EditarClientes"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: EdicionClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("menucliente")

            MDRoundFlatButton:
                id: botonBuscar
                markup: True
                text: "[color=#315582][b]Buscar[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.05, "center_y": 0.85}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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
                id:TituloEC1
                markup: True
                text: "[color=#315582][b]Editar Cliente[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .75}
                font_size: 30

            MDLabel:
                id:NombreEC1
                markup: True
                text: "Nombre"
                pos_hint: {"center_x": .5, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputNombreEC1
                pos_hint: {"center_x": .18, "center_y": .60}
                size_hint: None, None
                width: 350



            MDLabel:
                id:ApellidoEC1
                markup: True
                text: "Apellido"
                pos_hint: {"center_x": .5, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputApellidoEC1
                pos_hint: {"center_x": .18, "center_y": .50}
                size_hint: None, None
                width: 350


            MDLabel:
                id:DNIEC1
                markup: True
                text: "DNI"
                pos_hint: {"center_x": .5, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputDNIEC1
                pos_hint: {"center_x": .18, "center_y": .40}
                size_hint: None, None
                width: 350

            MDLabel:
                id:DireccionEC1
                markup: True
                text: "Direccion"
                pos_hint: {"center_x": .5, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputDireccionEC1
                pos_hint: {"center_x": .18, "center_y": .30}
                size_hint: None, None
                width: 350

            MDLabel:
                id:TelefonoEC1
                markup: True
                text: "Telefono"
                pos_hint: {"center_x": .5, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputTelefonoEC1
                pos_hint: {"center_x": .18, "center_y": .20}
                size_hint: None, None
                width: 350

            MDLabel:
                id:EmailEC1
                markup: True
                text: "Email"
                pos_hint: {"center_x": .5, "center_y": .15}
                font_size: 16

            MDTextField:
                id: InputEmailEC1
                pos_hint: {"center_x": .18, "center_y": .10}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosEC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.05}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

WindowManager:
    LoginWindow:

    pantallaPrincipal:

    calendario:

    etapas:

    Etapa2:

    Etapa3:

    Etapa4:

    Caso:

    MenuCaso:

    NuevoCaso:

    DatosCasos:
        id: data_scr1

    menucliente:

    NuevoCliente:

    EditarClientes:

    ClientWindow:
        id: data_scr
"""


class LoginWindow(Screen):
    pass


class ClientWindow(Screen):
    pass

class menucliente(Screen):
    pass

class NuevoCliente(Screen):
    pass

class DatosCasos(Screen):
    pass

class Caso(Screen):
    pass

class MenuCaso(Screen):
    pass

class NuevoCaso(Screen):
    pass

class pantallaPrincipal(Screen):
    pass

class etapas(Screen):
    pass

class Etapa2 (Screen):
    pass

class Etapa3 (Screen):
    pass

class Etapa4 (Screen):
    pass

class EditarClientes(Screen):
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
        self.data_tableC = None
        self.data_tables1= None

    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def add_datatable1(self):
        self.data_tables1 = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Tipo", dp(30)),
                ("Fecha de Inicio", dp(30)),
                ("Motivo", dp(30)),
            ],
            row_data=[
                (
                    "1",
                    "Denuncia",
                    "1984-11-09",
                    "Choque",
                ),
                (
                    "2",
                    "Divorcio",
                    "2002-04-18",
                    "Disputa"
                ),
            ]
        )
        self.root.ids.data_scr1.ids.data_layout1.add_widget(self.data_tables1)

    def add_datatable(self):
        self.data_tableC = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,

            column_data=[
                ("Nombre", dp(30)),
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

            ]
        )
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tableC)

    def change_screen(self, screen: str):
        self.root.current = screen


SIC().run()
