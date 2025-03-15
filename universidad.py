universidad = {
"estudiantes": {
"1": {
"nombre": "Juan",
"cursos": {
"1": {
"nombre": "Matemáticas",
"nota": 2,
"horario": "Lunes 10:00"
},
"2": {
"nombre": "Física",
"nota": 3,
"horario": "Martes 11:00"
}
}
},
"2": {
"nombre": "María",
"cursos": {
"1": {
"nombre": "Matemáticas",
"nota": 4,
"horario": "Lunes 10:00"
},
"3": {
"nombre": "Química",
"nota": 5,
"horario": "Miércoles 12:00"
}
}
}
},
"cursos": {
"1": {
"nombre": "Matemáticas",
"profesor": "Profesor 1",
"estudiantes": ["1", "2"]
},
"2": {
"nombre": "Física",
"profesor": "Profesor 2",
"estudiantes": ["1"]
},
"3": {
"nombre": "Química",
"profesor": "Profesor 3",
"estudiantes": ["2"]
}
},
"profesores": {
"1": {
"nombre": "Profesor 1"
},
"2": {
"nombre": "Profesor 2"
},
"3": {
"nombre": "Profesor 3"
}
}
}



print(" Estudiantes ")
for id_estudiante, estudiante in universidad["estudiantes"].items():
    print(f"Estudiante ID: {id_estudiante}, Nombre: {estudiante['nombre']}")
    for id_curso, curso in estudiante["cursos"].items():
        print(f"  - Curso: {curso['nombre']}, Nota: {curso['nota']}, Horario: {curso['horario']}")
    print()

print(" Cursos ")
for id_curso, curso in universidad["cursos"].items():
    print(f"Curso ID: {id_curso}, Nombre: {curso['nombre']}, Profesor: {curso['profesor']}")
    print("  Estudiantes inscritos:", ", ".join(curso["estudiantes"]))
    print()

print(" Profesores ")
for id_profesor, profesor in universidad["profesores"].items():
    print(f"Profesor ID: {id_profesor}, Nombre: {profesor['nombre']}")