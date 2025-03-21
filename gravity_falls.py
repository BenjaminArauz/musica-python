from music21 import stream, note, chord, instrument, tempo, tie

def crear_acorde(pitches, duracion=1, beam=None, tie_type=None):
    acorde = chord.Chord(pitches)
    acorde.duration.quarterLength = duracion

    if beam:
        acorde.beams.append(beam)
    
    if tie_type:
        acorde.tie = tie.Tie(tie_type)

    return acorde

def agregar_acorde(pentagrama, pitches, duracion=1, beam=None, tie_type=None):
    acorde = crear_acorde(pitches, duracion, beam, tie_type)
    pentagrama.append(acorde)

def crear_nota(pitch, duracion=1, beam=None, tie_type=None):
    nota = note.Note(pitch)
    nota.duration.quarterLength = duracion

    if beam:
        nota.beams.append(beam)
    
    if tie_type:
        nota.tie = tie.Tie(tie_type)
    
    return nota

def agregar_nota(pentagrama, pitch, duracion=1, beam=None, tie_type=None):
    nota = crear_nota(pitch, duracion, beam, tie_type)
    pentagrama.append(nota)

def agregar_silencio(pentagrama, duracion=1):
    silencio = note.Rest()
    silencio.duration.quarterLength = duracion
    pentagrama.append(silencio)

def main():
    # Crear el pentagrama e insertar la flauta como instrumento
    pentagrama = stream.Stream()
    pentagrama.insert(0, instrument.Flute())  # 🎵 Configura la partitura para flauta
    pentagrama.append(tempo.MetronomeMark(number=120))

    # Primer compás
    agregar_nota(pentagrama, "D", 3)
    agregar_nota(pentagrama, "E")

    # Segundo compás
    agregar_nota(pentagrama, "F", 4)

    # Tercer compás
    for pitch, duration in [("A", 1.5), ("G", 1.5), ("A", 1)]:
        agregar_nota(pentagrama, pitch, duration)

    # Cuarto compás
    agregar_nota(pentagrama, "C", 4)

    # Quinto compás
    agregar_nota(pentagrama, "D", 3)
    agregar_nota(pentagrama, "E")

    # Sexto compás
    for pitch, duration in [("F", 2), ("E", 2)]:
        agregar_nota(pentagrama, pitch, duration)

    # Séptimo compás
    for pitch, duration in [("G", 2), ("A", 2)]:
        agregar_nota(pentagrama, pitch, duration)

    # Octavo compás
    for pitch, duration in [("G", 2), ("F", 2)]:
        agregar_nota(pentagrama, pitch, duration)

    # Noveno compás
    agregar_silencio(pentagrama)
    for _ in range(3):
        agregar_nota(pentagrama, "F")

    # Décimo compás
    for pitch in ["A", "A", "G", "F"]:
        agregar_nota(pentagrama, pitch)

    # Décimo primer compás
    agregar_silencio(pentagrama, 1)
    for _ in range(3):
        agregar_nota(pentagrama, "A")

    # Décimo segundo compás
    for pitch in ["G", "A", "G", "F"]:
        agregar_nota(pentagrama, pitch)

    # Décimo tercer compás
    agregar_silencio(pentagrama, 1)
    for _ in range(3):
        agregar_nota(pentagrama, "F")

    # Décimo cuarto compás
    for pitch in ["A", "A", "G", "F"]:
        agregar_nota(pentagrama, pitch)

    # Décimo quinto compás
    agregar_silencio(pentagrama, 1)
    for _ in range(3):
        agregar_nota(pentagrama, "A")

    # Décimo sexto compás
    agregar_silencio(pentagrama, 1)
    for _ in range(3):
        agregar_nota(pentagrama, "C#5")

    # Décimo séptimo compás
    agregar_silencio(pentagrama, 1)
    for _ in range(3):
        agregar_nota(pentagrama, "F")

    # Décimo octavo compás
    for pitch in ["A", "F", "G", "F"]:
        agregar_nota(pentagrama, pitch)

    # Décimo noveno compás
    agregar_silencio(pentagrama, 1)
    for _ in range(3):
        agregar_nota(pentagrama, "B-4")

    # Vigésimo compás
    for pitch, duration in [("G", 2), ("C5", 2)]:
        agregar_nota(pentagrama, pitch, duration)

    # Vigésimo primer compás
    for pitch, duration in [("A", 2), ("C#5", 2)]:
        agregar_nota(pentagrama, pitch, duration)

    # Último compás
    agregar_nota(pentagrama, "D5", 4)

    # Mostrar partitura
    #pentagrama.show()

    # Guardar el archivo MIDI
    pentagrama.write('midi', 'gravity_falls_intro.mid')

if __name__ == "__main__":
    main()