#Cole Donovan, pauldepalma, and jkilfoyle
#Repository: CPSC351
#Python 2.7.12

import sys

class DFA:
	curr_state = None;
	def __init__(self, states, alphabet, transitions, start_state, accept_states):
		self.states = states;
		self.alphabet = alphabet;
		self.transitions = transitions;
		self.start_state = start_state;
		self.accept_states = accept_states;
		self.curr_state = start_state;
		return;
		
	pass;


#These are the members of the tuple that make up the DFA - Q, sigma, delta, start state, and accepting states.
states = [0, 1, 2, 3];
alphabet = ['0', '1'];

transitions = {0:{'0':3, '1':1}, 1:{'0':2, '1':2}, 2:{'0':3, '1':1}, 3:{'0':3, '1':3}};

start_state = 0;
accept_states = [1, 2];


#Gets first input before going into while loop. KeyboardInterrupt looks for the ctrl - c.
try:
	inp = str(raw_input("Input: "))
except KeyboardInterrupt:
	sys.exit();

while 1:
	# Constructs the DFA
	d = DFA(states, alphabet, transitions, start_state, accept_states);
	
	#Iterates over every character in the input.
	for ch in str(inp):
		if not ch in d.alphabet:
			#If input char is not in input, go to a reject state.
			d.curr_state = d.states[3]
		else:
			#Delta transition - Looks up the proper state to move to based on the current state and the current input cahracter.
			d.curr_state = d.transitions[d.curr_state][ch]
	#Checks if the current state is an accepting state and reaccts accordingly.
	if d.curr_state in d.accept_states:
		print("Accept");
	else:
		print("Reject");
	#Get next input.
	try:
		inp = str(raw_input("Input: "))
	except KeyboardInterrupt:
		sys.exit();
		