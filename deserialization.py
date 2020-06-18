from marshmallow import Schema, fields


class CursoSchema(Schema):
    sigla = fields.Str(required=True)
    nome = fields.Str(required=True)
    professor = fields.Str()


novo_curso = {
    "sigla": "Med",
    "nome": "Medicina",
    "professor": "John Doe"
}

curso_schema = CursoSchema()
curso = curso_schema.load(novo_curso)

print(curso)