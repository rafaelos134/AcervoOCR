# AcervoOCR

**OCR de documentos em português para Windows, Linux e macOS.**

Este programa transforma PDFs digitalizados em documentos pesquisáveis. A aparência das páginas continua praticamente igual, mas o programa acrescenta uma camada invisível de texto. Depois do processamento, é possível pesquisar palavras, selecionar trechos e copiar o conteúdo para outros programas.

Todo o reconhecimento é feito no próprio computador. Os documentos não são enviados para serviços externos.

## Uso rápido

1. Coloque um ou vários PDFs na pasta `arquivos`.
2. Abra o AcervoOCR.
3. A conversão começará automaticamente em alta qualidade.
4. Cada resultado será salvo como `nome_ocr.pdf` na mesma pasta.

## O que é OCR?

OCR é a sigla em inglês para **Reconhecimento Óptico de Caracteres**. Essa tecnologia examina a imagem de cada página e tenta identificar letras, palavras, números e sinais de pontuação.

Um PDF produzido por scanner ou câmera normalmente contém apenas fotografias das páginas. Para o computador, cada página é somente uma imagem. Depois do OCR, programas como navegadores e leitores de PDF conseguem localizar e copiar o texto existente nessa imagem.

Este programa:

- reconhece textos em português, incluindo acentos e cedilha;
- cria uma nova cópia pesquisável do PDF, sem alterar o arquivo original;
- corrige pequenas inclinações das páginas;
- identifica páginas que podem estar giradas;
- preserva páginas que já possuem uma camada de texto;
- processa vários PDFs em sequência;
- pode criar também um arquivo de texto simples (`.txt`);
- pode exportar o conteúdo em `.txt` e `.json`, separado por página;
- oferece um modo de alta qualidade para documentos difíceis.

## Utilidade para História e pesquisa documental

Acervos históricos digitalizados frequentemente são disponibilizados como imagens: jornais, revistas, livros, relatórios, processos, correspondências datilografadas, atas e documentos administrativos. Embora a digitalização preserve e facilite o acesso ao documento, uma imagem não permite pesquisar diretamente nomes, lugares, datas ou acontecimentos.

O OCR ajuda a transformar essas digitalizações em fontes mais fáceis de consultar. Por exemplo, um pesquisador pode:

- procurar todas as ocorrências de um sobrenome em um jornal;
- localizar rapidamente datas, cidades, instituições ou cargos;
- copiar trechos para fichamentos, respeitando a citação da fonte original;
- preparar conjuntos de documentos para análise textual;
- melhorar a acessibilidade por meio de leitores de tela;
- reduzir o tempo gasto examinando manualmente centenas de páginas.

O resultado do OCR deve ser entendido como um auxílio à pesquisa, não como uma transcrição definitiva. Fontes antigas, páginas manchadas, tipos desgastados, colunas complexas e grafias históricas podem gerar erros. Informações importantes sempre devem ser conferidas visualmente na página original. Manuscritos e textos cursivos geralmente exigem ferramentas especializadas e não são o foco deste programa.

## Antes de instalar

É necessário ter acesso à internet durante a preparação inicial, pois as bibliotecas e os modelos de português serão baixados. Depois disso, o processamento pode ser realizado sem internet.

Reserve aproximadamente 1 GB de espaço livre. O modo de alta qualidade pode demorar vários minutos em documentos extensos, dependendo do computador e da qualidade das páginas.

## Como baixar o programa pelo GitHub

Não é necessário criar uma conta no GitHub, conhecer programação ou instalar o Git.

1. Abra no navegador a página do projeto AcervoOCR no GitHub.
2. Na página do projeto, localize o botão verde chamado **Code**. Ele fica acima da lista de arquivos.
3. Clique em **Code** e depois em **Download ZIP**.
4. Aguarde o download. O arquivo normalmente será salvo na pasta **Downloads** e terá um nome parecido com `acervo-ocr-main.zip`.
5. O arquivo ZIP é uma pasta compactada. Ele precisa ser extraído antes do uso.

### Extrair no Windows

1. Abra a pasta **Downloads**.
2. Clique com o botão direito em `acervo-ocr-main.zip`.
3. Escolha **Extrair Tudo...**.
4. Clique em **Extrair** e aguarde a nova pasta ser aberta.
5. Entre na pasta extraída. Se houver outra pasta com o mesmo nome dentro dela, abra essa pasta também.
6. Confirme que consegue ver arquivos como `README.md`, `instalar_windows.bat` e a pasta `arquivos`.

Não execute o programa diretamente dentro da janela do ZIP. Os arquivos precisam estar na pasta extraída.

### Extrair no macOS

