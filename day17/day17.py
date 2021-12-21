
# launch a shot with velocity x_v and y_v
# returns a list of tuples containing the trajectory of the shot
def launch_shot(x_v, y_v, x_tar, y_tar):
	cur_pos_x = 0
	cur_pos_y = 0
	
	trajectory = []
	
	x_far_edge = x_target[1] if x_target[1] > 0 else x_target[0]
	y_far_edge = y_target[1] if y_target[1] > 0 else y_target[0]
	
	while cur_pos_x <= x_far_edge and cur_pos_y >= y_far_edge:
		trajectory.append((cur_pos_x, cur_pos_y))
		cur_pos_x += x_v
		cur_pos_y += y_v
		if x_v > 0:
			x_v -= 1
		elif x_v < 0:
			x_v += 1
		
		y_v -= 1

	return trajectory


# checks if any trajectory points hit the target. if one does, return the index of that point, otherwise return -1
def traj_is_in_target(traj, x_tar, y_tar):
	
	for i in range(len(traj)):
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

# calculate the minimum x value needed to hit the target
cur = 1
calculated = False
while not calculated:
	if sum([i for i in range(cur)]) >= x_target[0]:
		calculated = True
	else:
		cur += 1
#print(f'Minimum x required: {cur}')

x_vel = 21
y_vel = 125
# hahahaha brute forced it by plugging and chugging. not my finest hour

trajectory = launch_shot(x_vel, y_vel, x_target, y_target)


# verify if this trajectory was within the target
idx = traj_is_in_target(trajectory, x_target, y_target)
#print(trajectory)
if idx != -1:
	# print(trajectory[:idx + 1])
	pass
else:
	print('trajectory does not hit target')
max_y = max([i[1] for i in trajectory])

print(f'maximum height achieved: {max_y}')
# part 2

coords_that_work = []
for i in range(x_target[1] + 1):
	for j in range(0, y_target[0] - 1, -1):
		trajectory = launch_shot(i, j, x_target, y_target)
		idx = traj_is_in_target(trajectory, x_target, y_target)
		if idx != -1:
			coords_that_work.append((i,j))
		trajectory = launch_shot(i, -1 * j, x_target, y_target)
		idx = traj_is_in_target(trajectory, x_target, y_target)
		if idx != -1:
			coords_that_work.append((i, -1 * j))

print(f'total # of valid coordinates: {len(list(set(coords_that_work)))}')
