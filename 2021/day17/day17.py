
# launch a shot with velocity x_v and y_v
# returns a list of tuples containing the trajectory of the shot
def launch_shot(x_v, y_v, x_tar, y_tar):
	cur_pos_x = 0
	cur_pos_y = 0
	
	cur_traj = []
	
	x_far_edge = x_tar[1] if x_tar[1] > 0 else x_tar[0]
	y_far_edge = y_tar[1] if y_tar[1] > 0 else y_tar[0]
	
	while cur_pos_x <= x_far_edge and cur_pos_y >= y_far_edge:
		cur_traj.append((cur_pos_x, cur_pos_y))
		cur_pos_x += x_v
		cur_pos_y += y_v
		if x_v > 0:
			x_v -= 1
		elif x_v < 0:
			x_v += 1
		
		y_v -= 1

	return cur_traj


# checks if any trajectory points hit the target. if one does, return the index of that point, otherwise return -1
def traj_is_in_target(traj, x_tar, y_tar):
	
	for i in range(len(traj)):
		# noinspection PyChainedComparisons
		if (traj[i][0] >= x_tar[0] and traj[i][0] <= x_tar[1]) and (traj[i][1] >= y_tar[0] and traj[i][1] <= y_tar[1]):
			return i
	
	return -1


with open('input.txt', 'r') as f:
	lines = f.read().split('\n')[:-1]
	f.close()
lines = lines[0]
_, coords = lines.split(': ')

x_target, y_target = coords.split(', ')
x_target = [int(i) for i in x_target[2:].split('..')]
y_target = [int(i) for i in y_target[2:].split('..')]
y_target = sorted(y_target)
_target = sorted(x_target)
print(f'x coordinates: {x_target}\ny coordinates: {y_target}')

x_vel = 21
y_vel = 125
# hahahaha brute forced it by plugging and chugging. not my finest hour
# I knew it would be a near-maximum x value.
# any x velocity over 22 always overshoots the target no matter the y.
# nothing under 21 will make it to the target so I knew it had to be 21 or 22
# from there I just kept upping y by 10 until it overshot then backed off until it hit again
trajectory = launch_shot(x_vel, y_vel, x_target, y_target)


# verify if this trajectory was within the target
idx = traj_is_in_target(trajectory, x_target, y_target)

if idx == -1:
	print('trajectory does not hit target')
else:
	max_y = max([i[1] for i in trajectory])
	print(f'maximum height achieved: {max_y}')
# part 2

coords_that_work = []
for i in range(x_target[1] + 1):
	for j in range(0, y_target[0] - 1, -1):
		trajectory = launch_shot(i, j, x_target, y_target)
		idx = traj_is_in_target(trajectory, x_target, y_target)
		if idx != -1:
			coords_that_work.append((i, j))
		trajectory = launch_shot(i, -1 * j, x_target, y_target)
		idx = traj_is_in_target(trajectory, x_target, y_target)
		if idx != -1:
			coords_that_work.append((i, -1 * j))

print(f'total # of valid coordinates: {len(list(set(coords_that_work)))}')
