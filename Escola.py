class Escola:
    def __init__(self, nome, alunos=None):
        if alunos is None:
            alunos = []
        self.nome = nome
        self.alunos = alunos

    def adicionarAluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno} adicionado com sucesso")

    def removerAluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            print(f"Aluno {aluno} foi removido com sucesso")
        else:
            print(f"Aluno {aluno} não foi encontrado na lista")

    def listarAlunos(self):
        if self.alunos:
            print(f"Alunos da escola {self.nome}:")
            for aluno in self.alunos:
                print(aluno)
        else:
            print(f"Não há alunos cadastrados na escola {self.nome}")

escola1 = Escola("Escola Ideal")
escola1.listarAlunos()
escola1.adicionarAluno("Gabriel")
escola1.adicionarAluno("Yago")
escola1.listarAlunos()
escola1.removerAluno("Gabriel")
escola1.listarAlunos()

escola2 = Escola("Colégio Cesupa", ["Carlos", "Ana"])
escola2.listarAlunos()
escola2.adicionarAluno("Daniela")
escola2.listarAlunos()
