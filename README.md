# Fliperama Orientado a Objetos

Um fliperama de terminal desenvolvido em Python, com cinco jogos e registro local de recordes em JSON.

## Requisitos

- Python 3 instalado.
- Terminal com suporte a entrada interativa.

O projeto usa apenas módulos da biblioteca padrão do Python; não é necessário instalar dependências.

## Como executar

Abra o terminal na pasta do projeto e execute:

```powershell
python main_oop.py
```

Em alguns sistemas, o comando pode ser `python3 main_oop.py`.

## Jogos

1. **Adivinhação** — tente acertar um número entre 1 e 10.
2. **Jokenpô** — jogue pedra, papel e tesoura contra o computador.
3. **Forca** — descubra a palavra antes de acumular seis erros.
4. **Jogo dos dados** — aposte fichas; uma soma maior que 7 vence a rodada.
5. **Quiz de Python** — responda a três perguntas de conhecimentos básicos.

O menu também exibe as vitórias, o maior saldo no jogo dos dados e a maior pontuação no quiz.

## Recordes

O arquivo `recordes_oop.json` é criado na pasta de execução para armazenar os recordes entre partidas. Se ainda não existir, o programa começa com valores padrão. Campos ausentes em um arquivo válido também recebem os valores padrão; se o JSON estiver corrompido ou contiver recordes inválidos, o programa informa o erro em vez de substituir os dados silenciosamente.

## Arquivos do projeto

- `main_oop.py` — menu principal, carregamento e gravação dos recordes.
- `classes_jogos.py` — implementação das classes dos cinco jogos.

## 👨‍💻 Autor

### Diego Francisco da Silva

Desenvolvedor Front-End em formação e estudante de Engenharia de Software.

- **[Site Empresa](https://diegofranciscodasilva.github.io/dev-software-web/)**: dev.software.web Site Empresa
- **[LinkedIn](https://www.linkedin.com/in/diego-francisco-da-silva/)**: diego-francisco-da-silva
- **[GitHub](https://github.com/diegofranciscodasilva)**: diegofranciscodasilva
- **[Instagram](https://www.instagram.com/diego_francisco_da_silva/)**: @diego_francisco_da_silva
- **[Instagram](https://www.instagram.com/dev.software.web/)**: @dev.software.web

---

Feito com ❤️ por Diego.
