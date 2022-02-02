import os

# print()

imports = set()

dirname = os.path.dirname(__file__)

files = []
os.chdir(dirname + '/../Source/')
for file in os.listdir('.'):
  if file.endswith('.cpp') or file.endswith('.h'):
    files.append(file)

for file in files:
  os.system('clang-format -style=file -i ' + file)
  if file.endswith('.cpp'):
    contents = open(file, 'r').read()
    linei = 0
    lines = contents.split('\n')
    for line in lines:
      try:
        next_line = lines[linei + 1]
      except IndexError:
        continue
      if (line == '}' or line.endswith('}')) and len(next_line):
        if next_line[0].isalpha():
          lines[linei] = lines[linei] + '\n'

      linei += 1

    new_contents = '\n'.join(lines)
    with open(file, 'w') as f:
      f.write(new_contents)