import random
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"(oi|olá|e aí|bom dia|boa tarde|boa noite)",
        ["Saudações, Ashen One.", "Você está preparado para morrer... de novo?", "Bem-vindo ao Santuário do Elo de Fogo."]
    ],
    [
        r"(tchau|até mais|falou)",
        ["Descanse na próxima fogueira.", "Que as chamas te guiem.", "Até a próxima morte."]
    ],
    [
        r".(como.*subir.*nível|aumentar.*atributos).",
        ["Fale com a Guardiã do Fogo no Santuário para subir de nível usando almas."]
    ],
    [
        r".(espada.*forte|melhor.*arma|build.*dano).",
        ["A Claymore é versátil e poderosa. Mas lembre-se: a melhor arma é aquela que você domina."]
    ],
    [
        r".(chegar em Anor Londo|onde fica Anor Londo).",
        ["Você precisa derrotar o Iron Golem em Sen's Fortress e pegar a carona com os demônios alados."]
    ],
    [
        r".(como.*matar.*Ornstein.*Smough|luta contra os dois).",
        ["Tente focar em um deles primeiro. Derrotar Smough primeiro deixa Ornstein mais rápido, e vice-versa."]
    ],
    [
        r".(o que são humanidades|como usar humanidade).",
        ["Humanidade pode ser usada para reacender fogueiras, virar humano e invocar aliados."]
    ],
    [
        r".(invadir.*outros jogadores|pvp|ser invadido).",
        ["Você precisa estar em forma humana. Use Orbes de Olho Vermelho para invadir mundos."]
    ],
    [
        r".(como recuperar estus|ficar sem estus).",
        ["Descanse numa fogueira ou equipe o Anel da Madre da Reposição para ter mais cargas."]
    ],
    [
        r".(perdi minhas almas|morrer duas vezes).",
        ["Se você morrer antes de recuperar suas almas, elas se vão para sempre. Prepare-se melhor da próxima vez."]
    ],
    [
        r".(difícil|muito difícil|impossível).",
        ["Dark Souls não é difícil. Você que ainda não aprendeu a jogar... Git Gud."]
    ],
    [
        r".(quem é Gwyn|Senhor da Luz Solar|história do Gwyn).",
        ["Gwyn foi o Lorde da Luz Solar que sacrificou sua alma para manter a Primeira Chama acesa."]
    ],
    [
        r".(fogueiras|salvar progresso|checkpoints).",
        ["Fogueiras servem para descansar, recuperar vida e estus, e são seus checkpoints."]
    ],
    [
        r".(quem é Artorias|história do Artorias).",
        ["Artorias foi um dos Quatro Cavaleiros de Gwyn, corrompido pelo Abismo enquanto tentava salvá-lo."]
    ],
    [
        r".(o que é a maldição|como remover maldição).",
        ["Você pode remover a maldição com o item 'Pedra de Purificação' ou falando com um NPC como o Oswald de Carim."]
    ],
    [
        r".(vale a pena matar NPC|matei NPC sem querer).",
        ["Alguns NPCs têm itens únicos e questlines importantes. Use o Perdão com Oswald de Carim se precisar."]
    ],
    [
        r".(como abrir atalho|atalho escondido|muro invisível).",
        ["Algumas paredes falsas se abrem com um ataque. Teste em locais suspeitos."]
    ],
    [
        r".(como fazer pacto|quais são os pactos).",
        ["Você pode se juntar a pactos com certos NPCs. Cada pacto oferece recompensas e mecânicas únicas."]
    ],
    [
        r".(o que é NG\+|vale a pena NG\+|novo jogo plus).",
        ["NG+ é quando você recomeça o jogo mantendo seus equipamentos, mas os inimigos ficam mais fortes."]
    ],
    [
        r".(como invocar ajuda|jogar co-op).",
        ["Você precisa estar em forma humana e ver as marcas de invocação no chão. Use a Pedra Branca de Sinal Pequeno."]
    ],
    [
        r".(quais anéis usar|melhor anel|anéis bons).",
        ["O Anel de Havel aumenta a carga de equipamento. O Anel do Favor e Proteção é excelente para builds equilibradas."]
    ],
    [
        r".(dicas para iniciantes|sou novo|por onde começar).",
        ["Escolha uma arma que goste, não carregue mais que 70% de peso, e nunca subestime a esquiva."]
    ],
    [
        r".(qual.*seu.*nome.*|como*você*chama*).",
        ["Segredo de Estado :)"]
    ],
]

reflexoes_pt = {
    "eu": "você",
    "me": "te",
    "meu": "seu",
    "minha": "sua",
    "meus": "seus",
    "minhas": "suas",
    "sou": "é",
    "estou": "está",
    "era": "era",
    "fui": "foi",
    "serei": "será",
    "estive": "esteve",
    "estava": "estava",
    "estarei": "estará",
    "você": "eu",
    "vc": "eu",
    "te": "me",
    "seu": "meu",
    "sua": "minha",
    "seus": "meus",
    "suas": "minhas",
    "é": "sou",
    "está": "estou",
    "foi": "fui",
    "será": "serei",
    "esteve": "estive",
    "estava": "estava",
    "estará": "estarei",
    "nós": "vocês",
    "nosso": "seu",
    "nossa": "sua",
    "nossos": "seus",
    "nossas": "suas",
    "vocês": "nós",
    "seus": "nossos",
    "suas": "nossas",
}

chatbot = Chat(pares, reflexoes_pt)

def get_response(user_input):
    resposta = chatbot.respond(user_input)
    if resposta:
        return resposta
    else:
        return "Não entendi, poderia reformular a pergunta?"