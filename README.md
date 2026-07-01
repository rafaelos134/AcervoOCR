# AcervoOCR

**OCR de documentos em português para Windows, Linux e macOS.**

Este programa transforma PDFs digitalizados em documentos pesquisáveis. A aparência das páginas continua praticamente igual, mas o programa acrescenta uma camada invisível de texto. Depois do processamento, é possível pesquisar palavras, selecionar trechos e copiar o conteúdo para outros programas.

Todo o reconhecimento é feito no próprio computador. Os documentos não são enviados para serviços externos.

## Uso rápido no Windows

1. Instale o programa com `AcervoOCR-Instalador-1.0.0.exe`.
2. Abra o atalho **AcervoOCR**.
3. Arraste um ou vários PDFs para a janela.
4. Clique em **Converter arquivos**.
5. Encontre cada resultado na pasta do original com o nome `nome_ocr.pdf`.

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

No Windows, o instalador já contém o programa e todas as dependências; a instalação e o processamento podem ser realizados sem internet depois que o arquivo `.exe` for baixado. No Linux e no macOS, é necessário ter acesso à internet durante a instalação inicial.

Reserve aproximadamente 1 GB de espaço livre. O modo de alta qualidade pode demorar vários minutos em documentos extensos, dependendo do computador e da qualidade das páginas.

## Instalação no Windows 10 ou 11

O Windows deve ser de 64 bits. O usuário não precisa instalar Python, Tesseract, bibliotecas nem utilizar o Prompt de Comando.

1. Baixe o arquivo `AcervoOCR-Instalador-1.0.0.exe` na página de versões do projeto.
2. Clique duas vezes no arquivo baixado.
3. O Windows poderá perguntar se deseja permitir a instalação. Confira o nome **AcervoOCR** e prossiga.
4. Escolha a pasta de instalação ou mantenha a opção sugerida.
5. Deixe marcada a opção para criar um atalho na Área de Trabalho.
6. Clique em **Instalar** e aguarde.
7. Ao final, clique em **Concluir** para abrir o programa.

O instalador é um assistente convencional do Windows. Ele inclui o aplicativo, Python, OCRmyPDF, Tesseract e os modelos de português. O programa também aparecerá em **Configurações → Aplicativos → Aplicativos instalados**, onde poderá ser desinstalado normalmente.

> **Aviso sobre o Windows SmartScreen:** enquanto o instalador não possuir uma assinatura digital comercial, o Windows poderá mostrar a mensagem “O Windows protegeu o computador”. Nesse caso, confirme que o arquivo veio da página oficial do projeto, clique em **Mais informações** e depois em **Executar assim mesmo**. Para distribuição pública ampla, recomenda-se assinar digitalmente o instalador.

### Como usar no Windows

Ao terminar a instalação, será criado o atalho **AcervoOCR** na Área de Trabalho e no Menu Iniciar. Clique duas vezes no atalho para abrir a interface gráfica.

Na janela do AcervoOCR:

1. Arraste um ou vários PDFs para a grande área pontilhada. Se preferir, clique em **Selecionar PDFs**.
2. Confira os documentos apresentados na lista. Arquivos adicionados por engano podem ser removidos.
3. Marque **Alta qualidade** para documentos antigos, desgastados ou com letras pequenas. Essa opção demora mais.
4. Marque `.txt` para exportar somente texto. Marque `.json` para criar o texto simples e também um arquivo estruturado por página.
5. Clique em **Converter arquivos**.
6. Mantenha o programa aberto até aparecer a mensagem de conclusão.

Não é necessário abrir o Prompt de Comando, digitar comandos ou ativar o ambiente Python.

O novo documento será salvo na mesma pasta do original. Por exemplo:

```text
documento.pdf  →  documento_ocr.pdf
```

Documentos grandes podem levar algum tempo. A interface informa qual arquivo está sendo processado e avisa quando tudo estiver concluído.

## Instalação no macOS

O instalador utiliza o Homebrew, um gerenciador de programas para macOS.

