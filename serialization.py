from marshmallow import Schema, fields


class CursoSchema(Schema):
    sigla = fields.Str()
    nome = fields.Str()


class Curso:
    def __init__(self, sigla, nome, professor):
        self.sigla = sigla
        self.nome = nome
        self.professor = professor


curso = Curso("MED", "Medicina", "John Doe")

curso_schema = CursoSchema()
curso_dict = curso_schema.dump(curso)

print(curso_dict)