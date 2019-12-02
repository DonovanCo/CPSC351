#Cole Donovan (DonovanCo), pauldepalma, and jkilfoyle
#Repository: CPSC351
#Python 2.7.12

import sys

class PDA:
	curr_state = None;
	def __init__(self, q, alphabet, stack_alpha, start_state, accept_states):
		self.q = states;
		self.alphabet = alphabet;
		self.stack_alpha = stack_alpha;
		self.start_state = start_state;
		self.accept_states = accept_states;
		self.curr_state = start_state;
		return;
		
	def run_pda(self):
		try:
			inp = input("Input: ")
		except KeyboardInterrupt:
			self.decide();
		else:
			if inp == 1 or inp == 0:
				stack.append("$")
				self.curr_state = states[1];
				self.run_state_2(inp);
			else:
				print("Reject");
				sys.exit();
		return;
			
	def run_state_2(self, inp):
		if inp == 0:
			stack.append("0")
			try:
				inp = input("Input: ")
			except KeyboardInterrupt:
				self.decide();
			self.run_state_2(inp);
		elif inp == 1:
			if stack[len(stack)-1] != '0':
				self.decide();
			else:
				stack.pop(len(stack)-1)
				self.curr_state = states[2];
				self.run_state_3(inp);
		else:
			print("Reject");
			sys.exit();
		return;
		
	def run_state_3(self, inp):
		try:
			inp = input("Input: ")
		except KeyboardInterrupt:
			self.decide();
		else:
			if inp == 1:
				if stack[len(stack)-2] != '0':
					self.run_state_4();
				else:
					stack.pop(len(stack)-1)
					self.run_state_3(inp);
			elif inp == 0:
				self.decide();
			else:
				print("Reject");
				sys.exit();
		return;
		
	def run_state_4(self):
		try:
			inp = input("Input: ")
		except KeyboardInterrupt:
			self.curr_state = states[3];
			self.decide();
		if len(stack)==1 and stack[0] == "$":
			self.curr_state = states[3];
			self.decide();
		else:
			print("Reject");
		return;
	
	def decide(self):
		if self.curr_state == accept_states[0] or self.curr_state == accept_states[1]:
			print("\nAccept");
			sys.exit();
		else:
			print("\nReject");
			sys.exit();
		return;
	
	pass;
	
states = [1, 2, 3, 4];
alphabet = {0, 1};
stack_alpha = {0, "$"};
start_state = 1;
accept_states = [1, 4];
stack = [];

p = PDA(states, alphabet, stack_alpha, start_state, accept_states);

p.run_pda();