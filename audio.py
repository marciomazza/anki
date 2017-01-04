from downloadaudio.download import do_download, get_note_fields


def find(query):
    return [mw.col.getNote(id) for id in mw.col.findNotes(query)]

notes = [n for n in find('is:due') if not n['German_Audio']]
canceled = []


def download(note):
    print('%s %s -> %s' % tuple(
        note[k] for k in ('Noun_Article', 'German', 'English')))
    do_download(note, get_note_fields(note), 'de')
    if note['German_Audio']:
        print('  ', note['German_Audio'])
        note.flush()
    else:
        canceled.append(note.id)


# new = [n for n in find('"deck:Duolingo German" is:new')
#        if any(c.due < 20000 for c in n.cards())]
new = find('"deck:Duolingo German" is:new')
new = sorted(new, key=lambda n: min(c.due for c in n.cards()))

due = find('is:due')

def more(notes=new, limit=10):
    for note in [n for n in notes
                 if not n['German_Audio'] and n.id not in canceled][:limit]:
        download(note)

canceled = [1460960126017,
            1460960126613,
            1460960126854,
            1460960127358,
            1460960127372,
            1460960125913,
            1460960125914,
            1460960125915,
            1460960125969,
            1460960126005,
            1460960126018,
            1460960126019,
            1460960126020,
            1460960126239,
            1460960126615,
            1460960126739]
