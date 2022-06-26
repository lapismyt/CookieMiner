import kivy
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.audio import SoundLoader
clicksound = SoundLoader.load("point.ogg")
kivy.require("2.1.0")

class CookieMinerApp(App):

	def build(self):
		self.score = 0
		self.cookie_x = random.random()
		self.cookie_y = random.random()
		return Builder.load_string(KV)
	
	def on_start(self):
		self.root.current = "menu"
	
	def start_game(self):
		self.root.current = "game"
	
	def cookie_catch(self):
		self.score += 1
		self.cookie_x = random.random()
		self.cookie_y = random.random()
		while True:
			self.cookie_x = random.random()
			self.cookie_y = random.random()
			if self.cookie_x > 0.1 and self.cookie_y > 0.1:
				print(self.root.ids.cookie.pos_hint)
				break
			else:
				print(self.root.ids.cookie.pos_hint)
				continue
		self.root.ids.cookie.pos_hint = {"right": self.cookie_x, "top": self.cookie_y}
		self.root.ids.score_label.text = "Score: " + str(self.score)
		clicksound.play()

KV = """
ScreenManager:
	Screen:
		name: "menu"
		canvas.before:
			Rectangle:
				pos: self.pos
				size: self.size
				source: "bg.png"
		BoxLayout:
			orientation: "vertical"
			padding: 20
			Label:
				text: "COOKIE MINER\\nПЕЧЕНЬКА КЛИКЕР"
				font_name: "PixelFont.ttf"
				color: "#000000"
				font_size: "50sp"
				halign: "center"
				pos_hint_y: .75
			Button:
				text: "PLAY"
				font_size: "60sp"
				font_name: "PixelFont.ttf"
				valign: "top"
				halign: "center"
				size_hint_y: .1
				pos_hint_y: .3
				background_down: ""
				background_normal: ""
				background_color: rgba(0, 0, 0, 0)
				color: "#000000"
				on_release: app.start_game()
	Screen:
		id: game_screen
		name: "game"
		canvas.before:
			Rectangle:
				pos: self.pos
				size: self.size
				source: "bg.png"
		FloatLayout:
			id: game_layout
			Label:
				id: score_label
				text: "Score: " + str(app.score)
				halign: "left"
				font_size: "40sp"
				font_name: "PixelFont.ttf"
				color: "#000000"
				pos_hint: {"top": 1, "right": .3}
				size_hint: .1, .1
			Button:
				text: ""
				id: cookie
				pos_hint: {"right": app.cookie_x, "top": app.cookie_y}
				size_hint: .2, .1
				on_press: app.cookie_catch()
				background_normal: "cookie.png"
				background_down: "cookie.png"
				background_color: "#FFFFFF"
				color: rgba(0, 0, 0, 0)
"""

if __name__ == "__main__":
	CookieMinerApp().run()
