import random

class JogoAdivinhacao:
    def iniciar(self):
        print("\n--- JOGO DE ADIVINHAÇÃO ---")
        numero_secreto = random.randint(1, 10)
        try:
            palpite = int(input("Adivinhe um número entre 1 e 10: "))
            if not 1 <= palpite <= 10:
                print("⚠️ Escolha um número entre 1 e 10.")
                return 0
            if palpite == numero_secreto:
                print("🎉 Parabéns, você acertou!")
                return 1
            else:
                print(f"❌ Que pena! O número secreto era {numero_secreto}.")
                return 0
        except ValueError:
            print("⚠️ Digite apenas números inteiros válidos.")
            return 0


class JogoJokenpo:
    def iniciar(self):
        print("\n--- JOKENPÔ (PEDRA, PAPEL E TESOURA) ---")
        opcoes = ["pedra", "papel", "tesoura"]
        usuario = input("Escolha (pedra, papel ou tesoura): ").strip().lower()
        
        if usuario not in opcoes:
            print("⚠️ Opção inválida!")
            return 0
            
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")
        
        if usuario == computador:
            print("⚖️ Empate!")
            return 0
        elif (usuario == "pedra" and computador == "tesoura") or \
             (usuario == "papel" and computador == "pedra") or \
             (usuario == "tesoura" and computador == "papel"):
            print("🎉 Você venceu!")
            return 1
        else:
            print("😢 O computador venceu!")
            return 0


class JogoForca:
    def iniciar(self):
        print("\n=== BEM-VINDO AO JOGO DA FORCA! ===")
        palavras = ["python", "programacao", "desenvolvedor", "computador", "tecnologia"]
        palavra_secreta = random.choice(palavras)
        letras_certas = set()
        letras_erradas = set()
        
        while len(letras_erradas) < 6:
            palavra_mostrada = "".join([l + " " if l in letras_certas else "_ " for l in palavra_secreta])
            print(f"\nPalavra: {palavra_mostrada.strip()}")
            print(f"Erros: {len(letras_erradas)} de 6")
            
            if "_" not in palavra_mostrada:
                print(f"\n🎉 PARABÉNS! Você acertou a palavra: '{palavra_secreta}'!")
                return 1
                
            palpite = input("Digite uma letra: ").lower().strip()
            if len(palpite) != 1 or not palpite.isalpha():
                print("⚠️ Digite apenas uma letra válida.")
                continue
                
            if palpite in letras_certas or palpite in letras_erradas:
                print("⚠️ Você já tentou essa letra!")
                continue
                
            if palpite in palavra_secreta:
                print(f"✅ Boa! A letra '{palpite}' está na palavra.")
                letras_certas.add(palpite)
            else:
                print(f"❌ A letra '{palpite}' não está na palavra.")
                letras_erradas.add(palpite)
                
        print(f"\n💥 GAME OVER! A palavra era: '{palavra_secreta}'.")
        return 0


class JogoDados:
    def iniciar(self):
        print("\n=== CASSINO PYTHON: JOGO DOS DADOS ===")
        saldo = 100
        
        while saldo > 0:
            print(f"\n💰 Saldo atual: {saldo} ficha(s)")
            opcao = input("Deseja jogar uma rodada? (s/n): ").strip().lower()
            if opcao == 'n':
                print(f"Você parou com {saldo} fichas.")
                break
            elif opcao != 's':
                print("Opção inválida! Digite 's' ou 'n'.")
                continue
                
            try:
                aposta = int(input("Quanto deseja apostar em fichas? "))
                if aposta <= 0:
                    print("A aposta deve ser maior que zero.")
                    continue
                if aposta > saldo:
                    print("Você não tem saldo suficiente!")
                    continue
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
                continue
                
            dado1, dado2 = random.randint(1, 6), random.randint(1, 6)
            soma = dado1 + dado2
            print(f"🎲 Dados: {dado1} e {dado2} (Soma: {soma})")
            
            if soma > 7:
                print(f"🎉 Você venceu e ganhou +{aposta} fichas!")
                saldo += aposta
            else:
                print(f"😢 Você perdeu -{aposta} fichas.")
                saldo -= aposta
                
        return saldo

class JogoQuiz:
    def iniciar(self):
        print("\n=== QUIZ DE CONHECIMENTOS PYTHON ===")
        perguntas = [
            {
                "pergunta": "Qual palavra-chave é utilizada para definir uma função em Python?",
                "alternativas": ["A) func", "B) define", "C) def", "D) function"],
                "resposta": "C"
            },
            {
                "pergunta": "Qual das seguintes estruturas de dados é mutável (pode ser alterada)?",
                "alternativas": ["A) Tupla (tuple)", "B) Lista (list)", "C) String", "D) Inteiro"],
                "resposta": "B"
            },
            {
                "pergunta": "Como você faz um comentário de uma linha em Python?",
                "alternativas": ["A) // Comentário", "B) /* Comentário */", "C) # Comentário", "D) <!-- Comentário -->"],
                "resposta": "C"
            }
        ]
        
        pontos = 0
        total = len(perguntas)
        
        for i, item in enumerate(perguntas, start=1):
            print(f"\nQuestão {i}: {item['pergunta']}")
            for alt in item["alternativas"]:
                print(alt)
                
            while True:
                resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
                if resposta in {"A", "B", "C", "D"}:
                    break
                print("⚠️ Escolha uma alternativa válida: A, B, C ou D.")

            if resposta == item["resposta"]:
                print("✅ Resposta Correta!")
                pontos += 1
            else:
                print(f"❌ Resposta Incorreta! A correta era: {item['resposta']}")
                
        print(f"\nFim do Quiz! Você acertou {pontos} de {total} perguntas.")
        return pontos  # Retorna a pontuação total para o menu salvar
    