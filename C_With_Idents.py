in_file = "test.ci"
out_file = "test.c"

PREPROCESSORS = ["define", "undef", "ifdef", "endif", "error", "pragma"] # if else elif
ident = 0
ident_length = "\t"

in_file_data = """
include stdio.h
define ERROR 0

void main():
	printf("Shail ")
	puts("is implementing new version of C syntax")
	if (1):
		printf("shail")
		if hacker:
			shail()
			void shail():
				hacker()
				hacker()
	printf("shail")

void shail():
	printf("asdf")


struct shail:
	int shail
	int hacker
;
""".split("\n")


def main():
	global ident
	for line in in_file_data:
		process_line(line)


def process_line(file_line):
	out_file_data = ""
	if file_line:
		pre = check_preprocessors(file_line)
		if pre:
			write_data(pre)
			return
	indent_data = check_idents(file_line)
	write_data(indent_data)
	

def check_preprocessors(line):
	if line.startswith("include"):
		include = "#include "
		header = line.split(' ')[1]
		if '\"' in line:
			include += f"{header}"
		else:
			include += f"<{header}>"
		return include
	line = line.split(' ', 1) # split by space only one time

	if line[0] in PREPROCESSORS:
		return f"#{line[0]} {line[1]}"


def check_idents(line):
	global ident
	data = ""
	if line.endswith(":"):
		data = line[:-1]
		ident += 1
		data += " {"
	elif line.count(ident_length) < ident:
		num = ident - line.count(ident_length)
		if num == 1:
			data += "}\n"
		else:
			for i in range(ident - line.count(ident_length), 0, -1):
				data += ident_length*(i) + "}" + "\n"
		data += line
		if line and not line.endswith(";"):
			data += ";"
		ident -= ident - line.count(ident_length)
	else:
		data += line
		if line and not line.endswith(";"):
			data += ";"
	return data


def write_data(data):
	print(data)

main()
