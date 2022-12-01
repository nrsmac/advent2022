import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()

    summed_calories = []
    with open(args.input, 'r') as f:
        current_sum = 0 
        for i, line in enumerate(f.readlines()):
            # remove spaces and newlines
            line = line.strip()
            if line == '':
                summed_calories.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line)

    print(f"Part 1: {max(summed_calories)}")
    print(f"Part 2: {sum(sorted(summed_calories, reverse=True)[:3])}")

if __name__ == '__main__':
    main()
