
# Sobre
O Multiple-PDF-Chat é uma aplicação interativa desenvolvida em Python que permite aos usuários interagir com o conteúdo de múltiplos documentos PDF por meio de um chatbot. Utilizando tecnologias modernas de processamento de linguagem natural e aprendizado de máquina, o projeto transforma textos estáticos de PDFs em uma experiência de conversação dinâmica, possibilitando que os usuários façam perguntas e recebam respostas contextualizadas com base nos documentos carregados.

# Funcionalidades Principais
Leitura de PDFs: O projeto utiliza a biblioteca PyPDF2 para extrair texto de documentos PDF. O conteúdo é coletado de todas as páginas e preparado para análise.

## Divisão de Texto em Blocos: 
O texto extraído é segmentado em partes menores utilizando o CharacterTextSplitter, o que facilita a recuperação de informações específicas e melhora a performance do chatbot.

## Armazenamento Vetorial: 

Com o uso de embeddings de modelos como HuggingFaceEmbeddings, os blocos de texto são convertidos em vetores, permitindo uma busca eficiente e precisa de informações relevantes.

Chatbot Interativo: Integrado com langchain, o chatbot utiliza um modelo de linguagem como o Flan-T5 da Hugging Face para responder perguntas e manter um histórico de conversas, proporcionando interações mais ricas e contextualizadas.

# Tecnologias Utilizadas
- Python: A linguagem principal do projeto.
- Streamlit: Para a criação da interface de usuário interativa.
- PyPDF2: Para leitura e extração de texto dos PDFs.
- Langchain: Para processamento de linguagem natural e gerenciamento de interações conversacionais.
- Hugging Face: Para embeddings e modelo de linguagem.

# Como Usar
- Instalação: Clone o repositório e instale as dependências necessárias utilizando pip.
- Carregar PDFs: Utilize a interface para fazer upload dos documentos PDF que deseja processar.
- Processar Documentos: Clique no botão "Processar" para extrair e preparar o conteúdo dos PDFs.
- Interagir com o Chatbot: Digite suas perguntas na caixa de texto e receba respostas baseadas no conteúdo dos documentos.

# Contribuição
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias. A colaboração é fundamental para aprimorar a funcionalidade e a usabilidade deste projeto.

# Licença
Este projeto é licenciado sob a MIT License. Consulte o arquivo LICENSE para mais informações.