1. Abra a pasta **Downloads** no Finder.
2. Clique duas vezes em `acervo-ocr-main.zip`.
3. O macOS criará automaticamente uma pasta chamada `acervo-ocr-main`.
4. Abra essa pasta e confirme que nela aparecem `README.md`, `instalar_unix.sh` e a pasta `arquivos`.

### Extrair no Linux

1. Abra a pasta **Downloads** no gerenciador de arquivos.
2. Clique com o botão direito em `acervo-ocr-main.zip`.
3. Escolha **Extrair aqui** ou **Extrair para...**.
4. Abra a pasta extraída e confirme que nela aparecem `README.md`, `instalar_unix.sh` e a pasta `arquivos`.

> O nome do ZIP pode ser um pouco diferente, dependendo do nome do repositório ou da versão baixada. O procedimento é o mesmo.

## Preparação no Windows 10 ou 11

O Windows deve ser de 64 bits.

1. Depois de seguir a seção **Como baixar o programa pelo GitHub**, abra a pasta extraída.
2. Clique duas vezes em `instalar_windows.bat`.
3. O Windows instalará os componentes necessários. Se a janela pedir para ser fechada, abra `instalar_windows.bat` novamente.
4. Aguarde a mensagem `Instalação concluída`.
5. Nas próximas utilizações, abra `abrir_acervo_ocr.bat`.

A preparação instala uma versão isolada do Python, a interface gráfica, o OCRmyPDF, o Tesseract e os modelos de português.

### Como usar no Windows

Clique duas vezes em `abrir_acervo_ocr.bat` para abrir a interface gráfica.

Na janela do AcervoOCR:

1. Arraste um ou vários PDFs para a grande área pontilhada. Se preferir, clique em **Selecionar PDFs**.
2. Confira os documentos apresentados na lista. Arquivos adicionados por engano podem ser removidos.
3. O modo **Alta qualidade** já vem marcado e é o padrão. Desmarque somente se priorizar velocidade.
4. Marque `.txt` para exportar somente texto. Marque `.json` para criar o texto simples e também um arquivo estruturado por página.
5. Clique em **Converter arquivos**.
6. Mantenha o programa aberto até aparecer a mensagem de conclusão.

Como alternativa, coloque os PDFs na pasta `arquivos` antes de abrir o programa. Eles serão carregados e convertidos automaticamente.

O novo documento será salvo na mesma pasta do original. Por exemplo:

```text
documento.pdf  →  documento_ocr.pdf
```

Na próxima execução, um original que já possua resultado atualizado será ignorado. Se o PDF original for alterado posteriormente, ele será convertido novamente.

Documentos grandes podem levar algum tempo. A interface informa qual arquivo está sendo processado e avisa quando tudo estiver concluído.

## Instalação no macOS

O instalador utiliza o Homebrew, um gerenciador de programas para macOS.

