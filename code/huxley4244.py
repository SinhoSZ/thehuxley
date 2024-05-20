class Aluno: # A classe Aluno armazena o nome e as três notas de cada aluno, além da média e da situação.
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = 0.0
        self.situacao = ""

    def calcular_media_e_situacao(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3.0
        if self.media >= 7.0:
            self.situacao = "Aprovado"
        elif self.media >= 3.0:
            self.situacao = "Final"
        else:
            self.situacao = "Reprovado"

def ordenar_alunos_por_nome(alunos):
    return sorted(alunos, key=lambda aluno: aluno.nome) # sorted ordenar a lista de alunos pelo nome.

def main():
    n = int(input())

    alunos = []

    for _ in range(n):
        nome = input()
        dados = input().split()
        nota1 = float(dados[0])
        nota2 = float(dados[1])
        nota3 = float(dados[2])
        aluno = Aluno(nome, nota1, nota2, nota3)
        aluno.calcular_media_e_situacao()
        alunos.append(aluno)

    alunos = ordenar_alunos_por_nome(alunos)

    for aluno in alunos:
        print(f"Aluno: {aluno.nome}\nMedia: {aluno.media:.2f}\nSitucao: {aluno.situacao}\n")

if __name__ == "__main__":
    main()