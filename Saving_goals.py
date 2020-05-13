import streamlit as st
import pickle
import numpy as np
import random
import time
import os

@st.cache(allow_output_mutation =True)
class Data:
	def __init__(self):
		self.name = ""
		self.goal = 0
		self.curr_amnt = 0


		
data = Data()

data_file = f"{data.name}%{data.goal}/{data.curr_amnt}"

quoteList = [
	"One of the best things you can do for your money management is to make a budget (and stick to it!)",
	"Keep a close eye on your overall financial situation",
	"Are you paying too much for something that is worth lesser?",
	"Start saving today!",
	"Track your spendings",
	"Save up for rainy days!",
]

def main():
	title = st.empty()
	

	# checkFile()
	sidebar = st.sidebar.radio(label="Sections", options=["Intro", "Goal Setting", "Track Savings", "Daily"])
	if sidebar == "Intro":
		get_name = st.text_input("1.1 Please input your name.")
		if st.button("Done!"):
			data.name = get_name
			st.success(f"Welcome {get_name}.")

	if sidebar == "Goal Setting":
		title.title("Goal Settings")
		curr_goal = st.subheader(f"Your current goal is to save up to ${data.goal}.")
		goal_amnt = st.number_input("How much would you like to save?")
		data.goal = goal_amnt
		if st.button("Done!"):
			st.success("Your Goal is Successfully updated!")

	if sidebar == "Track Savings":
		title.title(f"{data.name} Savings")
		curr_goal = st.subheader(f"Goal:\t${data.goal}")
		curr_saving = st.subheader(f"Current saved amount:\t${data.curr_amnt}.")
		if data.goal == 0:
			myProgress = st.progress(0)
		else:
			progress = int((data.curr_amnt / data.goal) * 100)
			myProgress = st.progress(progress)
		randomQuote = random.choice(quoteList)
		tips = st.info(f"Random tip:\n'{randomQuote}'")

	if sidebar == "Daily":

		title.title("How much did I save today?")
		amnt = st.number_input("How much did you save?")
		if st.button("Finish"):
			data.curr_amnt += amnt
			if data.curr_amnt >= data.goal:
				st.success(f"Congratulations! You have saved up to ${data.goal}!")
				st.balloons()
				st.write("Head over to the Goal Settings to update your goals.")
			else:
				st.success(f"Hoorah! You have saved ${amnt} today!")


	save()

@st.cache
def checkFile():
	global data
	if os.path.exists("Savefile.txt"):
		file = open("Savefile.txt", "r")
		if file.mode == 'r':
			contents = file.read()
			#Find Saved Name
			name_pos = contents.find("%")
			data.name = contents[:name_pos]
			#Get Saved Goal
			goal_pos = contents.find("/")
			data.goal = contents[name_pos - 1:goal_pos]
			#Get Curr Savings
			data.curr_amnt = contents[goal_pos:]
	else:
		pass



def save():
	file = open("Savefile.txt", "w+")
	file.write(data_file)
	file.close()

			
main()
