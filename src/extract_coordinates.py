import re
from functools import reduce

origin_file_path = r"..\data\canadian_pit_data\canadian_pit_coordinates.txt"
out_file_path = r"..\data\canadian_pit_data\coordinates.txt"


def extract_coordinates(input_file, output_file):
    outf = open(output_file, "w")
    with open(input_file) as inf:
        for line in inf:
            res = line.split(sep=":")
            cor = res[-1]
            plane_cor = cor.split(sep=",")[0:-1]
            plane_cor = [item.strip(".") for item in plane_cor]
            line = reduce((lambda x, y: x+" "+y), plane_cor)
            line += "\n"
            outf.write(line)


if __name__ == "__main__":
    extract_coordinates(origin_file_path, out_file_path)
