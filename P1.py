n_inputs = int(input()) #number of samples

values = input().split() #input/inserting values in a list

values = [int(i) for i in values] #converting String elements to Int elements


for i in range(n_inputs):
    if i == 0:
       c_prev = values[i] = values[0] #saving the previos values and starting the list with the fistr element
    else:
        c_next = values[i] #saving value for the next operation, is needed because the list its been update in each iteration so is necessary to save the values
        n_diff = c_next - c_prev #calculating the difference
        c_prev = values[i] #saving the previous values
        values[i] = n_diff #updating the list
       

print(*values)

