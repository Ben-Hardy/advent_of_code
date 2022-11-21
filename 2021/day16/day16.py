from collections import deque

hexes = {
	'0': '0000',
	'1': '0001',
	'2': '0010',
	'3': '0011',
	'4': '0100',
	'5': '0101',
	'6': '0110',
	'7': '0111',
	'8': '1000',
	'9': '1001',
	'A': '1010',
	'B': '1011',
	'C': '1100',
	'D': '1101',
	'E': '1110',
	'F': '1111',
}


def hex_to_bin(hex_str):
	bin_str = deque()
	for i in hex_str:
		bin_str.append(hexes[i])
	
	return "".join(bin_str)

def bin_to_decimal(bin_str):
	bin_list = list(bin_str)[::-1]
	ctr = 0
	total = 0
	for i in bin_list:
		total += int(i) * 2**ctr
		ctr += 1
	return total


with open('small_input.txt', 'r') as f:
	lines = f.read()
	f.close()
code = lines.split("\n")[0]
bin_code = hex_to_bin(code)

version_sum = 0
while bin_code != "":
	# chop off first 3 bits
	packet_ver = bin_code[:3]
	print(packet_ver)
	bin_code = bin_code[3:]
	packet_ID_type = bin_code[:3]
	print(packet_ID_type)
	bin_code = bin_code[3:]
	packet_ver_dec = bin_to_decimal(packet_ver)
	packet_ID_dec = bin_to_decimal(packet_ID_type)
	
	if packet_ID_dec == 4:
		stored_num_bin = []
		while bin_code[0] == '1':
			chunk = bin_code[:5]
			stored_num_bin.append(chunk[1:5])
			bin_code = bin_code[5:]
		
		chunk = bin_code[:5]
		stored_num_bin.append(chunk[1:5])
		bin_code = bin_code[5:]
		print(stored_num_bin)
		
		ctr = 0
		inst_len = 6 + 5 * len(stored_num_bin)
		while ctr * 4 < inst_len:
			ctr += 1
		
		bits_to_remove = ctr * 4 - inst_len
		bin_code = bin_code[bits_to_remove:]
		stored_num_dec = bin_to_decimal("".join(stored_num_bin))
		print(stored_num_dec)
		
	else:
		length_type_ID = bin_code[0]
		bin_code = bin_code[1:]
		
		if length_type_ID == '0':
			total_length = bin_code[:15]
			bin_code = bin_code[15:]
			total_length_dec = bin_to_decimal(total_length)
			print(total_length_dec)
			
		else:
			pass
	version_sum += packet_ver_dec

print(version_sum)
