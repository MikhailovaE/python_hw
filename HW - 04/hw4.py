import os
import re

def first_task(filename):
    with open(filename, 'r') as tex_input, open('mod1-' + filename, 'w') as tex_output:
        tex_data = tex_input.read()
        tex_data.replace('hypothesis', 'conjecture').replace('hypothesises', 'conjectures')
        tex_output.write(tex_data)

def second_task(filename):
    with open(filename, 'r') as tex_input, open('mod2-' + filename, 'w') as tex_output:
        output = ''
        for line in tex_input:
            try:
                index = line.index('fontsize')
                parts = re.split(r'(\d+)', line[index:])
                for i in range(len(parts)):
                    if parts[i].isdigit():
                        parts[i] = str(int(parts[i]) + 2)
                tex_output.write(line[:index] + ''.join(parts))
            except ValueError:
                tex_output.write(line)

def third_task(filename):
    with open(filename, 'r') as tex_input, open('mod3-' + filename, 'w') as tex_output:
        beginning_found = False
        for line in tex_input:
            if '\\begin{document}' in line:
                tex_output.write(line)
                beginning_found = True
            if '\\section' in line or not beginning_found:
                tex_output.write(line)
        tex_output.write('\\end{document}\n')
os.system("pandoc mod3-multistability.tex -s -o mod3-multistability.docx")


first_task('multistability.tex')
second_task('ifacconf.cls')
third_task('multistability.tex')
