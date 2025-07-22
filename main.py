import flet as ft
from datetime import date
import random

# LIFE = 24107
# LIFE: int = 2410
SIZE: int = 5
SPACE: int = 1
# BORDER_HAVE: int = 1
# BORDER_SPENT: int = 2
BORDER_HAVE: int = 0
BORDER_TODAY: int = 1
BORDER_SPENT: int = 2
COLOR1: str = "#3A3A3A"
COLOR2: str = "#D9D9D9"
FDAY: date = date(1983, 12, 13)
LDAY: date = date(2058, 12, 13)
TODAY: date = date.today()
LIFE = LDAY - FDAY
LIFE_DAYS = LIFE.days
SPENT = TODAY - FDAY
SPENT_DAYS = SPENT.days
REST = LDAY - TODAY
REST_DAYS = REST.days
print(SPENT_DAYS)
print(REST_DAYS)


def main(page: ft.Page):
	# page.add(ft.Text(value="Hello, world!"))
	page.bgcolor = COLOR1
	page.vertical_alignment=ft.MainAxisAlignment.CENTER,
	page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
	# page.window_height=1080
	# page.window_width=1920

	page.padding = 0
	
	tody = ft.Text(
		color=COLOR2,
		value=TODAY
	)
	title = ft.Text(
		color=COLOR2,
		value=f"{SPENT_DAYS}d [{int(SPENT_DAYS/7)}w] — {REST_DAYS}d [{int(REST_DAYS/7)}w]"
	)

	days: list = []
	# day0 = ft.Container(
	# 		width=SIZE,
	# 		height=SIZE,
	# 		bgcolor=COLOR2)
	# days.append(day0)
	for d in range(LIFE_DAYS):
		_border = BORDER_HAVE if d > SPENT_DAYS else BORDER_SPENT
		_border = BORDER_TODAY if d == SPENT_DAYS+1 else _border
		_day = ft.Container(
			width=SIZE,
			height=SIZE,
			bgcolor=COLOR2,
			border=ft.border.all(_border, COLOR1),
			# border_radius=ft.border_radius.all(SIZE/2)
		)
		days.append(_day)
	
	weeks: list = []
	for w in range(1, int(LIFE_DAYS/7) + 1):
		_week = ft.Row(
			controls=days[(w-1)*7:w*7],
			spacing=0,
			alignment=ft.MainAxisAlignment.CENTER,
			vertical_alignment=ft.CrossAxisAlignment.CENTER
		)
		weeks.append(_week)

	rows: list = []
	for r in range(1, int(len(weeks)/30) + 1):
		_row = ft.Row(
			controls=weeks[(r-1)*30:r*30],
			spacing=SPACE,
			alignment=ft.MainAxisAlignment.CENTER,
			vertical_alignment=ft.CrossAxisAlignment.CENTER
		)
		rows.append(_row)
	


	jar = ft.Column(
		controls=rows,
		spacing=SPACE,
		alignment=ft.MainAxisAlignment.CENTER,
		horizontal_alignment=ft.CrossAxisAlignment.CENTER,
		tight=True
	)

	jar.controls.insert(0, title)
	jar.controls.insert(0, tody)

	# for d in days:
	# 	jar.controls.append(d)
	
	# page.add(weeks[len(weeks)-1])
	
	layout = ft.Container(
		content=jar,
		height=page.height,
		width=page.width,
		# border=ft.border.all(2,"black"),	
		alignment=ft.alignment.center
	)
	
	page.add(layout)
	# page.add(jar)
	
		
ft.app(target=main, assets_dir="assets", web_renderer=ft.WebRenderer.HTML)
# ft.app(target=main, assets_dir="assets")