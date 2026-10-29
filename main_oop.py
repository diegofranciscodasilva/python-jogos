import json
import os
from typing import Callable

from classes_jogos import JogoAdivinhacao, JogoJokenpo, JogoForca, JogoDados, JogoQuiz


class FliperamaApp:
    def __init__(self, arquivo_json="recordes_oop.json"):
        self.arquivo_json = arquivo_json
        self.recordes = self.carregar_recordes()

        self.adivinhacao = JogoAdivinhacao()
        self.jokenpo = JogoJokenpo()
        self.forca = JogoForca()
        self.dados = JogoDados()
        self.quiz = JogoQuiz()
        self.jogos_com_vitorias = {
            "1": ("adivinhacao", self.adivinhacao.iniciar),
            "2": ("jokenpo", self.jokenpo.iniciar),
            "3": ("forca", self.forca.iniciar),
        }

    def carregar_recordes(self):
        padrao = {"adivinhacao": 0, "jokenpo": 0, "forca": 0, "dados": 100, "quiz": 0}
        if not os.path.exists(self.arquivo_json):
            return padrao
        try:
            with open(self.arquivo_json, "r", encoding="utf-8") as f:
                recordes_salvos = json.load(f)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"O arquivo de recordes '{self.arquivo_json}' contém JSON inválido."
            ) from error

        if not isinstance(recordes_salvos, dict):
            raise ValueError(
                f"O arquivo de recordes '{self.arquivo_json}' deve conter um objeto JSON."
            )

        recordes = padrao.copy()
        for jogo, recorde in recordes_salvos.items():
            if jogo not in padrao:
                continue
            if isinstance(recorde, bool) or not isinstance(recorde, int) or recorde < 0:
                raise ValueError(
                    f"O recorde de '{jogo}' no arquivo '{self.arquivo_json}' "
                    "deve ser um inteiro não negativo."
                )
            recordes[jogo] = recorde

        return recordes

    def salvar_recordes(self) -> None:
        with open(self.arquivo_json, "w", encoding="utf-8") as f:
            json.dump(self.recordes, f, indent=4, ensure_ascii=False)

    def mostrar_menu(self) -> None:
        print("\n==================================")
        print("  🎮 FLIPERAMA ORIENTADO A OBJETOS 🎮")
        print("==================================")
        print("🏆 [Estatísticas / Recordes]")
        print(f"  • Adivinhação (Vitórias): {self.recordes['adivinhacao']}")
        print(f"  • Jokenpô (Vitórias): {self.recordes['jokenpo']}")
        print(f"  • Forca (Vitórias): {self.recordes['forca']}")
        print(f"  • Dados (Maior saldo): {self.recordes['dados']} fichas")
        print(f"  • Quiz (Maior pontuação): {self.recordes['quiz']} pts")
        print("----------------------------------")
        print("1. Jogar: Adivinhação")
        print("2. Jogar: Jokenpô")
        print("3. Jogar: Forca")
        print("4. Jogar: Dados (Cassino)")
        print("5. Jogar: Quiz Python")
        print("6. Sair")

    def registrar_vitoria(self, recorde: str, iniciar_jogo: Callable[[], int]) -> None:
        if iniciar_jogo() == 1:
            self.recordes[recorde] += 1
            self.salvar_recordes()
            print("💾 Vitória salva no JSON!")

    def jogar_dados(self) -> None:
        saldo = self.dados.iniciar()
        if saldo > self.recordes["dados"]:
            print(f"\n🌟 NOVO RECORDE NO CASSINO: {saldo} fichas!")
            self.recordes["dados"] = saldo
            self.salvar_recordes()
        else:
            print(f"\nVocê terminou com {saldo} fichas.")

    def jogar_quiz(self) -> None:
        pontos = self.quiz.iniciar()
        if pontos > self.recordes["quiz"]:
            print(f"\n🌟 NOVO RECORDE NO QUIZ: {pontos} pontos!")
            self.recordes["quiz"] = pontos
            self.salvar_recordes()
        else:
            print(f"\nVocê fez {pontos} pontos. O recorde atual é {self.recordes['quiz']}.")

    def executar(self):
        while True:
            self.mostrar_menu()
            opcao = input("\nEscolha uma opção (1 a 6): ").strip()

            if opcao in self.jogos_com_vitorias:
                recorde, iniciar_jogo = self.jogos_com_vitorias[opcao]
                self.registrar_vitoria(recorde, iniciar_jogo)
            elif opcao == "4":
                self.jogar_dados()
            elif opcao == "5":
                self.jogar_quiz()
            elif opcao == "6":
                print("\nSalvando recordes e encerrando... Até logo! 👋")
                self.salvar_recordes()
                break
            else:
                print("\n❌ Opção inválida! Escolha entre 1 e 6.")

if __name__ == "__main__":
    app = FliperamaApp()
    app.executar()
    