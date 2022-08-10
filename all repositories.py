#cor do texto
#o GREEN é o nome da cor, então colocar desse jeito em inglês
from colorama import Fore, Back, Style 
print(Fore.GREEN) 

print(f'''

esse é um script que tem todos os meus outros scripts em um só
digite help para ver os scripts
digite criador para ver o criador

''')

    #loop do input
loop="positivo"
while loop == "positivo":

    P1 = input("... ")

        #criador
    if P1 == "criador":
        print(f'''

        criador: pedro
        github: pedropy09
        telegram: Pedro_py
        link: https://t.me/Pedro_py

        ''')

        #help
    elif P1 == "help":
        print(f'''

        ╭─────────────────────────────
        ╎┝〢 help-people-in-repository
        ╎┝〢 digite: help-people
        ╎
        ╎┝〢 pedra-papel-tesoura
        ╎┝〢 digite tesoura
        ╎
        ╎┝〢 cassino em número
        ╎┝〢 digite cassino
        ╎
        ╎┝〢 paineArtText
        ╎┝〢 digite paineArt
        ╎
        ╎┝〢 auto-text
        ╎┝〢 digite auto-text
        ╎
        ╎┝〢 calculadora
        ╎┝〢 digite calc
        ╎
        ╎〢curso
        ╎〢digite curso
        ╰─────────────────────────────

        ''')

        #calculadora , calc
    elif P1 == "calc":
        print(f'''

        só uma calculadora básico, ela só usa + mesmo
        
        ''')
        n1 = int(input("digite um número: "))
        n2 = int(input("digita outro: "))
        s = n1 + n2
        print("valor:", s)




        #auto text , auto-text
    elif P1 == "auto-text":
        print()
        print("bem vindo ao save-text ")
#gato
        print(f'''
|\---/|
| o_o |
 \_^_/
        ''')
#ideia
        print("(tirei a ideia do autokey)")
        print("para ver a explicação do autokey digita autokey")
#espaço
        print()
