import streamlit as st
import pickle

ls = []

def main():
	start = st.slider("Set your Goal")
	if st.button("Done!"):
		goal = start
		print(goal)
		with open("savefile", "wb") as f:
			pickle.dump(goal, f)

		


main()