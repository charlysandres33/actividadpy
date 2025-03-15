perfil_usuario = {
    "nombre": "Carlos",
    "ciudad": "Cali",
    "edad": 21,
    "amigos": [
        {"nombre": "Victor", "tiempo de amistad": 3},
        {"nombre": "Daniel", "tiempo de amistad": 5},
    ],
    "lista de post": [
        {
            "contenido": "En las olas de Brasil",
            "likes": 1000,
            "comentarios": [
                {"usuario": "David", "texto": "Yo estuve el año pasado"}
            ]
        }
    ]
}


nuevo_post = {
    "contenido": "En el hotel más grande del mundo",
    "likes": 5500,
    "comentarios": [
        {"usuario": "Jose", "texto": "Se ve increíble"}
    ]
}


perfil_usuario["lista de post"].append(nuevo_post)


perfil_usuario["ciudad"] = "Madrid"


try:
    perfil_usuario["amigos"].remove({"nombre": "Victor", "tiempo de amistad": 3})
except ValueError:
    print("El amigo no se encontró en la lista.")


print("Perfil actualizado:")
print("Ciudad:", perfil_usuario["ciudad"])

print("Lista de amigos:")
for amigo in perfil_usuario["amigos"]:
    print(f"{amigo['nombre']} ({amigo['tiempo de amistad']} años de amistad)")

print("Lista de posts:")
for post in perfil_usuario["lista de post"]:
    print(f"Contenido: {post['contenido']}")
    print(f"Likes: {post['likes']}")
    print("Comentarios:")
    for comentario in post["comentarios"]:
        print(f"  {comentario['usuario']}: {comentario['texto']}")
    print("---")
