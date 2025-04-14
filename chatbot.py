import random
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"(oi|olá|e aí|bom dia|boa tarde|boa noite)",
        ["Olá!", "Oi, tudo bem?", "E aí, como posso ajudar?"]
    ],
    [
        r"(tchau|até mais|falou)",
        ["Tchau!", "Até logo!", "Volte Nunca!"]
    ],
    [
        r".*(computador.*lento|PC.*rápido|notebook.*travando).*",
        ["Você pode tentar desinstalar programas desnecessários, desativar aplicativos que iniciam com o sistema e verificar por vírus. Uma limpeza de disco também pode ajudar."]
    ],
    [
        r".*(atualizar.*Windows|atualizações do Windows).*",
        ["Vá em 'Configurações' > 'Atualização e Segurança' > 'Windows Update' e clique em 'Verificar atualizações'."]
    ],
    [
        r".*(atalho.*print|captura de tela|print no Windows).*",
        ["Pressione a tecla PrtScn para capturar a tela toda, ou Alt + PrtScn para capturar apenas a janela ativa."]
    ],
    [
        r".*(instalar.*impressora|adicionar.*impressora|conectar.*impressora).*",
        ["Conecte a impressora ao computador (via cabo USB ou Wi-Fi), vá em 'Dispositivos e Impressoras' e clique em 'Adicionar impressora'."]
    ],
    [
        r".*(antivírus|proteger.*computador).*",
        ["Antivírus é um programa que protege seu computador contra ameaças. Alguns bons e gratuitos são o Windows Defender, Avast e AVG."]
    ],
    [
        r".*(sem internet|Wi-Fi.*parou|não consigo acessar).*",
        ["Verifique se o roteador está ligado, se os cabos estão conectados e tente reiniciar o modem e o roteador."]
    ],
    [
        r".*(mudar|trocar|alterar).*senha.*(Wi[- ]?Fi|internet|roteador).*",
        ["Acesse o roteador pelo navegador (geralmente em 192.168.0.1 ou 192.168.1.1), entre com usuário e senha padrão, e vá até a seção 'Wireless' ou 'Segurança'."]
    ],
    [
        r".*(Wi[- ]?Fi.*conectado.*sem internet|sinal.*sem internet).*",
        ["Pode ser um problema com a operadora, com o modem ou até uma configuração errada no roteador. Tente reiniciar os equipamentos e testar com outro dispositivo."]
    ],
    [
        r".*(acessar.*roteador|endereço IP do roteador|configurações do Wi[- ]?Fi).*",
        ["Digite o IP do roteador na barra do navegador (geralmente 192.168.0.1), depois entre com o usuário e senha. Se não souber, tente 'admin' para ambos ou dê uma conferida na parte traseira do roteador, alguns modelos contém as credenciais."]
    ],
    [
        r".*(alguém.*usando.*Wi[- ]?Fi|ver.*conectado).*internet.*",
        ["Acesse as configurações do roteador e veja os dispositivos conectados. Se houver nomes desconhecidos, troque a senha do Wi-Fi."]
    ],
    [
        r".*(limpar.*celular|apagar.*arquivos|liberar.*memória).*",
        ["Apague fotos e vídeos duplicados, desinstale apps que não usa e limpe o cache em 'Configurações > Armazenamento'."]
    ],
    [
        r".*(celular.*trava|muito lento).*",
        ["Reinicie o aparelho, feche apps em segundo plano e verifique se há atualizações do sistema."]
    ],
    [
        r".*(modo avião|desligar conexões).*",
        ["No Android ou iPhone, deslize a barra de cima para baixo e toque no ícone de avião. Isso desativa todas as conexões sem fio."]
    ],
    [
        r".*(celular.*não conecta.*Wi[- ]?Fi|Wi[- ]?Fi.*celular).*",
        ["Tente esquecer a rede e conectar de novo, reinicie o roteador e o celular, ou verifique se a senha está correta."]
    ],
    [
        r".*(transferir fotos|copiar fotos|passar fotos).*celular.*(PC|computador|notebook).*",
        ["Conecte o celular via cabo USB, selecione 'Transferir arquivos' no celular e copie as fotos para uma pasta no computador."]
    ],
    [
        r".*(criar senha segura|senha forte|senha difícil).*",
        ["Use pelo menos 8 caracteres, misture letras maiúsculas e minúsculas, números e símbolos. Ex: S3nH@F0rt3!"]
    ],
    [
        r".*(e-mail.*hackeado|invadido|vazado).*",
        ["Acesse o site 'haveibeenpwned.com', digite seu e-mail e veja se ele aparece em vazamentos de dados."]
    ],
    [
        r".*(autenticação.*dois fatores|verificação.*duas etapas|autenticação dupla).*",
        ["É uma camada extra de segurança onde, além da senha, você precisa de um código enviado por SMS ou app, como o Google Authenticator."]
    ],
    [
        r".*(programa.*não responde|fechar programa travado|aplicativo congelou).*",
        ["Pressione Ctrl + Shift + Esc, vá no Gerenciador de Tarefas, selecione o programa e clique em 'Finalizar tarefa'."]
    ],
    [
        r".*(programas essenciais|instalar.*PC novo|aplicativos básicos).*",
        ["Navegador (Chrome, Firefox), pacote Office ou similar, leitor de PDF, um descompactador de arquivos (como WinRAR ou 7-Zip), e Minecraft."]
    ]
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