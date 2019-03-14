import sys
import count_area_API as count

if __name__ == "__main__":
    filename = sys.argv[1]
    shape = sys.argv[2].split(',')
    print("start processing...")
    count.count_area(filename, int(shape[0]), int(shape[1]))


