from music21 import stream, clef, key, meter, note, chord, instrument, tempo, tie

def crear_acorde(pitches, duracion=1, beam=None, tie_type=None):
    """Crea un acorde con las características especificadas."""
    acorde = chord.Chord(pitches)
    acorde.duration.quarterLength = duracion

    if beam:
        acorde.beams.append(beam)
    
    if tie_type:
        acorde.tie = tie.Tie(tie_type)

    return acorde

def agregar_acorde(pentagrama_base, pitches, duracion=1, beam=None, tie_type=None):
    """Agrega un acorde a un pentagrama."""
    acorde = crear_acorde(pitches, duracion, beam, tie_type)
    pentagrama_base.append(acorde)

def crear_nota(pitch, duracion=1, beam=None, tie_type=None):
    """Crea una nota con las características especificadas."""
    nota = note.Note(pitch)
    nota.duration.quarterLength = duracion

    if beam:
        nota.beams.append(beam)
    
    # Añadir ligadura
    if tie_type:
        nota.tie = tie.Tie(tie_type)
    
    return nota

def agregar_nota(pentagrama_base, pitch, duracion=1, beam=None, tie_type=None):
    """Agrega una nota a un pentagrama."""
    nota = crear_nota(pitch, duracion, beam, tie_type)
    pentagrama_base.append(nota)

def agregar_silencio(pentagrama_base, duracion=1):
    """Agrega un silencio de la duración especificada al pentagrama."""
    silencio = note.Rest()
    silencio.duration.quarterLength = duracion
    pentagrama_base.append(silencio)

def agregar_compases_repetidos(pentagrama_base):
    """ Agregar notas de secuencia de notas y silencios """
    # Primer compas
    agregar_silencio(pentagrama_base, 1)
    agregar_nota(pentagrama_base, "C#5", 0.5, "start")
    agregar_nota(pentagrama_base, "A4", 0.5, "stop")
    agregar_nota(pentagrama_base, "B", 0.5)
    agregar_nota(pentagrama_base, "C#5", 1)
    agregar_nota(pentagrama_base, "A4", 0.5, "start", "start")

    # Segundo compas
    agregar_nota(pentagrama_base, "A4", 1, "stop", "stop")
    agregar_nota(pentagrama_base, "C#5", 0.5, "start")
    agregar_nota(pentagrama_base, "B4", 0.5, "stop", "start")
    agregar_nota(pentagrama_base, "B4", 0.5, "stop")
    agregar_nota(pentagrama_base, "A4", 1)
    agregar_nota(pentagrama_base, "F#4", 1)

    # Tercer compas
    agregar_nota(pentagrama_base, "A4", 1)
    agregar_nota(pentagrama_base, "B4", 1)
    agregar_nota(pentagrama_base, "A4", 1)

def agregar_silencios_repetidos(pentagrama_base):
    """ Agregar notas de silencios repetidos """
    # Primer compas
    agregar_acorde(pentagrama_base, ["A3", "E4"], 4, "start", "start")
    # Segundo compas
    agregar_acorde(pentagrama_base, ["A3", "E4"], 4, "stop", "stop")

def agregar_parte_sol(pentagrama_base):
    """  Agregar la parte de sol al pentagrama """
    # Primeros tres compases
    agregar_compases_repetidos(pentagrama_base)
    agregar_nota(pentagrama_base, "F#4", 0.5)

    # Cuarto compas
    agregar_nota(pentagrama_base, "G#4", 0.5, "start")
    agregar_nota(pentagrama_base, "F#4", 0.5, "continue")
    agregar_nota(pentagrama_base, "G#4", 0.5, "continue")
    agregar_acorde(pentagrama_base, ["F#4", "A4"], 0.5, "stop", "start")
    agregar_acorde(pentagrama_base, ["F#4", "A4"], 0.5, "stop")
    agregar_acorde(pentagrama_base, ["G#4", "B4"], 1.5)

    # Quinto - septimo compas
    agregar_compases_repetidos(pentagrama_base)
    agregar_nota(pentagrama_base, "G#4", 0.5, "stop", "start")

    # Octavo compas
    agregar_nota(pentagrama_base, "G#4", 3, "stop")
    agregar_silencio(pentagrama_base, 1)

    # Noveno compas
    agregar_silencio(pentagrama_base, 1)
    agregar_acorde(pentagrama_base, ["C#5", "E4"], 0.5, "start", "start")
    agregar_acorde(pentagrama_base, ["B4", "D4"], 0.5, "stop", "start")
    agregar_acorde(pentagrama_base, ["B4", "D4"], 0.5, "stop", "stop")
    agregar_acorde(pentagrama_base, ["C#5", "E4"], 1)
    agregar_acorde(pentagrama_base, ["A4", "C#4"], 0.5, "start", "start")

    # Decimo compas
    agregar_acorde(pentagrama_base, ["A4", "C#4"], 1, "stop", "stop")
    agregar_acorde(pentagrama_base, ["C#5", "E4"], 0.5, "start", "start")
    agregar_nota(pentagrama_base, "A4", 0.5, "stop", "stop")
    agregar_nota(pentagrama_base, "B4", 0.5)
    agregar_nota(pentagrama_base, "C#5", 1.5)

    # Decimo primer compas
    agregar_silencio(pentagrama_base, 1)
    agregar_acorde(pentagrama_base, ["F#4", "C#5"], 0.5, "start", "start")
    agregar_nota(pentagrama_base, "B4", 0.5, "stop", "start")
    agregar_nota(pentagrama_base, "B4", 0.5, "stop", "stop")
    agregar_acorde(pentagrama_base, ["F#4", "C#5"], 1)
    agregar_nota(pentagrama_base, "A4", 0.5, "start", "start")

    # Decimo segundo compas
    agregar_nota(pentagrama_base, "A4", 1, "stop", "stop")
    agregar_acorde(pentagrama_base, ["F#4", "B3"], 1)
    agregar_nota(pentagrama_base, "A4", 0.5)
    agregar_nota(pentagrama_base, "B4", 1)
    agregar_acorde(pentagrama_base, ["A4", "F#4", "B3"], 1)

    