1. Baixe e extraia o projeto conforme explicado em **Como baixar o programa pelo GitHub**.
2. Se o Homebrew ainda não estiver instalado, siga as instruções em [brew.sh](https://brew.sh).
3. Abra o aplicativo **Terminal**.
4. Digite `cd`, deixe um espaço e arraste a pasta extraída do programa para dentro do Terminal. Pressione `Enter`. Isso abre a pasta correta no Terminal.
5. Copie e execute os comandos abaixo, um de cada vez:

```sh
chmod +x instalar_unix.sh executar_unix.sh
./instalar_unix.sh
```

6. Aguarde a mensagem `Instalação concluída`.

Para abrir o programa posteriormente, entre novamente na pasta pelo Terminal e execute:

```sh
./executar_unix.sh
```

Se não houver PDFs na pasta `arquivos`, uma janela será aberta para selecionar os documentos. O modo de alta qualidade será usado automaticamente. Se o macOS bloquear a primeira execução, abra **Ajustes do Sistema → Privacidade e Segurança** e autorize o programa.

## Instalação no Linux

O instalador reconhece Ubuntu, Debian, Fedora e distribuições que utilizam Homebrew.

1. Baixe e extraia o projeto conforme explicado em **Como baixar o programa pelo GitHub**.
2. Abra o Terminal na pasta extraída. Em muitos gerenciadores de arquivos, basta clicar com o botão direito dentro da pasta e escolher **Abrir no terminal**.
3. Execute:

```sh
chmod +x instalar_unix.sh executar_unix.sh
./instalar_unix.sh
```

4. Digite sua senha se o sistema solicitar. A senha não aparece na tela enquanto é digitada; isso é normal.
5. Aguarde a mensagem `Instalação concluída`.

Para usar o programa:

```sh
./executar_unix.sh
```

Se o computador não possuir interface gráfica, informe o PDF diretamente:

```sh
./executar_unix.sh documento.pdf
```

## Modo de alta qualidade

O modo de alta qualidade é o padrão. Ele é indicado para documentos históricos, letras pequenas, impressão desgastada ou digitalização de qualidade inferior:

```sh
./executar_unix.sh documento.pdf
```

No Windows, a caixa **Alta qualidade** já aparece marcada.

Esse modo:

- utiliza somente o idioma português para reduzir ambiguidades;
- utiliza o modelo oficial `tessdata_best`, mais preciso e mais pesado;
- analisa as páginas com resolução de 400 DPI;
- utiliza o mecanismo LSTM do Tesseract;
- aplica segmentação automática, correção de inclinação e rotação.

O processamento será mais lento e consumirá mais memória. Para priorizar velocidade no terminal, use `--modo_rapido`:

```sh
./executar_unix.sh documento.pdf --modo_rapido
```

## Outros comandos úteis

Criar o PDF pesquisável com o nome automático:

```sh
./executar_unix.sh documento.pdf
```

Processar vários PDFs de uma vez:

```sh
./executar_unix.sh livro.pdf jornal.pdf relatorio.pdf
```

Cada argumento é sempre considerado um arquivo de entrada. Os resultados serão `livro_ocr.pdf`, `jornal_ocr.pdf` e `relatorio_ocr.pdf`, nas mesmas pastas dos originais. O nome da saída não precisa e não pode ser informado manualmente.

Criar também um arquivo `.txt`:

```sh
./executar_unix.sh documento.pdf --texto
```

Criar simultaneamente um `.txt` e um `.json`:

```sh
./executar_unix.sh documento.pdf --exportar_texto
```

O arquivo JSON mantém os acentos e organiza o resultado desta forma:

```json
{
  "arquivo_pdf": "documento_ocr.pdf",
  "total_paginas": 2,
  "idioma": "português",
  "paginas": [
    {"pagina": 1, "texto": "Texto reconhecido na primeira página..."},
    {"pagina": 2, "texto": "Texto reconhecido na segunda página..."}
  ]
}
```

Esse formato facilita o uso do documento em bancos de dados, planilhas, programas de análise textual e projetos de pesquisa digital.

Refazer o OCR de páginas que já possuem texto:

```sh
./executar_unix.sh documento.pdf --forcar
```

Use `--forcar` apenas quando o texto existente estiver incorreto. Normalmente, o programa preserva páginas que já contêm texto.

No Windows, alta qualidade e exportação TXT/JSON estão disponíveis como caixas de seleção na interface gráfica. A opção avançada `--forcar` permanece disponível no script para Linux e macOS.

## Onde ficam os resultados?

Quando nenhum nome é informado, o resultado é criado ao lado do PDF original com `_ocr` no final do nome:

```text
relatorio.pdf  →  relatorio_ocr.pdf
```

O arquivo original não é apagado ou modificado. Se o arquivo `_ocr.pdf` já existir, ele será substituído pelo novo resultado, mas somente depois que o processamento terminar corretamente. Recomenda-se preservar o PDF original, especialmente quando ele fizer parte de um acervo ou pesquisa histórica.

## Limitações e recomendações

A qualidade depende diretamente da fonte. Para melhores resultados:

- prefira digitalizações com 300 DPI ou mais;
- evite páginas desfocadas, cortadas ou com sombras fortes;
- use o modo de alta qualidade quando o modo comum cometer muitos erros;
- confira nomes próprios, números, datas e citações antes de utilizá-los;
- não considere o texto extraído uma substituição da imagem ou do documento original.

O programa reconhece principalmente textos impressos ou datilografados. Caligrafia cursiva, tabelas muito complexas, fórmulas e páginas com várias orientações podem apresentar resultados limitados.

## Como o programa funciona internamente

O núcleo em Python chama o OCRmyPDF, que prepara cada página e acrescenta a camada pesquisável ao documento. O reconhecimento das letras é realizado pelo Tesseract com modelos específicos para português. A interface do Windows é construída com PySide6.

No modo comum, o programa usa `tessdata_fast`, que equilibra velocidade e precisão. No modo de alta qualidade, usa `tessdata_best`, reamostragem em 400 DPI e o mecanismo LSTM do Tesseract.

Não é preciso ativar manualmente o ambiente: `executar_unix.sh` no Linux/macOS e `abrir_acervo_ocr.bat` no Windows já utilizam o Python correto dentro de `.venv`.

Tecnologias e documentação oficial:

- [OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Instalação do OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/installation.html)
- [Idiomas no OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/languages.html)
- [Modelos oficiais do Tesseract](https://tesseract-ocr.github.io/tessdoc/Data-Files.html)
- [uv](https://docs.astral.sh/uv/)
- [PySide6](https://doc.qt.io/qtforpython-6/)
