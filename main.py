import flet as ft
from datetime import date, timedelta
from typing import List

# Configuration Constants
DAY_SIZE: int = 6  # Size of each day square
SPACE_BETWEEN_ROWS: int = 2  # Spacing between rows of weeks
BORDER_WIDTH_FUTURE: int = 1  # Border width for future days
BORDER_WIDTH_PAST: int = 2  # Border width for past days
BACKGROUND_COLOR: str = "#3A3A3A"  # Background color of the page
DAY_COLOR: str = "#D9D9D9"  # Color for the day squares
BIRTH_DATE: date = date(1983, 12, 13)  # Starting date (birth date)
EXPECTED_LIFE_END_DATE: date = date(2049, 12, 13)  # Ending date (expected lifespan)


def calculate_life_stats(birth_date: date, end_date: date) -> tuple[int, int]:
	"""Calculates total life days and spent days."""
	today: date = date.today()
	total_life: timedelta = end_date - birth_date
	total_life_days: int = total_life.days
	days_spent: timedelta = today - birth_date
	days_spent_count: int = days_spent.days
	return total_life_days, days_spent_count


def create_day_square(day_number: int, days_spent: int) -> ft.Container:
	"""Creates a square representing a day."""
	border_width: int = (
		BORDER_WIDTH_FUTURE
		if day_number > days_spent
		else BORDER_WIDTH_PAST
	)
	return ft.Container(
		width=DAY_SIZE,
		height=DAY_SIZE,
		bgcolor=DAY_COLOR,
		border=ft.border.all(border_width, BACKGROUND_COLOR),
	)


def create_week_row(days: List[ft.Container]) -> ft.Row:
	"""Creates a row representing a week."""
	return ft.Row(
		controls=days,
		spacing=0,
		alignment=ft.MainAxisAlignment.CENTER,
		vertical_alignment=ft.CrossAxisAlignment.CENTER,
	)


def create_life_calendar(
	total_life_days: int, days_spent: int
) -> List[ft.Row]:
	"""Generates the life calendar grid."""
	days: List[ft.Container] = [
		create_day_square(d, days_spent) for d in range(total_life_days)
	]
	weeks: List[ft.Row] = [
		create_week_row(days[i : i + 7]) for i in range(0, total_life_days, 7)
	]
	return weeks


def group_weeks_into_rows(weeks: List[ft.Row], weeks_per_row: int = 30) -> List[ft.Row]:
	"""Groups weeks into rows for the calendar."""
	return [
		ft.Row(
			controls=weeks[i : i + weeks_per_row],
			spacing=SPACE_BETWEEN_ROWS,
			alignment=ft.MainAxisAlignment.CENTER,
			vertical_alignment=ft.CrossAxisAlignment.CENTER,
		)
		for i in range(0, len(weeks), weeks_per_row)
	]


def main(page: ft.Page):
	"""Main function to set up the Flet page and display the life calendar."""
	try:
		# Page Setup
		page.bgcolor = BACKGROUND_COLOR
		page.vertical_alignment = ft.MainAxisAlignment.CENTER
		page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
		page.padding = 0

		# Calculate Life Statistics
		total_life_days, days_spent = calculate_life_stats(
			BIRTH_DATE, EXPECTED_LIFE_END_DATE
		)
		days_remaining: int = total_life_days - days_spent

		# Create Title
		title: ft.Text = ft.Text(
			color=DAY_COLOR,
			value=(
				f"{days_spent}d [{days_spent // 7}w] — "
				f"{days_remaining}d [{days_remaining // 7}w]"
			),
		)

		# Generate Life Calendar
		weeks: List[ft.Row] = create_life_calendar(total_life_days, days_spent)
		rows: List[ft.Row] = group_weeks_into_rows(weeks)

		# Create the Calendar Grid
		calendar_grid: ft.Column = ft.Column(
			controls=rows,
			spacing=SPACE_BETWEEN_ROWS,
			alignment=ft.MainAxisAlignment.CENTER,
			horizontal_alignment=ft.CrossAxisAlignment.CENTER,
			tight=True,
		)
		calendar_grid.controls.insert(0, title)

		# Layout
		layout: ft.Container = ft.Container(
			content=calendar_grid,
			height=page.height,
			width=page.width,
			alignment=ft.alignment.center,
		)

		# Add to Page
		page.add(layout)

	except Exception as e:
		print(f"An error occurred: {e}")
		page.add(
			ft.Text(
				f"An error occurred: {e}", color=ft.colors.RED
			)  # Display error on page
		)


if __name__ == "__main__":
	ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)