height = input('Enter the height: ').split()
height_half = int((int(height[0])-1) / 2)
width_half = int((int(height[1])-1) / 2)
welcome = 'WELCOME'
s = width_half + 2
for i in range(0, height_half):
    s = s-3
    print(('-'*s) + ('.|.'*(i+1)) + ('.|.'*i) + ('-'*s))

w = int((int(height[1]) - len(welcome)) / 2)
print('-'*w + welcome + '-'*w)
s = 3
for i in range(0, height_half):
    print(('-'*s) + ('.|.'*(height_half - i)) + ('.|.'*(height_half-1-i)) + ('-'*s))
    s = s+3
