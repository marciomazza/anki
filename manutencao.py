notes = find('is:due') + new
notes = set(find('is:due') + new)
pl = [c for n in notes for c in n.cards() if c.template()['name'] == 'Plural']
for c in pl:
    c.due = i
    i += 1
for c in pl: c.flush()
