import fileinput, string, sys, re

for line in fileinput.FileInput(sys.argv[1], inplace=1):
    line = re.sub('[.,)(?"“”:;!]', r'', line, flags = re.M)
    line = re.sub("’s ", r' ', line, flags = re.M)
    line = re.sub("'s ", r' ', line, flags = re.M)
    line = re.sub("' s ", r' ', line, flags = re.M)
    line = re.sub(" – ", r' ', line, flags = re.M)
    line = re.sub("– ", r'', line, flags = re.M)
    line = re.sub("- ", r'', line, flags = re.M)
    line = re.sub(" -", r'', line, flags = re.M)
    line = re.sub("['’]", r'', line, flags = re.M)
    line = re.sub("[a-z-0-9]*/[a-z-0-9]*", r'', line, flags = re.M)
    line = re.sub("[A-Z]*[0-9]", r'', line, flags = re.M)
    line = re.sub("[0-9]", r'', line, flags = re.M)
    line = re.sub("  [ ]*", r' ', line, flags = re.M)
    sys.stdout.write(line)