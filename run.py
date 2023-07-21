from thefuzz import fuzz, utils
from thefuzz import process
# from thefuzz.string_processing import StringProcessor

in1 = open("data/test_first", "r")
in2 = open("data/test_second", "r")

in1_str = in1.read()
in2_str = in2.read()

# out = open("ratio.out", "w")

ratio = fuzz.ratio(in1_str, in2_str)

# out.write(str(ratio))
print(str(ratio))
