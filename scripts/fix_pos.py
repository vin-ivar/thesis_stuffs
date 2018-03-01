import sys

with open("raw.conllu", "r") as raw, open("tr.parse.conllu") as final:
	for a, b in zip(raw, final):

		if not a.strip():
			sys.stdout.write("\n")
			continue
		
		if a[0] == '#':
			sys.stdout.write(a)
			continue

		cols = b.split("\t")
		trupos = a.split("\t")[4]
		sys.stdout.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*cols[0:3], trupos, '_', *cols[5:10]))
