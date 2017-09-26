'''
Created By: Roman Beya
Created On: 26-Sep-2017
Created For: ICS3U
This program calculates the total cost of a pizza based on constants and variables given a diameter value
'''

import ui

# Constants
labour_cost = 0.75
rent_shop_cost = 1.00
HST = 1.13

def calculate_on_touch_up_inside(sender):
	# get diameter input
	diameter = float(view['diameter_textfield'].text)
	# calculate total cost
	total_cost = (labour_cost + rent_shop_cost + 0.50 * diameter) * HST
	# print total_cost
	view['total_cost_label'].text = 'Your total cost is: ${:,.2F}'.format(total_cost)

view = ui.load_view()
view.present('sheet')