def agregar_parte_fa(pentagrama_base):
    """ Agregar la parte de fa al pentagrama """
    # Primer, segundo compas
    agregar_silencios_repetidos(pentagrama_base)

    # Tercer compas
    agregar_acorde(pentagrama_base, ["D3", "A3"], 4)

    # Cuarto compas
    agregar_acorde(pentagrama_base, ["E3", "D4"], 4)

    # Quinto, sexto compas
    agregar_silencios_repetidos(pentagrama_base)

    # Septimo compas
    agregar_acorde(pentagrama_base, ["A3", "D3"], 2, "start", "start")
    agregar_acorde(pentagrama_base, ["A3", "D3"], 1.5, "stop", "stop")
    agregar_acorde(pentagrama_base, ["D4", "E3"], 0.5, "start", "start")

    # Octavo compas
    agregar_acorde(pentagrama_base, ["D4", "E3"], 3, "stop", "stop")
    agregar_silencio(pentagrama_base, 1)

    # Noveno compas
    agregar_nota(pentagrama_base, "A2", 1)
    agregar_silencio(pentagrama_base, 1)
    agregar_nota(pentagrama_base, "E2", 1)
    agregar_silencio(pentagrama_base, 1)

    # Decimo compas
    agregar_nota(pentagrama_base, "A2", 1)
    agregar_silencio(pentagrama_base, 1)
    agregar_nota(pentagrama_base, "A2", 1)
    agregar_silencio(pentagrama_base, 1)

    # Decimo primer compas
    agregar_nota(pentagrama_base, "D3", 1)
    agregar_silencio(pentagrama_base, 1)
    agregar_nota(pentagrama_base, "D3", 1)
    agregar_silencio(pentagrama_base, 1)

    # Decimo primer compas
    agregar_nota(pentagrama_base, "D#3", 1)
    agregar_silencio(pentagrama_base, 1)
    agregar_nota(pentagrama_base, "D#3", 1)
    agregar_silencio(pentagrama_base, 1)
    

def main():
    """ Funcionalidad principal """
    pentagrama = stream.Stream()
    tiempo = tempo.MetronomeMark(number=129)

    # Dividir el pentagrama en dos partes (sol, fa)
    parte_sol = stream.Part()
    parte_fa = stream.Part()

    # Claves de sol, fa
    clave_sol = clef.GClef()
    clave_fa = clef.FClef()

    # Insertar claves
    parte_sol.insert(0, clave_sol)
    parte_fa.insert(0, clave_fa)

    # Insertar las notas de las partes
    agregar_parte_sol(parte_sol)
    agregar_parte_fa(parte_fa)

    # Insertar el tiempo (crear un objeto MetronomeMark separado para cada parte)
    tiempo_sol = tempo.MetronomeMark(number=129)
    tiempo_fa = tempo.MetronomeMark(number=129)
    parte_sol.insert(0, tiempo_sol)
    parte_fa.insert(0, tiempo_fa)

    # Insertar la armadura (crear un objeto KeySignature separado para cada parte)
    armadura_sol = key.KeySignature(3)
    armadura_fa = key.KeySignature(3)
    parte_sol.insert(0, armadura_sol)
    parte_fa.insert(0, armadura_fa)

    # Insertar las partes al pentagrama
    pentagrama.append(parte_sol)
    pentagrama.append(parte_fa)
    
    # Mostrar partitura
    #pentagrama.show()

    # Guardar el archivo MIDI
    pentagrama.write('midi', 'here_comes_the_sun.mid')

if __name__ == "__main__":
    main()