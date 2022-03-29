import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0 
    while(n != 1):
      count += 1
      if(n % 2) == 0:        # n is even
         n = n // 2
      else:                 # n is odd
        n = n * 3 + 1
    return(count)
    print(n)           # the last print is 1

def graph_seq3np1(upper_bound):
  write_max= turtle.Turtle()
  write_max.up()
  x_axis=turtle
  y_axis=turtle.Turtle()
  window=turtle.Screen()
  graph= turtle.Turtle()
  graph.speed(0)
  window.setworldcoordinates(0,0,10,10)
  max_so_far = 0
  upper_limit = int(upper_bound)
  for i in range(1,upper_limit+1,1):
    result = seq3np1(i)
    x_axis.goto(i+10,0)
    if result> max_so_far:
      max_so_far= result
      y_axis.goto(0,max_so_far+11)
      write_max.clear()
      write_max.goto(0,max_so_far)
      write_max.write("Max so far: " + str(i) +"," + str(max_so_far))
      window.setworldcoordinates(0,0, upper_limit +10, max_so_far +10)
    graph.goto(i,result)
  window.exitonclick()

def main():
  upper_bound= input("enter a number:")
  int(upper_bound)
  if upper_bound > str(0):
    start=int(upper_bound)
    for i in range(1,start+1, 1):
      print("It requires "+ str(seq3np1(i))+ " iterations for " +str(i) + " to get to 1")
  elif upper_bound < str(0):
    quit()
  graph_seq3np1(upper_bound)
main()
  
    

seq3np1(3)
main()
