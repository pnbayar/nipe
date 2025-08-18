old_string="daksh"
reverse_string=' ' * len(old_string)
for i in range(len(old_string)):
    reverse_string+=old_string[-(i+1)]

print(reverse_string)