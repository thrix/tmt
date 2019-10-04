#!/usr/bin/python3

import fmf
import re

def separator(level, length=66):
    return '=~^:-'[level] * length

print("Stories\n" + separator(0))

for node in fmf.Tree('.').prune(keys=['story'], whole=True):
    depth = len(re.findall('/', node.name)) - 1

    # Heading
    story = node.get('story')
    print('\n{}\n{}'.format(story.strip(), separator(depth, len(story))))

    # Description
    description = node.get('description')
    if description:
        print('\n' + description)

    # Examples
    examples = node.get('examples')
    if examples:
        print('\nExamples::\n')
        if isinstance(examples, str):
            examples = re.sub('^', '    ', examples.rstrip())
            examples = re.sub(r'\n', '\n    ', examples)
        elif isinstance(examples, list):
            examples = '    ' + '\n    '.join(examples)
        print(examples)
