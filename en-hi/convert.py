import sys

count = 1
UNK = '_'
for line in sys.stdin:
	if not line.strip():
		count = 1
		sys.stdout.write("\n")
		continue

	word, lang, tag = line.rstrip("\n").split("\t")
	sys.stdout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(count, word, word, UNK, tag, UNK, UNK, UNK, UNK, 'Lang=' + lang.upper() + '|Orig=' + word))
	count += 1