#explicação
        print(f'''
essa é uma ferramenta facil que fiz
você pode escrever o que quiser que no final ela mostra
sei que você pode usa o bloco de notas pra salvar seus texto kkk
mais eu fiz só pra passa o tempo mesmo e relaxa 🦝
        ''')

        #S1/S2/S3
        S1 = input("escreva seu texto: ")

        #respostas
        print("seu texto:", S1)

        #autokey
        if S1 == "autokey":
            print (f'''
Traduzido do inglês-
O AutoKey é um aplicativo de script de código aberto gratuito para Linux.
O AutoKey permite ao usuário definir teclas de atalho e acionar frases que
se expandem para texto predefinido
            ''')


        #cassino em número , cassino
    elif P1 == "cassino":

        print("Bem vindo")
        print("logo avisando que esse cassino é básico")
        print("[a] começar")
        print("nome de user no telegram: pedro_py")
            #começo
        print("")
        r = input("")
            #a
        if r == "a":
            resposta = input("coloque seu nome de usuário:")
            print("bem vindo", (resposta))
            print("")
            import random
            print("seu jogo foi:")
            resposta = ["177", "771", "717", "171", "711", "117", "117", "177", "771", "777", "111"]
            print (random.choice(resposta))

        #pedra papel tesoura , tesoura
    elif P1 == "tesoura":
        print("pedra papel tesoura simples.")
        print(f'''
        pedra
        papel
        tesoura
        ''')
        input("escolhe uma das opções: ")
        import random
        resposta = ["pedra", "papel", "tesoura"]
        print (random.choice(resposta))



        #cursos
    elif P1== "cursos":
        print()
        print("bem vindo")

                #S1
        S1 = input("qual curso você vai escolher?: ")

            #python
        if S1 == "python":
            print(f'''
        curso de python do Curso em Vídeo
        142 videos aulas de python
        
        https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0
        ''')

            #java/j
        if S1 == "java":
            print(f'''
        curso de java do Curso em Vídeo
        30 videos aulas de java

        https://www.youtube.com/watch?v=sTX0UEplF54&list=PLHz_AreHm4dkI2ZdjTwZA4mPMxWTfNSpR
        ''')

            #j
        if S1 == "j":
            print(f'''
        curso de java do Curso em Vídeo
        30 videos aulas de java

        https://www.youtube.com/watch?v=sTX0UEplF54&list=PLHz_AreHm4dkI2ZdjTwZA4mPMxWTfNSpR
        ''')

            #javascript/js
        if S1 == "javascript":
            print(f'''
        curso de javascript do Curso em Vídeo
        12 videos aulas de javascript

        https://www.youtube.com/watch?v=Ptbk2af68e8&list=PLeuwJul7tRBfsm7sxnR5_7wG3KvaQ6oOt
        ''')

            #js
        if S1 == "js":
            print(f'''
        curso de javascript do Curso em Vídeo
        12 videos aulas de javascript

        https://www.youtube.com/watch?v=Ptbk2af68e8&list=PLeuwJul7tRBfsm7sxnR5_7wG3KvaQ6oOt
        ''')

            #HTML E CSS/Html e CSS/Html e Css/html e css
        if S1 == "HTML e CSS":
            print(f'''
        curso de HTML e CSS do Curso em Vídeo
        Curso completo e atual de HTML5 e CSS3 - Módulo 1 de 5 
        
        41 Html e css
        https://www.youtube.com/watch?v=Ejkb_YpuHWs&list=PLHz_AreHm4dkZ9-atkcmcBaMZdmLHft8n
        ''')

            #Html e CSS
        if S1 == "Html e CSS":
            print(f'''
        curso de HTML e CSS do Curso em Vídeo
        Curso completo e atual de HTML5 e CSS3 - Módulo 1 de 5 
        
        41 Html e css
        https://www.youtube.com/watch?v=Ejkb_YpuHWs&list=PLHz_AreHm4dkZ9-atkcmcBaMZdmLHft8n
        ''')

            #Html e Css
        if S1 == "Html e Css":
            print(f'''
        curso de HTML e CSS do Curso em Vídeo
        Curso completo e atual de HTML5 e CSS3 - Módulo 1 de 5 
        
        41 Html e css
        https://www.youtube.com/watch?v=Ejkb_YpuHWs&list=PLHz_AreHm4dkZ9-atkcmcBaMZdmLHft8n
        ''')

            #html e css
        if S1 == "html e css":
            print(f'''
        curso de HTML e CSS do Curso em Vídeo
        Curso completo e atual de HTML5 e CSS3 - Módulo 1 de 5 
        
        41 Html e css
        https://www.youtube.com/watch?v=Ejkb_YpuHWs&list=PLHz_AreHm4dkZ9-atkcmcBaMZdmLHft8n
        ''')

            #shell script/shell
            #shell script
        if S1 == "shell script":
            print(f'''
        curso de shell script do Bóson Treinamentos

        30 videos aulas de shell script
        https://www.youtube.com/watch?v=EOLPUc6oo-w&list=PLucm8g_ezqNrYgjXC8_CgbvHbvI7dDfhs
        ''')

            #shell
        if S1 == "shell":
            print(f'''
        curso de shell script do Bóson Treinamentos

        30 videos aulas de shell script
        https://www.youtube.com/watch?v=EOLPUc6oo-w&list=PLucm8g_ezqNrYgjXC8_CgbvHbvI7dDfhs
        ''')

            #C++
        if S1 == "C++":
            print(f'''
        curso de C++ do Marcos Castro
        
        103 videos aulas de C++
        https://www.youtube.com/watch?v=p2RsIed0hnA&list=PL8eBmR3QtPL13Dkn5eEfmG9TmzPpTp0cV
        ''')

            #bash
        if S1 == "bash":
            print(f'''
        curso do debxp
        
        19 videos aulas de bash
        https://www.youtube.com/watch?v=ZM--I3NJ2jY&list=PLXoSGejyuQGpf4X-NdGjvSlEFZhn2f2H7
        ''')

            #css/CSS/Css
            #css
        if S1 == "css":
            print(f'''
        curso de css do CFBCursos
        
        73 videos aulas de css
        https://www.youtube.com/watch?v=GPK8A-A156o&list=PLx4x_zx8csUi47Bnugpk78nqJN6rYvEnV
        ''')

            #CSS
        if S1 == "CSS":
            print(f'''
        curso de css do CFBCursos
        
        73 videos aulas de css
        https://www.youtube.com/watch?v=GPK8A-A156o&list=PLx4x_zx8csUi47Bnugpk78nqJN6rYvEnV
        ''')

            #Css
        if S1 == "Css":
            print(f'''
        curso de css do CFBCursos
        
        73 videos aulas de css
        https://www.youtube.com/watch?v=GPK8A-A156o&list=PLx4x_zx8csUi47Bnugpk78nqJN6rYvEnV
        ''')

            #HTML/Html/html
            #HTML
        if S1 == "HTML":
            print(f'''
        curso de html do CFBCursos
        
        67 videos aulas de html 
        https://www.youtube.com/watch?v=8dPpZsC6Vg8&list=PLx4x_zx8csUgS5ioRmQVBeGHmKBQEyNXQ
        ''')

            #html
        if S1 == "html":
            print(f'''
        curso de html do CFBCursos
        
        67 videos aulas de html 
        https://www.youtube.com/watch?v=8dPpZsC6Vg8&list=PLx4x_zx8csUgS5ioRmQVBeGHmKBQEyNXQ
        ''')

            #Html
        if S1 == "Html":
            print(f'''
        curso de html do CFBCursos
        
        67 videos aulas de html 
        https://www.youtube.com/watch?v=8dPpZsC6Vg8&list=PLx4x_zx8csUgS5ioRmQVBeGHmKBQEyNXQ
        ''')


    elif P1 == "paineArt":
        print("paineArtText")

        print(f'''
isso daqui é como se fosse um google só que ART TEXT
dando uma explicação rápida: desenho em texto
''')
        print(f'''
  ________    _____
 /\/\/\/\/\  | "º  \\
<|\/\/\/\/\|_/ /___/
 |____________/
 |_|_|   /_/_/
''')

        print(f'''
[99] disponível
[0] sair

os animais eu peguei no github do meu colega: sacadsii 
''')

        loop="positivo"
        while loop == "positivo":

            resposta=input("pesquisa o animal: ")

            if resposta == "raposa":
                print(f'''

 ^...^ 
<_* *_> 
  \_/ 
        ''')



            if resposta == "cavalo":
                print(f'''
,~~_
|/\ =_ _ ~
 _( )_( )\~~
 \,\  _|\ \~~~
    \`   \
    `    `


            .''
  ._.-.___.' (`\
 //(        ( `'
'/ )\ ).__. ) 
' <' `\ ._/'\
   `   \     \
        ''')

            if resposta == "aranha magrela":
                print(f'''
                   /\ 
                  /  \ 
                 |  _ \                  _ 
                 | / \ \                / \ 
                 |/   \ \              /   \ 
                 /     \ |        /\  /     \ 
                /|      \| ~  ~  /  \/       \ 
        _______/_|_______\(o)(o)/___/\_____   \ 
       /      /  |       (______)     \    \   \_ 
      /      /   |                     \    \ 
     /      /    |                      \    \ 
    /      /     |                       \    \ 
   /     _/      |                        \    \ 
  /             _|                         \    \_ 
_/                                          \ 
                                             \ 
                                              \_ 
        ''')

            if resposta == "aranhas coletivo":
                print(f'''
                                   _ 
       /      \         __      _\( )/_ 
    \  \  ,,  /  /   | /  \ |    /(O)\  
     '-.`\()/`.-'   \_\\  //_/    _.._   _\(o)/_  //  \\ 
    .--_'(  )'_--.   .'/()\'.   .'    '.  /(_)\  _\\()//_ 
/ /` /`""`\ `\ \ \\ // / __ \ / // \\ \ 
|  |  >< |  |  , |  >< |  , |  \__/ | 
    \  \      /  /         . \  \      /  / .              _ 
   _    '.__.'    _\(O)/_   \_'--`(  )'--'_/     __     _\(_)/_ 
_\( )/_            /(_)\      .--'/()\'--.    | /  \ |   /(O)\ 
 /(O)\  //  \\         _     /  /` '' `\  \  \_\\  //_/ 
       _\\()//_     _\(_)/_    |        |      //()\\  
 jgs  / //  \\ \     /(o)\      \      /       \\  // 
       | \__/ |         
        ''')






            elif resposta == "99":
                print(f'''
    raposa [tem]
    vaca [ainda não]
    panda [ainda não]
    cavalo [tem]
    elefante [ainda não]
    aranha magrela [tem]
    aranhas coletivo [tem]


        ''')



            elif resposta == "0":
                print ("saindo ...")
        
                loop="negativo"

        #tá em beta

    elif P1 == "help-people":
        import os
        os.system('clear') or None

        print(f'''
bem vindo ao: help people in repository
help people in repository vem do inglês, ou seja..
ajudar as pessoas no repositório.

digita 'github' para ver o github do criado

''')

        print(f'''
  ________    _____
 /\/\/\/\/\  | "º  \\
<|\/\/\/\/\|_/ /___/
 |____________/
 |_|_|   /_/_/

''')

        print(f'''
digita ferramentas para ver as que tem
digita 0 para sair
digita clear para limpar

''')

        resposta=input("pesquisa o repositório/ferramenta: ")

    #zphisher
        if resposta == "zphisher":
            print ("git clone https://github.com/htr-tech/zphisher ")
            print(f'''
        Zphisher é uma ferramenta poderosa de código aberto Phishing Tool.
        Tornou-se muito popular hoje em dia que é usado para fazer ataques
        de phishing no Target. Zphisher é mais fácil do que o Kit de ferramentas
        de engenharia social.
        ''')
        
            #zaproxy
        elif resposta == "zaproxy":
            print(f'''
        site para baixar o zaproxy https://www.zaproxy.org/download/

        OWASP ZAP é um scanner de segurança de aplicativos da web de código aberto.
        Ele deve ser usado tanto por aqueles que são novos em segurança de aplicativos
        quanto por testadores de penetração profissionais.
        ''')

            #zaproxy
        elif resposta == "zaprox":
            print(f'''
        site para baixar o zaproxy https://www.zaproxy.org/download/

        OWASP ZAP é um scanner de segurança de aplicativos da web de código aberto.
        Ele deve ser usado tanto por aqueles que são novos em segurança de aplicativos
        quanto por testadores de penetração profissionais.
        ''')

            #zaproxy
        elif resposta == "zap":
            print(f'''
        site para baixar o zaproxy https://www.zaproxy.org/download/

        OWASP ZAP é um scanner de segurança de aplicativos da web de código aberto.
        Ele deve ser usado tanto por aqueles que são novos em segurança de aplicativos
        quanto por testadores de penetração profissionais.
        ''')

            #metasploit
        elif resposta == "metasploit":
            print(f'''
                git clone https://github.com/gushmazuko/metasploit_in_termux
                O Projeto Metasploit é um projeto de segurança de
                computadores que fornece informações sobre vulnerabilidades
                de segurança e ajuda em testes de penetração e desenvolvimento
                de assinaturas IDS. É propriedade da Rapid7, empresa de segurança
                sediada em Boston, Massachusetts.
                ''')

            #social engineering
        elif resposta == "social engineering":
            print(f'''
            git clone https://github.com/trustedsec/social-engineer-toolkit
    O Social Engineering Toolkit é uma ferramenta integrada com o Metasploit
    Framework com o objetivo de facilitar os testes, avaliações e ataques 
    relacionados à engenharia social.
            ''')

            #social engineering
        elif resposta == "engenharia social":
            print(f'''
            git clone git clone https://github.com/trustedsec/social-engineer-toolkit

            O Social Engineering Toolkit é uma ferramenta integrada com o Metasploit
            Framework com o objetivo de facilitar os testes, avaliações e ataques 
            relacionados à engenharia social.
            ''')

        #clear
        elif resposta == "clear":
            import os
            os.system('clear') or None
            print("bem vindo ao: help people in repository")
            print("")
            print("help people in repository vem do inglês, ou seja..")
            print("ajudar as pessoas no repositório")
            print("a ferramenta foi crianda por mim e por um colega")
            print("digita 'github' para ver o github do criador")
            print(f'''
  ________    _____
 /\/\/\/\/\  | "º  \\
<|\/\/\/\/\|_/ /___/
 |____________/
 |_|_|   /_/_/


digita ferramentas para ver as que tem
digita 0 para sair
digita clear para limpar
            ''')

            #ferramentas
        elif resposta == "ferramentas":
            print(f'''
            metasploit
            social engineering
            zaproxy
            zphisher
            são poucas porque a ferramenta tá em beta
            ''')

            #meu github :)
        elif resposta == "github":
            print(f'''
            meu github: https://github.com/UIy2KHDkF6WPXx3k83Df8w
            eu botei meu nome em criptografia pra mim é legal
            ''')

        elif resposta == "0":
            print ("saindo da ferramenta...")
        
            loop="negativo"