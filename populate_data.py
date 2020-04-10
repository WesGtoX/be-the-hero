import requests
import json
import random
import pprint
import time

pp = pprint.PrettyPrinter(indent=2, width=160)


def load_data():
    data = [
      {
        "title": "Internet no Oceano",
        "description": "A internet não é facilmente acessível em muitas áreas do mundo, como os oceanos da Terra.",
        "value": 35
      },
      {
        "title": "Água Subindo",
        "description": "O nível do mar está subindo ao redor do mundo e aproximadamente 40% da população humana vive em zonas costeiras.",
        "value": 864
      },
      {
        "title": "Limpeza de Lixo",
        "description": "Manchas de lixo oceânicas são coleções de detritos marinhos que se juntam devido às correntes oceânicas; eles têm efeitos devastadores nos ecossistemas oceânicos.",
        "value": 249
      },
      {
        "title": "Limpe-se",
        "description": "As missões da Apollo nos mostraram que o pó lunar não apenas se agarrava a tudo e era impossível removê-lo completamente.",
        "value": 963
      },
      {
        "title": "Uni, duni, duni tê, Amostra!",
        "description": "Você é o líder da missão astronauta / robótica encarregada de trazer espécimes valiosos da Lua de volta à Terra para um estudo mais aprofundado.",
        "value": 132
      },
      {
        "title": "O lado artístico da lua",
        "description": "Cinqüenta anos atrás, gerações foram inspiradas quando os humanos deram um salto gigante e caminharam na lua.",
        "value": 353
      },
      {
        "title": "Construa um planeta",
        "description": "Seu desafio é criar um jogo que permita aos jogadores personalizar as características de uma estrela e projetar planetas que possam existir razoavelmente nesse sistema estelar.",
        "value": 912
      },
      {
        "title": "Fora deste mundo!",
        "description": "Crie um aplicativo para pilotar um sistema aéreo não tripulado (UAS), como um drone espacial da NASA, utilizando o sensor giroscópio de 6 eixos em um smartphone ou tablet.",
        "value": 389
      },
      {
        "title": "O criador de memória",
        "description": "A eletrônica tradicional não funciona bem em Vênus, e a memória é um dos maiores desafios.",
        "value": 659
      },
      {
        "title": "Caçadores dos Dados Perdidos",
        "description": "Ajude a encontrar maneiras de melhorar o desempenho do aprendizado de máquina e dos modelos preditivos, preenchendo as lacunas nos conjuntos de dados antes do treinamento do modelo.",
        "value": 253
      },
      {
        "title": "Voar-por-Wireless",
        "description": "Começando com o design ou conceito de uma aeronave ou espaçonave atual, seu desafio é projetar o design da primeira aeronave ou espaçonave sem fios, conectores ou penetrações!",
        "value": 305
      },
      {
        "title": "Sucata Orbital",
        "description": "Porcas, parafusos, palcos gastos de foguetes e pedaços de satélites que orbitam a Terra são apenas alguns dos muitos milhares de itens conhecidos como detritos orbitais ou lixo espacial.",
        "value": 792
      },
      {
        "title": "O espaço trans-netuniano",
        "description": "Assim como a Ferrovia Transiberiana ligou partes remotas da Ásia ao Ocidente, a Via Espacial Trans-Neptuniana (TNS) leva turistas e empreendedores à nova região acessível do nosso sistema solar, além de Netuno.",
        "value": 533
      },
      {
        "title": "Para cima, para fora e para longe!",
        "description": "Permita que o usuário siga Webb em sua jornada desde o lançamento até seu destino final em órbita a um milhão de quilômetros da Terra!",
        "value": 566
      },
      {
        "title": "1UP para NASA Earth",
        "description": "Crie um novo videogame que use os dados da NASA Earth, oferecendo aos jogadores uma nova maneira de interagir e se divertir com os dados da NASA Earth.",
        "value": 781
      },
      {
        "title": "Ascensão à resiliência!",
        "description": "Você é um recém-nomeado Engenheiro Verde Regional.",
        "value": 923
      },
      {
        "title": "Das mentes curiosas vêm ajudar as mãos",
        "description": "Projete e construa uma plataforma inovadora para integrar dados e informações de satélite sobre populações vulneráveis ​​e riscos ambientais, a fim de identificar as populações em maior risco.",
        "value": 584
      },
      {
        "title": "Defina suas vistas altas!",
        "description": "A NASA constrói e opera inúmeras missões aéreas e por satélite que fornecem medições e dados críticos para a comunidade científica do mundo.",
        "value": 774
      },
      {
        "title": "Mostre ao mundo os dados!",
        "description": "As fontes de dados abertas da NASA contêm uma abundância de imagens.",
        "value": 510
      },
      {
        "title": "Esmague seus ODS!",
        "description": "Desenvolva soluções criativas que usam as observações da Terra para atender aos Objetivos de Desenvolvimento Sustentável das Nações Unidas e promover o desenvolvimento sustentável em todo o mundo.",
        "value": 752
      },
      {
        "title": "Encontre o local do fogo V2.0",
        "description": "Crie um aplicativo que aproveite os conjuntos de dados de incêndio florestal em tempo quase real e arquivados da NASA, juntamente com outras ferramentas para apoiar os esforços de combate a incêndios e mitigação de incêndios.",
        "value": 22
      },
      {
        "title": "Missão Superfície-a-Ar (Qualidade)",
        "description": "Integre dados da NASA, dados de qualidade do ar baseados em terra e dados da ciência do cidadão para criar uma superfície de qualidade do ar que exibe os dados mais precisos para um local e hora.",
        "value": 863
      },
      {
        "title": "Florescer ou não florescer",
        "description": "Resolva o mistério por trás das flores de algas!",
        "value": 789
      },
      {
        "title": "Planeta Aquecimento, Idéias Legais",
        "description": "Examine o espaço existente e os projetos e sistemas da Terra e adapte-os a tecnologias específicas que ajudam a estabilizar ou melhorar o clima da Terra e / ou eliminar processos que causam o aquecimento global.",
        "value": 715
      },
      {
        "title": "Onde as coisas altas são encontradas",
        "description": "Explore os tipos de superfícies planetárias em todo o mundo e projete novos produtos de dados para tipos de terreno além das camadas de gelo, gelo marinho, terra, oceano e elevação da água interior.",
        "value": 659
      }
    ]
    return data


def populate_data(url=None, payload=None, querystring=None, token=None):
    payload = json.dumps(payload)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    response = requests.request('POST', url, data=payload, headers=headers, params=querystring)
    print('OK ==>', response.text)


if __name__ == '__main__':
    # _url = 'http://localhost:3333/incidents'
    _url = 'https://be-the-hero-wes.herokuapp.com/incidents'

    token_list = [
        '',
        '',
        '',
    ]

    data_list = load_data()

    for data in data_list:
        auth_token = random.choice(token_list)
        populate_data(url=_url, payload=data, querystring=None, token=auth_token)
        time.sleep(5)
