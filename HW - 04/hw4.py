import re
import os
import docx

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
            if not beginning_found:
                tex_output.write(line)
            else:
                match = re.search(r'\\(sub)*section', line)
                if match:
                    tex_output.write('\\quad ' * line[match.start(): match.end()].count('sub') + line)

        tex_output.write('\\end{document}\n')

first_task('multistability.tex')
second_task('ifacconf.cls')
third_task('multistability.tex')

os.system("pandoc mod3-multistability.tex -s -o mod3-multistability.docx")

mod3 = docx.Document('mod3-multistability.docx')
for s in mod3.styles:
    if 'Heading ' in s.name:
        s.paragraph_format.left_indent = docx.shared.Inches(0.5 * (int(s.name.split()[-1]) - 1))
mod3.save('mod3-multistability.docx')
