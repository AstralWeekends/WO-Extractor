# Extract and Format a List of Work Orders from a text file

#Input Fields:
'''
Source File:
'''
import PySimpleGUI as sg
import re
import sys

# color theme, use sg.theme_previewer() to see all theme options
sg.theme('Topanga')

ftypes = [
            ('Text Files', '*.txt')
        ]

while True:
	text = sg.popup_get_file('Source File: ', file_types = ftypes)
	if text == '':
		sg.popup("Error", "No file was selected for this operation. Please select a file next time.")
	elif text is None:
		sys.exit()()
	else:
		while True:
			text_save = sg.popup_get_file('Save New File: ', file_types = ftypes, save_as=True)
			if text is None:
				sys.exit()()
			elif text_save == '':
				sg.popup("Error", "No file was selected for this operation. Please select a file next time.")
			elif text_save is None:
				sys.exit()()
			elif text_save != '':
				if text_save.endswith(".txt") == False:
					text_save = text_save + ".txt"
				break	
		
		p = re.compile('[ ]*[\t]*[0-9]{7}(?![0-9])')
		wo_list = []

		with open(text, 'r') as file1:
			file_lines = file1.readlines()

		for i in file_lines:
			m = p.match(i)
			if m:
				wo_list.append(m.group())
			else:
				continue

		wo_string = str(wo_list)
		wo_string = wo_string.replace(' ', '')
		wo_string = wo_string.replace('\\t', '')
		wo_string = wo_string.replace('[', '(')
		wo_string = wo_string.replace(']',')')

		f = open(text_save, 'w+')
		f.write(str(wo_string))

		sg.popup('Results:', text_save)
		
		sys.exit()()