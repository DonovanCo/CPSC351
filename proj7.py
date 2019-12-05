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
	
states = [0, 1, 2, 3];
alphabet = ['0', '1'];

transitions = {0:{'0':3, '1':1}, 1:{'0':2, '1':2}, 2:{'0':3, '1':1}, 3:{'0':3, '1':3}};

start_state = 0;
accept_states = [1, 2];

try:
	inp = str(raw_input("Input: "))
except KeyboardInterrupt:
	sys.exit();

while 1:
	d = DFA(states, alphabet, transitions, start_state, accept_states);
	for ch in str(inp):
		if not ch in d.alphabet:
			d.curr_state = d.states[3]
		else:
			d.curr_state = d.transitions[d.curr_state][ch]
	if d.curr_state in d.accept_states:
		print("Accept");
	else:
		print("Reject");
	try:
		inp = input("Input: ")
	except KeyboardInterrupt:
		sys.exit();
		