from tracemalloc import start


def song(notes,order,decalate) :
    numberNotes = len(notes)
    startNote = notes[decalate]
    notes = [notes[elem] for elem in order]
    notes.insert(0,startNote)
    return notes

print(song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))