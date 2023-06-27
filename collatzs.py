import csv
import sys


def main():
    # ensure csv file is supplied
    if len(sys.argv) != 2 or isinstance(sys.argv[1], int):
        sys.exit("Usage: python3 collatzs.py INT")
    
    # open csv to write rows to
    with open('output.csv', 'w') as file:
        fieldnames = ['Start', 'Steps']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        
        # iterate over each value and write the number of steps into output
        for x in range (1, (int(sys.argv[1]) + 1)):
            # count the number of steps for each starting x
            steps = count_steps(x)
            #write number of steps for that x to csv file
            writer.writerow({"Start": x, "Steps": steps})



def count_steps(x):
    # create step variable to keep track of the number of steps
    steps = 0

    # follow the rules of Collatzs conjecture
    while x > 1:
        if x % 2 == 0:
            x = x /2
        else:
            x =  (x * 3) + 1
        steps = steps + 1
    return steps


if __name__ == "__main__":
    main()