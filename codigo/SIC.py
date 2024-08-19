from kivy.config import Config
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton
import webbrowser
from kivymd.uix.menu import MDDropdownMenu
import mysql.connector as mysql
import pandas as pd
import datetime
import os


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
		pos_hint: {"center_x": .5, "center_y": 0.5}
		padding: 15
		spacing: 25
		orientation: 'vertical'
		md_bg_color: 0.85, 0.8, 0.72, 1

		MDLabel:
			id: prueba
            markup: True
			text: "[color=#315582]Sistema Integral de Clientes[/color]"
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
            password: True
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
                app.login()

<pantallaPrincipalAdmin>:
	name: "Pantalla Principal Admin"
    id: pp

	MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: flayout
			padding: 5

            MDRoundFlatButton:
                id: botonregistro
                markup: True
                text: "[color=#315582][b]Registro de Usuario[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.1, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("registro")

			Image:
				source: "logo.jpeg"
				size_hint : None, None
				pos_hint: {"center_x": 0.5, "center_y": 0.93}

			MDRoundFlatButton:
				id: botonUsuario_ppA
				markup: True
				text: "[color=#315582][b]Usuario[/b][/color]"
				size_hint: None, None
				width: 100
				pos_hint: {"center_x": .95, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.dropdown_pp()

			MDLabel:
				markup: True
				text: "[color=#315582][i]Sistema Integral[/i][/color]"
				font_size: 26
				pos_hint: {"center_x": 0.93, "center_y": 0.80}

			MDLabel:
				markup: True
				text: "[color=#315582][i]de clientes[/i][/color]"
				font_size: 26
				pos_hint: {"center_x": 0.955, "center_y": 0.75}


			MDRoundFlatButton:
				markup: True
				id: botonClientes
				text: "[color=#315582][b]Clientes[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.65}
				on_release:
				md_bg_color: 0.93, 0.69, 0.63, 0.2

			MDRoundFlatButton:
				id: botonEtapas
				markup: True
				text: "[color=#315582][b]Etapas[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.55}
				on_release:
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
				text: "[color=#315582][b]Reuniones[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.25}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("calendario")


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
				id: botonUsuario_pp
				markup: True
				text: "[color=#315582][b]Usuario[/b][/color]"
				size_hint: None, None
				width: 100
				pos_hint: {"center_x": .95, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.dropdown_pp()


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
				text: "[color=#315582][b]Reuniones[/b][/color]"
				font_size: 20
				size_hint: .2, None
				pos_hint: {"center_x": 0.5, "center_y": 0.25}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release:
                    app.change_screen("calendario")
                    app.mostrarReuniones()




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
    			pos_hint: {"center_x": 0.87, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.mostraralerta()

    		MDIconButton:
    			id: botonEditar
                icon: "pencil"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.80, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.Menucliente()

            MDIconButton:
    			id: botonAgregar
                icon: "account-plus"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.73, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("NuevoClientes")


            AnchorLayout:
                id: data_layout
                pos_hint: {"center_x": .5, "center_y": .3}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<etapas>:
	name: "etapas"
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
                on_release: app.change_screen("Pantalla Principal")

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDIconButton:
    			id: botonEditar
                icon: "pencil"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.73, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.menucaso()

            MDRoundFlatButton:
        		id: botonLlamarEtapas
        		text: "[color=#315582][b]Seleccione una Etapa[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.5, "center_y": 0.65}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release: app.dropdown()

            AnchorLayout:
                id: data_layout2
                pos_hint: {"center_x": .5, "center_y": .3}
                md_bg_color: 0.93, 0.69, 0.63, 0.2


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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}



            MDLabel:
        		id: infoFecha
                markup:True
        		text: "[color=#315582][b]Fecha[/b][/color]"
                font_size: 25
        		pos_hint: {"center_x": 0.9, "center_y": 0.55}

            MDLabel:
        		id: infoHora
                markup:True
        		text: "[color=#315582][b]Hora[/b][/color]"
                font_size: 25
        		pos_hint: {"center_x": 1.1, "center_y": 0.55}


        	MDTextField:
                id: InputFechaR1
                pos_hint: {"center_x": .45, "center_y": .50}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 100



        	MDTextField:
                id: InputHoraR1
                pos_hint: {"center_x": .65, "center_y": .50}
                size_hint: None, None
                helper_text:"Hora:Minutos:Segundos"
                helper_text_mode: "persistent"
                width: 100

        	MDLabel:
        		id: r
                markup:True
        		text: "[color=#315582][b]Reuniones[/b][/color]"
                font_size: 30
        		pos_hint: {"center_x": 0.93, "center_y": 0.75}

        	MDLabel:
        		id: fecha_R1
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.1, "center_y": 0.5}

        	MDLabel:
        		id: hora_R1
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.3, "center_y": 0.5}

        	MDRaisedButton:
        		id: borrar_R1
        		text: "[color=#315582][b]Borrar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.95, "center_y": 0.5}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.borrar_R1()
                    app.mostrarR1()

            MDRaisedButton:
        		id: guardar_R1
        		text: "[color=#315582][b]Guardar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.85, "center_y": 0.5}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.guardar_R1()
                    app.mostrarR1()

        	MDTextField:
                id: InputFechaR2
                pos_hint: {"center_x": .45, "center_y": .40}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 100

        	MDTextField:
                id: InputHoraR2
                pos_hint: {"center_x": .65, "center_y": .40}
                size_hint: None, None
                helper_text:"Hora:Minutos:Segundos"
                helper_text_mode: "persistent"
                width: 100

        	MDLabel:
        		id: fecha_R2
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.1, "center_y": 0.4}

        	MDLabel:
        		id: hora_R2
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.3, "center_y": 0.4}

        	MDRaisedButton:
        		id: borrar_R2
        		text: "[color=#315582][b]Borrar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.95, "center_y": 0.4}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.borrar_R2()
                    app.mostrarR2()

            MDRaisedButton:
        		id: guardar_R2
        		text: "[color=#315582][b]Guardar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.85, "center_y": 0.4}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.guardar_R2()
                    app.mostrarR2()

        	MDTextField:
                id: InputFechaR3
                pos_hint: {"center_x": .45, "center_y": .30}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 100

        	MDTextField:
                id: InputHoraR3
                pos_hint: {"center_x": .65, "center_y": .30}
                size_hint: None, None
                helper_text:"Hora:Minutos:Segundos"
                helper_text_mode: "persistent"
                width: 100

        	MDLabel:
        		id: fecha_R3
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.1, "center_y": 0.3}

        	MDLabel:
        		id: hora_R3
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.3, "center_y": 0.3}

        	MDRaisedButton:
        		id: borrar_R3
        		text: "[color=#315582][b]Borrar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.95, "center_y": 0.3}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.borrar_R3()
                    app.mostrarR3()

            MDRaisedButton:
        		id: guardar_R3
        		text: "[color=#315582][b]Guardar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.85, "center_y": 0.3}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.guardar_R3()
                    app.mostrarR3()


        	MDTextField:
                id: InputFechaR4
                pos_hint: {"center_x": .45, "center_y": .20}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 100

        	MDTextField:
                id: InputHoraR4
                pos_hint: {"center_x": .65, "center_y": .20}
                size_hint: None, None
                helper_text:"Hora:Minutos:Segundos"
                helper_text_mode: "persistent"
                width: 100

        	MDLabel:
        		id: fecha_R4
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.1, "center_y": 0.2}

        	MDLabel:
        		id: hora_R4
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.3, "center_y": 0.2}

        	MDRaisedButton:
        		id: borrar_R4
        		text: "[color=#315582][b]Borrar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.95, "center_y": 0.2}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.borrar_R4()
                    app.mostrarR4()

            MDRaisedButton:
        		id: guardar_R4
        		text: "[color=#315582][b]Guardar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.85, "center_y": 0.2}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.guardar_R4()
                    app.mostrarR4()


        	MDTextField:
                id: InputFechaR5
                pos_hint: {"center_x": .45, "center_y": .10}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 100

        	MDTextField:
                id: InputHoraR5
                pos_hint: {"center_x": .65, "center_y": .10}
                size_hint: None, None
                helper_text:"Hora:Minutos:Segundos"
                helper_text_mode: "persistent"
                width: 100

        	MDLabel:
        		id: fecha_R5
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.1, "center_y": 0.1}

        	MDLabel:
        		id: hora_R5
        		text: "-"
        		size_hint: None, None
        		pos_hint: {"center_x": 0.3, "center_y": 0.1}

        	MDRaisedButton:
        		id: borrar_R5
        		text: "[color=#315582][b]Borrar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.95, "center_y": 0.1}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.borrar_R5()
                    app.mostrarR5()

            MDRaisedButton:
        		id: guardar_R5
        		text: "[color=#315582][b]Guardar[/b][/color]"
        		size_hint: None, None
        		width: 100
        		pos_hint: {"center_x": 0.85, "center_y": 0.1}
        		md_bg_color: 0.93, 0.69, 0.63, 0.2
        		on_release:
                    app.guardar_R5()
                    app.mostrarR5()


        	MDRoundFlatButton:
		        id: boton_borrar
		        markup: True
		        text: "[color=#315582][b]Borrar Todo[/b][/color]"
		        size_hint: None, None
		        width: 100
		        pos_hint: {"center_x": .95, "center_y": 0.65}
		        md_bg_color: 0.85, 0.8, 0.72, 0
		        on_press:
                    app.borrar_r()
                    app.mostrarReuniones()





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
                on_release:
                    app.change_screen("Clientes")
                    app.add_datatable()
            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDRoundFlatButton:
                id: botonvolverPP
                markup: True
                text: "[color=#315582][b]Volver a Página Principal[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": .10, "center_y": 0.85}
                md_bg_color: 0.85, 0.8, 0.72, 0
                on_release:
                    app.change_screen("Pantalla Principal")


            MDLabel:
                id:tituloMenuCliente
                markup: True
                text: "[color=#315582][i]Menu Cliente[/i][/color]"
				font_size: 26
				pos_hint: {"center_x": 0.92, "center_y": 0.75}

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
				text: "[color=#315582][b]Casos[/b][/color]"
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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDLabel:
                id:TituloNC1
                markup: True
                text: "Nuevo Cliente"
                pos_hint: {"center_x": .90, "center_y": .75}
                font_size: 30

            MDLabel:
                id:NombreNC1
                markup: True
                text: "Nombre y Apellido"
                pos_hint: {"center_x": .82, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputNombreNC1
                pos_hint: {"center_x": .5, "center_y": .60}
                size_hint: None, None
                width: 350


            MDLabel:
                id:DNINC1
                markup: True
                text: "DNI"
                pos_hint: {"center_x": .82, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputDNINC1
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: None, None
                width: 350

            MDLabel:
                id:DireccionNC1
                markup: True
                text: "Direccion"
                pos_hint: {"center_x": .82, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputDireccionNC1
                pos_hint: {"center_x": .5, "center_y": .40}
                size_hint: None, None
                width: 350

            MDLabel:
                id:TelefonoNC1
                markup: True
                text: "Telefono"
                pos_hint: {"center_x": .82, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputTelefonoNC1
                pos_hint: {"center_x": .5, "center_y": .30}
                size_hint: None, None
                width: 350

            MDLabel:
                id:EmailNC1
                markup: True
                text: "Email"
                pos_hint: {"center_x": .82, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputEmailNC1
                pos_hint: {"center_x": .5, "center_y": .20}
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
                on_release:
                    app.nuevocliente()
                    app.change_screen("Clientes")
                    app.add_datatable()


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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}



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
                on_release:
                    app.mostratalerta1()

    		MDIconButton:
    			id: botonEditarCasos
                icon: "pencil"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.73, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.menucaso()

            MDIconButton:
    			id: botonAgregarCasos
                icon: "account-plus"
    			size_hint: None, None
                width: 30
    			pos_hint: {"center_x": 0.66, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("nuevocaso")


    		MDIconButton:
    			id: botonArchivarCasos
                icon: "folder"
    			size_hint: None, None
    			pos_hint: {"center_x": 0.87, "center_y": 0.57}
    			md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release:
                    app.archivarcaso()

            AnchorLayout:
                id: data_layout1
                pos_hint: {"center_x": .5, "center_y": .3}
                md_bg_color: 0.93, 0.69, 0.63, 0.2

<NuevoCaso>
    name: "nuevocaso"
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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDLabel:
                id:TituloCC1
                markup: True
                text: "[color=#315582][b]Nuevo Caso[/b][/color]"
                pos_hint: {"center_x": .94, "center_y": .75}
                font_size: 30

            MDLabel:
                id:TipoCC1
                markup: True
                text: "Tipo"
                pos_hint: {"center_x": .87, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputTipoCC1
                pos_hint: {"center_x": .5, "center_y": .60}
                size_hint: None, None
                width: 350

            MDLabel:
                id:FechaInicioCC1
                markup: True
                text: "Fecha de Inicio"
                pos_hint: {"center_x": .87, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaInicioCC1
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 350


            MDLabel:
                id:MotivoCC1
                markup: True
                text: "Motivo"
                pos_hint: {"center_x": .87, "center_y": .40}
                font_size: 16

            MDTextField:
                id: InputMotivoCC1
                pos_hint: {"center_x": .5, "center_y": .35}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosCC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.10}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release:
                    app.nuevocaso()
                    app.change_screen("DatosCasos")
                    app.add_datatable1()

<VerCaso>
    name: "VerCaso"
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
                on_release:
                    app.change_screen("MenuCaso")

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDLabel:
                id:TituloVC1
                markup: True
                text: "[color=#315582][b]Caso[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30

            MDLabel:
                id: VerTipo
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .50, "center_y": .65}
                font_size: 25

            MDLabel:
                id: VerFechaInicio
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .50, "center_y": .55}
                font_size: 25

            MDLabel:
                id: VerMotivo
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .50, "center_y": .45}
                font_size: 25

            MDLabel:
                id: VerFirma
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .50, "center_y": .35}
                font_size: 25

            MDLabel:
                id: VerFechaFirma
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .50, "center_y": .25}
                font_size: 25

            MDLabel:
                id: VerLugarFirma
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .50, "center_y": .15}
                font_size: 25

            MDLabel:
                id: VerFechaInicioE3
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .65}
                font_size: 25

            MDLabel:
                id: VerFechaCM
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .55}
                font_size: 25

            MDLabel:
                id: VerFechaFinE3
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .45}
                font_size: 25


            MDLabel:
                id: VerPPD
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .35}
                font_size: 25

            MDLabel:
                id: VerFechaD
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .25}
                font_size: 25

            MDLabel:
                id: VerFechaCon
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .15}
                font_size: 25

            MDLabel:
                id: VerEtapaIE4
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": 1.3, "center_y": .65}
                font_size: 25

            MDLabel:
                id: VerFechaEtapaIE4
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": 1.3, "center_y": .55}
                font_size: 25

            MDLabel:
                id: VerEtapaInterE4
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": 1.3, "center_y": .45}
                font_size: 25

            MDLabel:
                id: VerFechaEtapaInterE4
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": 1.3, "center_y": .35}
                font_size: 25

            MDLabel:
                id: VerEtapaFE4
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": 1.3, "center_y": .25}
                font_size: 25

            MDLabel:
                id: VerFechaEtapaFE4
                markup: True
                text: "[color=#315582][b]-[/b][/color]"
                pos_hint: {"center_x": 1.3, "center_y": .15}
                font_size: 25


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
                on_release:
                    app.change_screen("DatosCasos")
                    app.add_datatable1()

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDRoundFlatButton:
                id: botonvolverPP
                markup: True
                text: "[color=#315582][b]Volver a Página Principal[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": .10, "center_y": 0.85}
                md_bg_color: 0.85, 0.8, 0.72, 0
                on_release:
                    app.change_screen("Pantalla Principal")

            MDLabel:
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Menu Caso[/b][/color]"
                pos_hint: {"center_x": .91, "center_y": .75}
                font_size: 30

            MDRoundFlatButton:
				id: botonVerDatosCaso
				markup: True
				text: "[color=#315582][b]Ver Datos del Caso[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.60}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release:
                    app.change_screen("VerCaso")
                    app.MostrarCaso()

            MDRoundFlatButton:
				id: botonEditarDatosCaso
				markup: True
				text: "[color=#315582][b]Editar Datos del Caso[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.50}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Caso")

            MDRoundFlatButton:
				id: botonEditaEtapa1
				markup: True
				text: "[color=#315582][b]Etapa 2[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.40}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Etapa2")

            MDRoundFlatButton:
				id: botonEtapa2
				markup: True
				text: "[color=#315582][b]Etapa 3[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.30}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Etapa3")

            MDRoundFlatButton:
				id: botonEtapa4
				markup: True
				text: "[color=#315582][b]Etapa 4[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.20}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.change_screen("Etapa4")

            MDRoundFlatButton:
				id: botonEtapafechafin
				markup: True
				text: "[color=#315582][b]Establecer Fecha Fin[/b][/color]"
				font_size: 20
				size_hint: .3, None
				pos_hint: {"center_x": 0.5, "center_y": 0.10}
				md_bg_color: 0.93, 0.69, 0.63, 0.2
				on_release: app.fechafin()

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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


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
                pos_hint: {"center_x": .87, "center_y": .65}
                font_size: 16

            MDCheckbox:
                id: CheckboxFirma
                pos_hint: {"center_x": .7, "center_y": .65}
                height: 50
                width: 50
                on_active: app.check(*args)

            MDLabel:
                id:FechaFirmaEC2
                markup: True
                text: "Fecha de la Firma"
                pos_hint: {"center_x": .87, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaFirmaEC2
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:LugarFirmaEC2
                markup: True
                text: "Lugar de la Firma"
                pos_hint: {"center_x": .87, "center_y": .40}
                font_size: 16

            MDTextField:
                id: InputLugarFirmaEC2
                pos_hint: {"center_x": .5, "center_y": .35}
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
                on_release:
                    app.GuardarE2()
                    app.change_screen("MenuCaso")

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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDLabel:
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Etapa 3[/b][/color]"
                pos_hint: {"center_x": .94, "center_y": .75}
                font_size: 30

            MDLabel:
                id:FechaInicioEC3
                markup: True
                text: "Fecha de inicio de la Etapa 3"
                pos_hint: {"center_x": .55, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputFechaInicioEC3
                pos_hint: {"center_x": .23, "center_y": .60}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaComisionMedicaEC3
                markup: True
                text: "Fecha de Comision Medica"
                pos_hint: {"center_x": .55, "center_y": .50}
                font_size: 16

            MDTextField:
                id: InputFechaComisionMedicaEC3
                pos_hint: {"center_x": .23, "center_y": .45}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaFinEC3
                markup: True
                text: "Fecha del fin de la Etapa 3"
                pos_hint: {"center_x": .55, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputFechaFinEC3
                pos_hint: {"center_x": .23, "center_y": .30}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:ProntoDespachoEC3
                markup: True
                text: "¿Presenta Pronto Despacho?"
                pos_hint: {"center_x": 1.05, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputProntoDespachoEC3
                pos_hint: {"center_x": .73, "center_y": .60}
                size_hint: None, None
                width: 350
                helper_text:"Si o No"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaDictamenEC3
                markup: True
                text: "Fecha de Dictamen"
                pos_hint: {"center_x": 1.05, "center_y": .50}
                font_size: 16

            MDTextField:
                id: InputFechaDictamenEC3
                pos_hint: {"center_x": .73, "center_y": .45}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:FechaConciliacionEC3
                markup: True
                text: "Fecha de Conciliacion"
                pos_hint: {"center_x": 1.05, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputFechaConciliacionEC3
                pos_hint: {"center_x": .73, "center_y": .30}
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
                on_release:
                    app.GuardarE3()
                    app.change_screen("MenuCaso")


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

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}



            MDLabel:
                id:TituloMCC1
                markup: True
                text: "[color=#315582][b]Etapa 4[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .80}
                font_size: 30

            MDLabel:
                id:EtapaInicioEC4
                markup: True
                text: "Etapa Inicial"
                pos_hint: {"center_x": .70, "center_y": .625}
                font_size: 16

            MDCheckbox:
                id: CheckEtapaInicialEC4
                pos_hint: {"center_x": .35, "center_y": .625}
                size_hint: None, None
                height: 50
                width: 50
                on_active: app.check2(*args)


            MDLabel:
                id:FechaEtapaInicioEC4
                markup: True
                text: "Fecha de inicio de la etapa inicial"
                pos_hint: {"center_x": 1.05, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputFechaEtapaInicioEC4
                pos_hint: {"center_x": .73, "center_y": .60}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:EtapaIntermediaEC4
                markup: True
                text: "Etapa Intermedia"
                pos_hint: {"center_x": .70, "center_y": .425}
                font_size: 16

            MDCheckbox:
                id: CheckEtapaIntermediaEC4
                pos_hint: {"center_x": .35, "center_y": .425}
                size_hint: None, None
                height: 50
                width: 50
                on_active: app.check3(*args)


            MDLabel:
                id:FechaEtapaIntermediaEC4
                markup: True
                text: "Fecha de inicio de la etapa intermedia"
                pos_hint: {"center_x": 1.05, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputFechaEtapaIntermediaEC4
                pos_hint: {"center_x": .73, "center_y": .40}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDLabel:
                id:EtapaFinalEC4
                markup: True
                text: "Etapa Final"
                pos_hint: {"center_x": .70, "center_y": .225}
                font_size: 16

            MDCheckbox:
                id: CheckEtapaFinalEC4
                pos_hint: {"center_x": .35, "center_y": .225}
                size_hint: None, None
                height: 50
                width: 50
                on_active: app.check4(*args)

            MDLabel:
                id:FechaEtapaFinalEC4
                markup: True
                text: "Fecha de inicio de la etapa Final"
                pos_hint: {"center_x": 1.05, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputFechaEtapaFinalEC4
                pos_hint: {"center_x": .73, "center_y": .20}
                size_hint: None, None
                width: 350
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"

            MDRoundFlatButton:
                id: botonGuardarDatosEC4
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.07}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release:
                    app.GuardarE4()
                    app.change_screen("MenuCaso")


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
                on_release:
                    app.change_screen("MenuCaso")

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}


            MDLabel:
                id:TituloCC1
                markup: True
                text: "[color=#315582][b]Editar Caso[/b][/color]"
                pos_hint: {"center_x": .96, "center_y": .75}
                font_size: 30

            MDLabel:
                id:TipoCC1
                markup: True
                text: "Tipo"
                pos_hint: {"center_x": .87, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputTipoEC1
                pos_hint: {"center_x": .5, "center_y": .60}
                size_hint: None, None
                width: 350

            MDLabel:
                id:FechaInicioCC1
                markup: True
                text: "Fecha de Inicio"
                pos_hint: {"center_x": .87, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputFechaInicioCC1
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: None, None
                helper_text:"Año-Mes-Día"
                helper_text_mode: "persistent"
                width: 350


            MDLabel:
                id:MotivoCC1
                markup: True
                text: "Motivo"
                pos_hint: {"center_x": .87, "center_y": .40}
                font_size: 16

            MDTextField:
                id: InputMotivoCC1
                pos_hint: {"center_x": .5, "center_y": .35}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosCC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.25}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release:
                    app.editarcaso()
                    app.change_screen("MenuCaso")

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
                on_release:
                    app.change_screen("menucliente")

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}

            MDLabel:
                id:TituloEC1
                markup: True
                text: "[color=#315582][b]Editar Cliente[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .75}
                font_size: 30

            MDLabel:
                id:NombreEC1
                markup: True
                text: "Nombre y Apellido"
                pos_hint: {"center_x": .82, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputNombreEC1
                pos_hint: {"center_x": .5, "center_y": .60}
                size_hint: None, None
                width: 350




            MDLabel:
                id:DNIEC1
                markup: True
                text: "DNI"
                pos_hint: {"center_x": .82, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputDNIEC1
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: None, None
                width: 350

            MDLabel:
                id:DireccionEC1
                markup: True
                text: "Direccion"
                pos_hint: {"center_x": .82, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputDireccionEC1
                pos_hint: {"center_x": .5, "center_y": .40}
                size_hint: None, None
                width: 350

            MDLabel:
                id:TelefonoEC1
                markup: True
                text: "Telefono"
                pos_hint: {"center_x": .82, "center_y": .35}
                font_size: 16

            MDTextField:
                id: InputTelefonoEC1
                pos_hint: {"center_x": .5, "center_y": .30}
                size_hint: None, None
                width: 350

            MDLabel:
                id:EmailEC1
                markup: True
                text: "Email"
                pos_hint: {"center_x": .82, "center_y": .25}
                font_size: 16

            MDTextField:
                id: InputEmailEC1
                pos_hint: {"center_x": .5, "center_y": .20}
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
                on_release:
                    app.editarcliente()
                    app.change_screen("menucliente")

<RegistroUsuario>
    name:"registro"
    MDBoxLayout:
		size: 1, 1
		orientation: "vertical"
		md_bg_color: 0.85, 0.8, 0.72, 1
		FloatLayout:
			id: RegistroClayout
			padding: 5

            MDIconButton:
                id: botonVolver
                icon: "arrow-left-bold"
                size_hint: None, None
                pos_hint: {"center_x": 0.05, "center_y": 0.95}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release: app.change_screen("Pantalla Principal Admin")

            Image:
                source: "logo.jpeg"
                size_hint : None, None
                pos_hint: {"center_x": 0.5, "center_y": 0.93}



            MDLabel:
                id:TituloR
                markup: True
                text: "[color=#315582][b]Registro de Usuario[/b][/color]"
                pos_hint: {"center_x": .90, "center_y": .75}
                font_size: 30

            MDLabel:
                id:NombreA
                markup: True
                text: "Nombre de Usuario"
                pos_hint: {"center_x": .87, "center_y": .65}
                font_size: 16

            MDTextField:
                id: InputNombreA
                pos_hint: {"center_x": .5, "center_y": .60}
                size_hint: None, None
                width: 350


            MDLabel:
                id:DNIA
                markup: True
                text: "DNI"
                pos_hint: {"center_x": .87, "center_y": .55}
                font_size: 16

            MDTextField:
                id: InputDNIA
                pos_hint: {"center_x": .5, "center_y": .50}
                size_hint: None, None
                width: 350


            MDLabel:
                id:contraseñaA
                markup: True
                text: "Contraseña"
                pos_hint: {"center_x": .87, "center_y": .45}
                font_size: 16

            MDTextField:
                id: InputContrasenaA
                pos_hint: {"center_x": .5, "center_y": .40}
                size_hint: None, None
                width: 350

            MDRoundFlatButton:
                id: botonGuardarDatosEC1
                markup: True
                text: "[color=#315582][b]Guardar Datos[/b][/color]"
                size_hint: None, None
                width: 100
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                md_bg_color: 0.93, 0.69, 0.63, 0.2
                on_release:
                    app.nuevouser()
                    app.change_screen("Pantalla Principal Admin")

WindowManager:
    LoginWindow:
        id:login
    pantallaPrincipal:
        id: pp

    pantallaPrincipalAdmin:
        id: ppA

    calendario:
        id: calendario

    etapas:
        id: data_scr2

    RegistroUsuario:
        id: registroU

    Etapa2:
        id: etapa2
    Etapa3:
        id: etapa3
    Etapa4:
        id: etapa4
    Caso:
        id: Caso

    VerCaso:
        id: VerCaso

    MenuCaso:
        id: menucaso
    NuevoCaso:
        id: nuevocaso

    DatosCasos:
        id: data_scr1

    menucliente:
        id: menucliente
    NuevoCliente:
        id: nuevocliente
    EditarClientes:
        id: editarcliente
    ClientWindow:
        id: data_scr

"""


class LoginWindow(Screen):
    pass

class RegistroUsuario(Screen):
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

class VerCaso(Screen):
    pass

class MenuCaso(Screen):
    pass

class NuevoCaso(Screen):
    pass

class pantallaPrincipal(Screen):
    pass

class pantallaPrincipalAdmin(Screen):
    pass

class etapas(Screen):
    pass

class Etapa2(Screen):
    pass

class Etapa3(Screen):
    pass

class Etapa4(Screen):
    pass

class EditarClientes(Screen):
    pass

class calendario(Screen):
    pass


class WindowManager(ScreenManager):
    pass




HOST = "localhost"

DATABASE = "SIC"

USER = "root"

PASSWORD = "Contraseña"

mydb = mysql.connect(host= HOST, database= DATABASE, user= USER, password= PASSWORD)

c = mydb.cursor()



def cursor (self, accion):
    c.execute(accion)
    for x in c:
        print (x)

class SIC(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tableC = None
        self.data_tables1= None
        self.data_tablesE1 = None
        self.data_tables2 = None
        self.data_tables3 = None
        self.data_tables4 = None
        self.listaEtapas = None
        self.menu = None
        self.menu1 = None
        self.menu2 = None
        self.menu3 = None
        self.menu4 = None
        self.menu5 = None
        self.DNIA = None
        self.idcliente = None
        self.idcaso= None
        self.activoE2= None
        self.activoEI4= None
        self.activoEInE4= None
        self.activoEF4= None
        self.dialogcliente= None
        self.dialogcaso= None


    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


    def abrirPJN (instance):
        webbrowser.open('https://www.pjn.gov.ar/')

    def abrirMEV (instance):
        webbrowser.open('https://mev.scba.gov.ar/loguin.asp')


    def build(self):
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def dropdown_pp(self):
        self.menuusuario = [
            {
                "viewclass" : "OneLineListItem",
                "text" : "Cerrar Sesión",
                "on_release" : lambda x= "Cerrar Sesion": self.login_pp()
            },
        ]
        self.menu1 = MDDropdownMenu(
            caller = self.root.ids.ppA.ids.botonUsuario_ppA and self.root.ids.pp.ids.botonUsuario_pp,
            items= self.menuusuario,
            width_mult= 3,
        )
        self.menu1.open()



    def dropdown (self):
        self.listaEtapas = [
            {
                "viewclass" : "TwoLineListItem",
                "text" : "Etapa 1",
                "on_release" : lambda x= "Etapa 1": self.add_datatableE1()

            },
            {
                "viewclass" : "OneLineListItem",
                "text" : "Etapa 2",
                "on_release" : lambda x= "Etapa 2": self.add_datatableE2()

            },
            {
                "viewclass" : "TwoLineListItem",
                "text" : "Etapa 3",
                "on_release" : lambda x="Etapa 3": self.add_datatable3()
            },
            {
                "viewclass" : "OneLineListItem",
                "text" : "Etapa 4",
                "on_release" : lambda x= "Etapa 4": self.add_datatable4()

            },

        ]

        self.menu = MDDropdownMenu(
            caller = self.root.ids.data_scr2.ids.botonLlamarEtapas,
            items = self.listaEtapas,
            width_mult = 4,
        )
        self.menu.open()



    def login_pp(self):
        self.change_screen("main")

    def change_screen(self, screen: str):
        self.root.current = screen

    def guardar_R1(self):
        c.execute("INSERT INTO Reunion (Fecha, Hora) VALUES ('"+str(self.root.ids.calendario.ids.InputFechaR1.text)+"', '"+str(self.root.ids.calendario.ids.InputHoraR1.text)+"');")
        mydb.commit()
        c.execute("SELECT IDReunion FROM Reunion WHERE Fecha= '"+str(self.root.ids.calendario.ids.InputFechaR1.text)+"' AND '"+str(self.root.ids.calendario.ids.InputHoraR1.text)+"';")
        tup= c.fetchone()
        lis= list(tup)
        id= lis.pop(0)
        c.execute("UPDATE Abogado SET IDReunion="+str(id)+" WHERE DNI="+str(self.DNIA)+";")
        mydb.commit()

    def guardar_R2(self):
        c.execute("INSERT INTO Reunion (Fecha, Hora) VALUES ('"+str(self.root.ids.calendario.ids.InputFechaR2.text)+"', '"+str(self.root.ids.calendario.ids.InputHoraR2.text)+"');")
        mydb.commit()
        c.execute("SELECT IDReunion FROM Reunion WHERE Fecha= '"+str(self.root.ids.calendario.ids.InputFechaR2.text)+"' AND '"+str(self.root.ids.calendario.ids.InputHoraR2.text)+"';")
        tup= c.fetchone()
        lis= list(tup)
        id= lis.pop(0)
        c.execute("UPDATE Abogado SET IDReunion2="+str(id)+" WHERE DNI="+str(self.DNIA)+";")
        mydb.commit()

    def guardar_R3(self):
        c.execute("INSERT INTO Reunion (Fecha, Hora) VALUES ('"+str(self.root.ids.calendario.ids.InputFechaR3.text)+"', '"+str(self.root.ids.calendario.ids.InputHoraR3.text)+"');")
        mydb.commit()
        c.execute("SELECT IDReunion FROM Reunion WHERE Fecha= '"+str(self.root.ids.calendario.ids.InputFechaR3.text)+"' AND '"+str(self.root.ids.calendario.ids.InputHoraR3.text)+"';")
        tup= c.fetchone()
        lis= list(tup)
        id= lis.pop(0)
        c.execute("UPDATE Abogado SET IDReunion3="+str(id)+" WHERE DNI="+str(self.DNIA)+";")
        mydb.commit()

    def guardar_R4(self):
        c.execute("INSERT INTO Reunion (Fecha, Hora) VALUES ('"+str(self.root.ids.calendario.ids.InputFechaR4.text)+"', '"+str(self.root.ids.calendario.ids.InputHoraR4.text)+"');")
        mydb.commit()
        c.execute("SELECT IDReunion FROM Reunion WHERE Fecha= '"+str(self.root.ids.calendario.ids.InputFechaR4.text)+"' AND '"+str(self.root.ids.calendario.ids.InputHoraR4.text)+"';")
        tup= c.fetchone()
        lis= list(tup)
        id= lis.pop(0)
        c.execute("UPDATE Abogado SET IDReunion4="+str(id)+" WHERE DNI="+str(self.DNIA)+";")
        mydb.commit()

    def guardar_R5(self):
        c.execute("INSERT INTO Reunion (Fecha, Hora) VALUES ('"+str(self.root.ids.calendario.ids.InputFechaR5.text)+"', '"+str(self.root.ids.calendario.ids.InputHoraR5.text)+"');")
        mydb.commit()
        c.execute("SELECT IDReunion FROM Reunion WHERE Fecha= '"+str(self.root.ids.calendario.ids.InputFechaR5.text)+"' AND '"+str(self.root.ids.calendario.ids.InputHoraR5.text)+"';")
        tup= c.fetchone()
        lis= list(tup)
        id= lis.pop(0)
        c.execute("UPDATE Abogado SET IDReunion5="+str(id)+" WHERE DNI="+str(self.DNIA)+";")
        mydb.commit()


    def borrar_R1(self):
        c.execute("SELECT IDReunion FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("UPDATE Abogado SET IDReunion= NULL WHERE DNI="+str(self.DNIA)+";")
            mydb.commit()
            c.execute("DELETE FROM Reunion WHERE IDReunion = "+str(idr)+";")
            mydb.commit()
            self.root.ids.calendario.ids.fecha_R1.text = "-"
            self.root.ids.calendario.ids.hora_R1.text = "-"

    def borrar_R2(self):
        c.execute("SELECT IDReunion2 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("UPDATE Abogado SET IDReunion2= NULL WHERE DNI="+str(self.DNIA)+";")
            mydb.commit()
            c.execute("DELETE FROM Reunion WHERE IDReunion = "+str(idr)+";")
            mydb.commit()
            self.root.ids.calendario.ids.fecha_R2.text = "-"
            self.root.ids.calendario.ids.hora_R2.text = "-"

    def borrar_R3(self):
        c.execute("SELECT IDReunion3 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("UPDATE Abogado SET IDReunion3= NULL WHERE DNI="+str(self.DNIA)+";")
            mydb.commit()
            c.execute("DELETE FROM Reunion WHERE IDReunion = "+str(idr)+";")
            mydb.commit()
            self.root.ids.calendario.ids.fecha_R3.text = "-"
            self.root.ids.calendario.ids.hora_R3.text = "-"

    def borrar_R4(self):
        c.execute("SELECT IDReunion4 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("UPDATE Abogado SET IDReunion4= NULL WHERE DNI="+str(self.DNIA)+";")
            mydb.commit()
            c.execute("DELETE FROM Reunion WHERE IDReunion = "+str(idr)+";")
            mydb.commit()
            self.root.ids.calendario.ids.fecha_R4.text = "-"
            self.root.ids.calendario.ids.hora_R4.text = "-"

    def borrar_R5(self):
        c.execute("SELECT IDReunion5 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("UPDATE Abogado SET IDReunion5= NULL WHERE DNI="+str(self.DNIA)+";")
            mydb.commit()
            c.execute("DELETE FROM Reunion WHERE IDReunion = "+str(idr)+";")
            mydb.commit()
            self.root.ids.calendario.ids.fecha_R5.text = "-"
            self.root.ids.calendario.ids.hora_R5.text = "-"

    def borrar_r(self):
        self.borrar_R1()
        self.borrar_R2()
        self.borrar_R3()
        self.borrar_R4()
        self.borrar_R5()

    def mostrarR1(self):
        c.execute("SELECT IDReunion FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("SELECT Fecha, HORA FROM Reunion WHERE IDReunion="+str(idr)+"")
            tup= c.fetchone()
            lis= list(tup)
            fecha= lis.pop(0)
            hora= lis.pop(0)
            res= bool(fecha)
            if res:
                self.root.ids.calendario.ids.fecha_R1.text= str(fecha)
            else:
                self.root.ids.calendario.ids.fecha_R1.text= "-"

            res1= bool(hora)
            if res:
                self.root.ids.calendario.ids.hora_R1.text= str(hora)
            else:
                self.root.ids.calendario.ids.hora_R1.text= "-"

    def mostrarR2(self):
        c.execute("SELECT IDReunion2 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("SELECT Fecha, HORA FROM Reunion WHERE IDReunion="+str(idr)+"")
            tup= c.fetchone()
            lis= list(tup)
            fecha= lis.pop(0)
            hora= lis.pop(0)
            res= bool(fecha)
            if res:
                self.root.ids.calendario.ids.fecha_R2.text= str(fecha)
            else:
                self.root.ids.calendario.ids.fecha_R2.text= "-"

            res1= bool(hora)
            if res:
                self.root.ids.calendario.ids.hora_R2.text= str(hora)
            else:
                self.root.ids.calendario.ids.hora_R2.text= "-"

    def mostrarR3(self):
        c.execute("SELECT IDReunion3 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("SELECT Fecha, HORA FROM Reunion WHERE IDReunion="+str(idr)+"")
            tup= c.fetchone()
            lis= list(tup)
            fecha= lis.pop(0)
            hora= lis.pop(0)
            res= bool(fecha)
            if res:
                self.root.ids.calendario.ids.fecha_R3.text= str(fecha)
            else:
                self.root.ids.calendario.ids.fecha_R3.text= "-"

            res1= bool(hora)
            if res:
                self.root.ids.calendario.ids.hora_R3.text= str(hora)
            else:
                self.root.ids.calendario.ids.hora_R3.text= "-"


    def mostrarR4(self):
        c.execute("SELECT IDReunion4 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("SELECT Fecha, HORA FROM Reunion WHERE IDReunion="+str(idr)+"")
            tup= c.fetchone()
            lis= list(tup)
            fecha= lis.pop(0)
            hora= lis.pop(0)
            res= bool(fecha)
            if res:
                self.root.ids.calendario.ids.fecha_R4.text= str(fecha)
            else:
                self.root.ids.calendario.ids.fecha_R4.text= "-"

            res1= bool(hora)
            if res:
                self.root.ids.calendario.ids.hora_R4.text= str(hora)
            else:
                self.root.ids.calendario.ids.hora_R4.text= "-"

    def mostrarR5(self):
        c.execute("SELECT IDReunion5 FROM Abogado WHERE DNI="+str(self.DNIA)+";")
        tup= c.fetchone()
        lis= list(tup)
        idr= lis.pop(0)
        res2= bool(idr)
        if res2:
            c.execute("SELECT Fecha, HORA FROM Reunion WHERE IDReunion="+str(idr)+"")
            tup= c.fetchone()
            lis= list(tup)
            fecha= lis.pop(0)
            hora= lis.pop(0)
            res= bool(fecha)
            if res:
                self.root.ids.calendario.ids.fecha_R5.text= str(fecha)
            else:
                self.root.ids.calendario.ids.fecha_R5.text= "-"

            res1= bool(hora)
            if res:
                self.root.ids.calendario.ids.hora_R5.text= str(hora)
            else:
                self.root.ids.calendario.ids.hora_R5.text= "-"


    def mostrarReuniones (self):
        self.mostrarR1()
        self.mostrarR2()
        self.mostrarR3()
        self.mostrarR4()
        self.mostrarR5()

    def login (self):
        nombre= str(self.root.ids.login.ids.nombre.text)
        psw= str(self.root.ids.login.ids.psw.text)
        res = bool(nombre)
        res2= bool(psw)
        if res and res2:
            query= "SELECT count(*) FROM Abogado where Nombre='"+str(self.root.ids.login.ids.nombre.text)+"'AND Psw='" +str(self.root.ids.login.ids.psw.text) + "'"
            query2= "SELECT * FROM Abogado where Nombre='"+str(self.root.ids.login.ids.nombre.text)+"'AND Psw='" +str(self.root.ids.login.ids.psw.text) + "'"
            c.execute(query)
            data= c.fetchone()
            count = data[0]

            if count == 0:
                r= 0
            else:
                r = 1
                c.execute(query2)
                tupla= c.fetchone()
                lista= list(tupla)
                dni= lista.pop(0)
                self.DNIA = dni
                self.change_screen("Pantalla Principal")

            if r == 1 and dni== 0000000:
                self.change_screen("Pantalla Principal Admin")


    def nuevouser (self):
        c.execute("INSERT INTO Abogado (DNI, Nombre, Psw) VALUES ('"+str(self.root.ids.registroU.ids.InputDNIA.text)+"', '"+ str(self.root.ids.registroU.ids.InputNombreA.text)+"', '"+str(self.root.ids.registroU.ids.InputContrasenaA.text)+"');")
        mydb.commit()


    def nuevocliente (self):
        c.execute("INSERT INTO Cliente (NombreC, DNIC, Direccion, Telefono, Mail, DNIA) VALUES ('"+ str(self.root.ids.nuevocliente.ids.InputNombreNC1.text)+"', '"+str(self.root.ids.nuevocliente.ids.InputDNINC1.text) +"', '"+ str(self.root.ids.nuevocliente.ids.InputDireccionNC1.text)+"', '"+str(self.root.ids.nuevocliente.ids.InputTelefonoNC1.text)+"', '"+str(self.root.ids.nuevocliente.ids.InputEmailNC1.text)+"', "+str(self.DNIA)+");")
        mydb.commit()

    def editarcliente(self):
        Nombre= str(self.root.ids.editarcliente.ids.InputNombreEC1.text)
        DNI= str(self.root.ids.editarcliente.ids.InputDNIEC1.text)
        Direccion= str(self.root.ids.editarcliente.ids.InputDireccionEC1.text)
        Telefono= str(self.root.ids.editarcliente.ids.InputTelefonoEC1.text)
        Mail= str(self.root.ids.editarcliente.ids.InputEmailEC1.text)
        res= bool(Nombre)
        if res:
            c.execute("UPDATE Cliente SET NombreC =  '"+ str(self.root.ids.editarcliente.ids.InputNombreEC1.text) + "' WHERE IDCliente= "+ str(self.idcliente))
            mydb.commit()
        res1= bool(DNI)
        if res1:
            c.execute("UPDATE Cliente SET DNIC= '"+ str(self.root.ids.editarcliente.ids.InputDNIEC1.text)+ "' WHERE IDCliente= "+ str(self.idcliente))
            mydb.commit()
        res2= bool(Direccion)
        if res2:
            c.execute("UPDATE Cliente SET Direccion= '"+ str(self.root.ids.editarcliente.ids.InputDireccionEC1.text)+"' WHERE IDCliente= "+ str(self.idcliente))
            mydb.commit()
        res3= bool(Telefono)
        if res3:
            c.execute("UPDATE Cliente SET Telefono= '"+ str(self.root.ids.editarcliente.ids.InputTelefonoEC1.text)+"' WHERE IDCliente= "+ str(self.idcliente))
            mydb.commit()
        res4= bool(Mail)
        if res4:
            c.execute("UPDATE Cliente SET Mail= '"+str(self.root.ids.editarcliente.ids.InputEmailEC1.text)+ "' WHERE IDCliente= "+ str(self.idcliente))
            mydb.commit()
    

    def nuevocaso(self):
        c.execute("INSERT INTO Caso (Tipo, FechaInicio, Motivo, IDCliente) VALUES ('"+ str(self.root.ids.nuevocaso.ids.InputTipoCC1.text)+"', '"+str(self.root.ids.nuevocaso.ids.InputFechaInicioCC1.text)+"', '"+ str(self.root.ids.nuevocaso.ids.InputMotivoCC1.text)+"', "+ str(self.idcliente)+");")
        mydb.commit()
        c.execute("SELECT * FROM Caso WHERE Tipo='"+str(self.root.ids.nuevocaso.ids.InputTipoCC1.text)+"' AND FechaInicio='"+ str(self.root.ids.nuevocaso.ids.InputFechaInicioCC1.text)+"' AND Motivo='"+str(self.root.ids.nuevocaso.ids.InputMotivoCC1.text)+"';")
        data=c.fetchone()
        lista=list(data)
        idcaso= lista.pop(0)
        self.idcaso=idcaso
        c.execute("INSERT INTO Etapas (IDCaso) VALUES ("+str(self.idcaso)+");")
        mydb.commit()

    def menucaso(self):
        res = bool(self.idcaso)
        if res:
            self.change_screen("MenuCaso")

    def Menucliente(self):
        res = bool(self.idcliente)
        if res:
            self.change_screen("menucliente")

    def editarcaso(self):
        Tipo= str(self.root.ids.Caso.ids.InputTipoEC1.text)
        res= bool(Tipo)
        if res:
            c.execute("UPDATE Caso SET Tipo='"+ str(self.root.ids.Caso.ids.InputTipoEC1.text)+"' WHERE IDCaso="+ self.idcaso)
            mydb.commit()

        FechaInicio= str(self.root.ids.Caso.ids.InputFechaInicioCC1.text)
        res1= bool(FechaInicio)
        if res1:
            c.execute("UPDATE Caso SET FechaInicio= '"+str(self.root.ids.Caso.ids.InputFechaInicioCC1.text)+"' WHERE IDCaso="+ self.idcaso)
            mydb.commit()

        Motivo= str(self.root.ids.Caso.ids.InputMotivoCC1.text)
        res2= bool(Motivo)
        if res2:
            c.execute("UPDATE Caso SET Motivo='"+ str(self.root.ids.Caso.ids.InputMotivoCC1.text)+"' WHERE IDCaso="+ self.idcaso)
            mydb.commit()



    def fechafin(self):
        x= datetime.datetime.now()
        anio= x.strftime("%Y")
        mes= x.strftime("%m")
        dia= x.strftime("%d")

        fecha= "'"+anio + "-" + mes + "-" + dia+"'"
        print(fecha)
        c.execute("UPDATE Caso SET FechaFin= "+ fecha +" WHERE IDCaso="+ self.idcaso+";")

    def check(self, checkbox, value):
        if value:
            self.activoE2= True
        else:
            self.activoE2= False
        print(self.activoE2)

    def GuardarE2(self):
        if self.activoE2 == True:
            c.execute("UPDATE Etapas SET Firma= 'Si', FechaFirma='"+str(self.root.ids.etapa2.ids.InputFechaFirmaEC2.text)+ "', LugarFirma= '"+str(self.root.ids.etapa2.ids.InputLugarFirmaEC2.text)+ "' WHERE IDCaso="+ self.idcaso+";")
            mydb.commit()
            c.execute("SELECT NEtapa FROM Caso WHERE IDCaso="+self.idcaso+";")
            data=c.fetchone()
            lista= list(data)
            NEtapa= lista.pop(0)
            if NEtapa < 2:
                c.execute("UPDATE Caso SET NEtapa= 2 WHERE IDCaso="+self.idcaso+";")
                mydb.commit()

    def GuardarE3(self):
        fechaIE3 = self.root.ids.etapa3.ids.InputFechaInicioEC3.text
        comisionM = self.root.ids.etapa3.ids.InputFechaComisionMedicaEC3.text
        fechaFE3 = self.root.ids.etapa3.ids.InputFechaFinEC3.text
        prontoD = self.root.ids.etapa3.ids.InputProntoDespachoEC3.text
        fechaD = self.root.ids.etapa3.ids.InputFechaDictamenEC3.text
        fechaC = self.root.ids.etapa3.ids.InputFechaConciliacionEC3.text
        res = bool(fechaIE3)
        if res == True:
            c.execute("UPDATE Etapas SET FechaInicioE3='"+str(fechaIE3)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()
        else:
            print("Nada")

        res1 = bool(comisionM)
        if res1 == True:
            c.execute("UPDATE Etapas SET FechaComisionMedica='"+str(comisionM)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()
        else:
            print("Nada")

        res2 = bool(fechaFE3)
        if res2 == True:
            c.execute("UPDATE Etapas SET FechaCierreE3='"+str(fechaFE3)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()
        else:
            print("Nada")

        res3 = bool(prontoD)
        if res3 == True:
            c.execute("UPDATE Etapas SET PresentaPD='"+str(prontoD)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()
        else:
            print("Nada")

        res4 = bool(fechaD)
        if res4 == True:
            c.execute("UPDATE Etapas SET FechaDictamen='"+str(fechaD)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()
        else:
            print("Nada")

        res5 = bool(fechaC)
        if res5 == True:
            c.execute("UPDATE Etapas SET FechaConciliación='"+str(fechaC)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()
        else:
            print("Nada")
        c.execute("SELECT NEtapa FROM Caso WHERE IDCaso="+self.idcaso+";")
        data=c.fetchone()
        lista= list(data)
        NEtapa= lista.pop(0)
        if NEtapa < 3:
            c.execute("UPDATE Caso SET NEtapa= 3 WHERE IDCaso="+self.idcaso+";")
            mydb.commit()


    def check2(self, checkbox, value):
        if value:
            self.activoEI4= True
        else:
            self.activoEI4= False


    def check3(self, checkbox, value):
        if value:
            self.activoEInE4= True
        else:
            self.activoEInE4= False


    def check4(self, checkbox, value):
        if value:
            self.activoEF4= True
        else:
            self.activoEF4= False

    def GuardarE4(self):
        if self.activoEI4:
            c.execute("UPDATE Etapas SET EtapaInicio= 'Si', FechaInicio='"+str(self.root.ids.etapa4.ids.InputFechaEtapaInicioEC4.text)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()

        if self.activoEInE4:
            c.execute("UPDATE Etapas SET EtapaIntermedia= 'Si', FechaIntermedia='"+str(self.root.ids.etapa4.ids.InputFechaEtapaIntermediaEC4.text)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()

        if self.activoEF4:
            c.execute("UPDATE Etapas SET EtapaFinal= 'Si', FechaFinal='"+str(self.root.ids.etapa4.ids.InputFechaEtapaFinalEC4.text)+"' WHERE IDCaso="+self.idcaso+";")
            mydb.commit()

        c.execute("SELECT NEtapa FROM Caso WHERE IDCaso="+self.idcaso+";")
        data=c.fetchone()
        lista= list(data)
        NEtapa= lista.pop(0)
        if NEtapa < 4:
            c.execute("UPDATE Caso SET NEtapa= 4 WHERE IDCaso="+self.idcaso+";")
            mydb.commit()


    def cerrardialogo(self, obj):
        self.dialogcliente.dismiss()


    def borrarcliente(self, obj):
        self.dialogcliente.dismiss()
        c.execute("DELETE FROM Caso WHERE IDCliente= "+self.idcliente+";")
        mydb.commit()
        c.execute("DELETE FROM Cliente WHERE IDCliente="+self.idcliente+";")
        mydb.commit()


    def mostraralerta(self):
        if not self.dialogcliente:
            self.dialogcliente= MDDialog(
                background_color="#D8CCB7",
                title= "¿Borrar Cliente?",
                text= "Si borra el cliente este y todos sus casos serán eliminados ",
                buttons=[
                    MDRoundFlatButton(
                        text= "Cancelar",
                        on_release= self.cerrardialogo
                    ),
                    MDRoundFlatButton(
                        text="Borrar",
                        on_release= self.borrarcliente
                    ),
                ],
            )
        self.dialogcliente.open()


    def borrarcaso(self, obj):
        self.dialogcaso.dismiss()
        c.execute("DELETE FROM Etapas WHERE IDCaso="+self.idcaso+";")
        mydb.commit()
        c.execute("DELETE FROM Caso WHERE IDCaso= "+self.idcaso+";")
        mydb.commit()




    def mostratalerta1(self):
        if not self.dialogcaso:
            self.dialogcaso= MDDialog(
                background_color="#D8CCB7",
                title= "¿Borrar Caso?",
                text= "Si borra el caso este será eliminado permanentemente",
                buttons=[
                    MDRoundFlatButton(
                        text= "Cancelar",
                        on_release= self.cerrardialogo
                    ),
                    MDRoundFlatButton(
                        text="Borrar",
                        on_release= self.borrarcaso
                    ),
                ],
            )
        self.dialogcaso.open()


    def MostrarCaso(self):
        c.execute("SELECT Tipo, FechaInicio, Motivo FROM Caso WHERE idcaso="+self.idcaso+";")
        data= c.fetchone()
        datos= list(data)
        Tipo= datos.pop(0)
        FechaI= datos.pop(0)
        Motivo= datos.pop(0)
        self.root.ids.VerCaso.ids.VerTipo.text= str(Tipo)
        self.root.ids.VerCaso.ids.VerFechaInicio.text= str(FechaI)
        self.root.ids.VerCaso.ids.VerMotivo.text= str(Motivo)
        c.execute("SELECT Firma, FechaFirma, LugarFirma, FechaInicioE3, FechaComisionMedica, FechaCierreE3, PresentaPD, FechaDictamen, FechaConciliación, EtapaInicio, FechaInicio, EtapaIntermedia, FechaIntermedia, EtapaFinal, FechaFinal FROM Etapas WHERE IDCaso="+self.idcaso+";")
        data1= c.fetchone()
        resM = bool(data1)
        if resM:
            datos1= list(data1)
            Firma= datos1.pop(0)
            FechaFirma= datos1.pop(0)
            LugarFirma= datos1.pop(0)
            FechaInicioE3= datos1.pop(0)
            FechaComisionMedica= datos1.pop(0)
            FechaCierreE3= datos1.pop(0)
            PresentaPD= datos1.pop(0)
            FechaDictamen= datos1.pop(0)
            FechaConciliación= datos1.pop(0)
            EtapaInicio= datos1.pop(0)
            FechaInicio= datos1.pop(0)
            EtapaIntermedia= datos1.pop(0)
            FechaIntermedia= datos1.pop(0)
            EtapaFinal= datos1.pop(0)
            FechaFinal= datos1.pop(0)

            res = bool(Firma)
            if res == True:
                self.root.ids.VerCaso.ids.VerFirma.text = str(Firma)
            res1 = bool(FechaFirma)
            if res1 == True:
                self.root.ids.VerCaso.ids.VerFechaFirma.text = str(FechaFirma)
            res2 = bool(LugarFirma)
            if res2 == True:
                self.root.ids.VerCaso.ids.VerLugarFirma.text = str(LugarFirma)
            res3 = bool(FechaInicioE3)
            if res3 == True:
                self.root.ids.VerCaso.ids.VerFechaInicioE3.text = str(FechaInicioE3)
            res4 = bool(FechaComisionMedica)
            if res4 == True:
                self.root.ids.VerCaso.ids.VerFechaCM.text = str(FechaComisionMedica)
            res5 = bool(FechaCierreE3)
            if res5 == True:
                self.root.ids.VerCaso.ids.VerFechaFinE3.text = str(FechaCierreE3)
            res6 = bool(PresentaPD)
            if res6 == True:
                self.root.ids.VerCaso.ids.VerPPD.text = str(PresentaPD)
            res7 = bool(FechaDictamen)
            if res7 == True:
                self.root.ids.VerCaso.ids.VerFechaD.text = str(FechaDictamen)
            res8 = bool(FechaConciliación)
            if res8 == True:
                self.root.ids.VerCaso.ids.VerFechaCon.text = str(FechaConciliación)
            res9 = bool(EtapaInicio)
            if res9 == True:
                self.root.ids.VerCaso.ids.VerEtapaIE4.text = str(EtapaInicio)
            res10 = bool(FechaInicio)
            if res10 == True:
                self.root.ids.VerCaso.ids.VerFechaEtapaIE4.text = str(FechaInicio)
            res11 = bool(EtapaIntermedia)
            if res11 == True:
                self.root.ids.VerCaso.ids.VerEtapaInterE4.text = str(EtapaIntermedia)
            res12 = bool(FechaIntermedia)
            if res12 == True:
                self.root.ids.VerCaso.ids.VerFechaEtapaInterE4.text = str(FechaIntermedia)
            res13 = bool(EtapaFinal)
            if res13 == True:
                self.root.ids.VerCaso.ids.VerEtapaFE4.text = str(EtapaFinal)
            res14 = bool(FechaFinal)
            if res14 == True:
                self.root.ids.VerCaso.ids.VerFechaEtapaFE4.text = str(FechaFinal)

    def archivarcaso(self):
        path= os.getcwd()
        c.execute("SELECT NombreC FROM Cliente WHERE IDCliente="+str(self.idcliente)+";")
        n= c.fetchone()
        n1= list(n)
        Nombre= n1.pop(0)
        c.execute("SELECT IDCaso, Tipo, Motivo, FechaInicio, FechaFin FROM Caso WHERE IDCaso="+str(self.idcaso)+"")
        res= c.fetchone()
        lis= list(res)
        id= lis.pop(0)
        tipo= lis.pop(0)
        motivo= lis.pop(0)
        fechafin= lis.pop(0)
        narchivo= str(Nombre) +" "+ str(id)+" "+ str(tipo)
        with open(r''+path+'/'+narchivo+'.txt', 'w') as fp:
            fp.write('Nombre del cliente: ')
            fp.write(''+str(Nombre)+'')
            fp.write(' ID Caso: ')
            fp.write(''+str(id)+'')
            fp.write(' Tipo: ')
            fp.write(''+str(tipo)+'')
            fp.write(' Motivo: ')
            fp.write(''+str(motivo)+'')
            c.execute("SELECT Firma, FechaFirma, LugarFirma, FechaInicioE3, FechaComisionMedica, FechaCierreE3, PresentaPD, FechaDictamen, FechaConciliación, EtapaInicio, FechaInicio, EtapaIntermedia, FechaIntermedia, EtapaFinal, FechaFinal FROM Etapas WHERE IDCaso="+str(self.idcaso)+";")
            data1= c.fetchone()
            resX= bool(data1)
            if resX:
                datos1= list(data1)
                resD= bool(datos1)
                print(resD)
                if resD:
                    Firma= datos1.pop(0)
                    FechaFirma= datos1.pop(0)
                    LugarFirma= datos1.pop(0)
                    FechaInicioE3= datos1.pop(0)
                    FechaComisionMedica= datos1.pop(0)
                    FechaCierreE3= datos1.pop(0)
                    PresentaPD= datos1.pop(0)
                    FechaDictamen= datos1.pop(0)
                    FechaConciliación= datos1.pop(0)
                    EtapaInicio= datos1.pop(0)
                    FechaInicio= datos1.pop(0)
                    EtapaIntermedia= datos1.pop(0)
                    FechaIntermedia= datos1.pop(0)
                    EtapaFinal= datos1.pop(0)
                    FechaFinal= datos1.pop(0)

                    res = bool(Firma)
                    if res == True:
                        fp.write(' Firma: ')
                        fp.write(''+str(Firma)+'')

                    res1 = bool(FechaFirma)
                    if res1 == True:
                        fp.write(' Fecha de Firma: ')
                        fp.write(''+str(FechaFirma)+'')
                    res2 = bool(LugarFirma)
                    if res2 == True:
                        fp.write(' Lugar de Firma: ')
                        fp.write(''+str(LugarFirma)+'')
                    res3 = bool(FechaInicioE3)
                    if res3 == True:
                        fp.write(' Fecha de Inicio de la Etapa 3: ')
                        fp.write(''+str(FechaInicioE3)+'')
                    res4 = bool(FechaComisionMedica)
                    if res4 == True:
                        fp.write(' Fecha de Comision Medica: ')
                        fp.write(''+str(FechaComisionMedica)+'')
                    res5 = bool(FechaCierreE3)
                    if res5 == True:
                        fp.write(' Fecha del Cierre de la Etapa 3: ')
                        fp.write(''+str(Firma)+'')
                    res6 = bool(PresentaPD)
                    if res6 == True:
                        fp.write(' ¿Presenta Pronto Despacho? ')
                        fp.write(''+str(PresentaPD)+'')
                    res7 = bool(FechaDictamen)
                    if res7 == True:
                        fp.write(' Fecha del Dictamen: ')
                        fp.write(''+str(FechaDictamen)+'')
                    res8 = bool(FechaConciliación)
                    if res8 == True:
                        fp.write(' Fecha de Conciliacion: ')
                        fp.write(''+str(FechaConciliación)+'')
                    res9 = bool(EtapaInicio)
                    if res9 == True:
                        fp.write(' Etapa Inicio: ')
                        fp.write(''+str(EtapaInicio)+'')
                    res10 = bool(FechaInicio)
                    if res10 == True:
                        fp.write(' Fecha de la Etapa Inicial: ')
                        fp.write(''+str(FechaInicio)+'')
                    res11 = bool(EtapaIntermedia)
                    if res11 == True:
                        fp.write(' Etapa Intermedia: ')
                        fp.write(''+str(EtapaIntermedia)+'')
                    res12 = bool(FechaIntermedia)
                    if res12 == True:
                        fp.write(' Fecha de la Etapa Intermedia: ')
                        fp.write(''+str(FechaIntermedia)+'')
                    res13 = bool(EtapaFinal)
                    if res13 == True:
                        fp.write(' Etapa Final: ')
                        fp.write(''+str(EtapaFinal)+'')
                    res14 = bool(FechaFinal)
                    if res14 == True:
                        fp.write(' Fecha de la Etapa Final: ')
                        fp.write(''+str(FechaFinal)+'')
                    res15 = bool(fechafin)
                    if res15:
                        fp.write(' Fecha de finalización del caso: ')
                        fp.write(''+str(fechafin)+'')






    def on_check_press(self, instance_table, current_row):
        current= current_row
        id= current.pop(0)
        print(id)
        self.idcliente = id

    def add_datatable(self):

        DATA= pd.read_sql_query("SELECT * FROM Cliente WHERE DNIA=" + str(self.DNIA), mydb)
        cols = DATA.columns.values
        values= DATA.values
        self.data_tableC = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check= True,

            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.data_tableC.bind(on_check_press=self.on_check_press)
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tableC)

    def on_check_press1(self, instance_table, current_row):
        current= current_row
        id= current.pop(0)
        print(id)
        self.idcaso = id


    def on_check_pressEtapas(self, instance_table, current_row):
        current= current_row
        id= current.pop(0)
        self.idcaso= id
        c.execute("SELECT IDCliente FROM Caso WHERE IDCaso="+str(id)+";")
        tup= c.fetchone()
        lis= list(tup)
        idc= lis.pop(0)
        self.idcliente = idc


    def add_datatable1(self):
        print (self.idcliente)
        DATA= pd.read_sql_query("SELECT IDCaso, Tipo, FechaInicio, Motivo, NEtapa FROM Caso WHERE IDCliente="+ str(self.idcliente), mydb)
        cols = DATA.columns.values
        values= DATA.values
        self.data_tables1 = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,
            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.root.ids.data_scr1.ids.data_layout1.add_widget(self.data_tables1)
        self.data_tables1.bind(on_check_press=self.on_check_press1)


    def add_datatableE1(self):
        DATA= pd.read_sql_query("SELECT IDCaso, NombreC, Tipo, Motivo, FechaInicio FROM Caso INNER JOIN Cliente ON Caso.IDCliente = Cliente.IDCliente WHERE Cliente.DNIA="+ str(self.DNIA)+ " AND NEtapa=1;", mydb)
        cols = DATA.columns.values
        values= DATA.values
        self.data_tablesE1 = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,
            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.root.ids.data_scr2.ids.data_layout2.add_widget(self.data_tablesE1)
        self.data_tablesE1.bind(on_check_press=self.on_check_pressEtapas)


    def add_datatableE2(self):
        DATA= pd.read_sql_query("SELECT IDCaso, NombreC, Tipo, Motivo, FechaInicio FROM Caso INNER JOIN Cliente ON Caso.IDCliente = Cliente.IDCliente WHERE Cliente.DNIA="+ str(self.DNIA)+ " AND NEtapa=2;", mydb)
        cols = DATA.columns.values
        values= DATA.values
        self.data_tables2 = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,
            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.root.ids.data_scr2.ids.data_layout2.add_widget(self.data_tables2)
        self.data_tables2.bind(on_check_press=self.on_check_pressEtapas)

    def add_datatable3(self):
        DATA= pd.read_sql_query("SELECT IDCaso, NombreC, Tipo, Motivo, FechaInicio FROM Caso INNER JOIN Cliente ON Caso.IDCliente = Cliente.IDCliente WHERE Cliente.DNIA="+ str(self.DNIA)+ " AND NEtapa=3;", mydb)
        cols = DATA.columns.values
        values= DATA.values
        self.data_tables3 = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,
            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.root.ids.data_scr2.ids.data_layout2.add_widget(self.data_tables3)
        self.data_tables3.bind(on_check_press=self.on_check_pressEtapas)

    def add_datatable4(self):
        DATA= pd.read_sql_query("SELECT IDCaso, NombreC, Tipo, Motivo, FechaInicio FROM Caso INNER JOIN Cliente ON Caso.IDCliente = Cliente.IDCliente WHERE Cliente.DNIA="+ str(self.DNIA)+ " AND NEtapa=4;", mydb)
        cols = DATA.columns.values
        values= DATA.values
        self.data_tables4 = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint=(0.5, 0.4),
            background_color_header="#D8CCB7",
            use_pagination=True,
            check=True,
            column_data=[
                (col, dp(30))
                for col in cols
            ],
            row_data=values
        )
        self.root.ids.data_scr2.ids.data_layout2.add_widget(self.data_tables4)
        self.data_tables4.bind(on_check_press=self.on_check_pressEtapas)



    def change_screen(self, screen: str):
        self.root.current = screen


SIC().run()
