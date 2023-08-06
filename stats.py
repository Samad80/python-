import statistics

d=[10,49,50,70,80,40,56,93,91,38,78,65,56,51,77,88]

def mean ():
    n=statistics.mean(d)
    return print (f"the mean is {n}")

def mode ():
    m = statistics.mode(d)
    return print ( f"The most common number in the list is :{m}")

def median():
    o=statistics.median(d)
    return  print (f"Median of the numbers are:{o} ")


def main():
    mean()
    mode()
    median()
    
main ()