1. Se o Homebrew ainda não estiver instalado, siga as instruções em [brew.sh](https://brew.sh).
2. Abra o aplicativo **Terminal**.
3. Digite `cd`, deixe um espaço e arraste a pasta deste programa para dentro do Terminal. Pressione `Enter`. Isso abre a pasta correta no Terminal.
4. Copie e execute os comandos abaixo, um de cada vez:

```sh
chmod +x instalar_unix.sh executar_unix.sh
./instalar_unix.sh
```

5. Aguarde a mensagem `Instalação concluída`.

Para abrir o programa posteriormente, entre novamente na pasta pelo Terminal e execute:

```sh
./executar_unix.sh
```

Uma janela será aberta para selecionar os PDFs. O programa perguntará se deseja usar o modo normal ou o modo de alta qualidade. Se o macOS bloquear a primeira execução, abra **Ajustes do Sistema → Privacidade e Segurança** e autorize o programa.

## Instalação no Linux

O instalador reconhece Ubuntu, Debian, Fedora e distribuições que utilizam Homebrew.

1. Abra o Terminal na pasta deste programa. Em muitos gerenciadores de arquivos, basta clicar com o botão direito dentro da pasta e escolher **Abrir no terminal**.
2. Execute:

```sh
chmod +x instalar_unix.sh executar_unix.sh
./instalar_unix.sh
```

3. Digite sua senha se o sistema solicitar. A senha não aparece na tela enquanto é digitada; isso é normal.
4. Aguarde a mensagem `Instalação concluída`.

Para usar o programa:

```sh
./executar_unix.sh
```

Se o computador não possuir interface gráfica, informe o PDF diretamente:

```sh
./executar_unix.sh documento.pdf
```

## Modo de alta qualidade

O modo comum oferece um bom equilíbrio entre velocidade e precisão. Para documentos com letras pequenas, impressão desgastada ou digitalização de qualidade inferior, use `--qualidade_alta`:

```sh
./executar_unix.sh documento.pdf --qualidade_alta
```

No Windows, basta marcar **Alta qualidade** na interface antes de clicar em **Converter arquivos**.

Esse modo:

- utiliza somente o idioma português para reduzir ambiguidades;
- utiliza o modelo oficial `tessdata_best`, mais preciso e mais pesado;
- analisa as páginas com resolução de 400 DPI;
- utiliza o mecanismo LSTM do Tesseract;
- aplica segmentação automática, correção de inclinação e rotação.

O processamento será mais lento e consumirá mais memória. No Windows, o modelo já está incluído no aplicativo. No Linux e no macOS, ele é baixado automaticamente durante a instalação.

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

No Linux e no macOS, não é preciso ativar manualmente esse ambiente: `executar_unix.sh` já utiliza o Python correto. No Windows, todos os componentes ficam empacotados dentro do aplicativo instalado.

## Gerando o instalador do Windows

Esta seção é destinada somente aos responsáveis por publicar o programa. Usuários comuns devem baixar o instalador pronto.

O instalador precisa ser compilado em Windows. O projeto contém `AcervoOCR.spec` para empacotamento com PyInstaller e `instalador_windows.iss` para criação do assistente com Inno Setup. A automação em `.github/workflows/windows-installer.yml` gera o arquivo `.exe` pelo GitHub Actions.

Para gerar uma nova versão, crie uma tag como `v1.0.0` no GitHub. A automação compilará o programa e anexará o instalador à página da versão. Também é possível iniciar manualmente a ação **Gerar instalador do Windows** e baixar o artefato produzido.

Para compilar diretamente em um computador Windows, instale `uv`, Tesseract 64 bits e Inno Setup 6. Depois, abra o PowerShell na pasta do projeto e execute:

```powershell
.\build_windows.ps1
```

O resultado será criado em:

```text
dist\installer\AcervoOCR-Instalador-1.0.0.exe
```

O instalador final deve ser testado em uma máquina Windows limpa antes da publicação.

Tecnologias e documentação oficial:

- [OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/)
- [Instalação do OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/installation.html)
- [Idiomas no OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/languages.html)
- [Modelos oficiais do Tesseract](https://tesseract-ocr.github.io/tessdoc/Data-Files.html)
- [uv](https://docs.astral.sh/uv/)
- [PySide6](https://doc.qt.io/qtforpython-6/)
- [PyInstaller](https://pyinstaller.org/)
- [Inno Setup](https://jrsoftware.org/isinfo.php)
