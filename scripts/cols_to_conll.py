import sys

num = 1
IDK = '_'
for line in sys.stdin:
	if line == "\n":
		print("")
		num = 1
		continue

	try:
		_, word, lang, pos = line.rstrip("\n").split("\t")
	except:
		print(line)

	print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\tLang={}".format(num, word, IDK,IDK,pos, IDK, IDK, IDK, IDK, lang))
	num += 1
