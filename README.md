# 🐍 Python Challenge Generator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

Sistema para geração de desafios de Python personalizados via IA (OpenAI), permitindo que usuários resolvam e recebam feedback automatizado.

## 📋 Pré-requisitos

- Python 3.8+
- Conta na [OpenAI](https://platform.openai.com/) para API Key
- (Opcional) Conta no [Supabase](https://supabase.com/) para persistência

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd profVirtualprogramacao
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o arquivo `config/secrets.toml`:
```toml
# Chave da OpenAI (obrigatória)
openai_key = "sua-chave-openai-aqui"

# Configurações do Supabase (opcional)
supabase_url = "sua-url-supabase"
supabase_key = "sua-chave-supabase"
```

## 🚀 Executando a Aplicação

```bash
streamlit run streamlit_app/main.py
```

## 🏗️ Arquitetura do Projeto

```
profVirtualprogramacao/
├── cria_estrutura.bat       # Script para setup inicial
├── requirements.txt         # Dependências Python
├── config/
│   └── secrets.toml         # Configurações sensíveis
└── streamlit_app/           # Aplicação principal
    ├── main.py              # Ponto de entrada
    ├── components/          # Componentes UI
    │   └── code_editor.py   # Editor de código
    └── services/            # Integrações
        ├── openai_service.py # Serviço da OpenAI
        └── supabase_service.py # Banco de dados
```

## 🔄 Fluxo da Aplicação

1. O sistema busca tópicos da ementa (atualmente mockados)
2. Ao clicar em "Me Desafie":
   - Seleciona um tópico aleatório
   - Usa a API da OpenAI para gerar um desafio
   - Exibe o desafio para o usuário
3. O usuário pode:
   - Resolver no editor integrado
   - Solicitar correção automática
   - Receber feedback da IA

## 📚 Tópicos Disponíveis

- Variáveis e Tipos
- Estruturas Condicionais
- Funções
- Laços de Repetição
- Listas e Dicionários

## 🛠️ Melhorias Planejadas

- [ ] Implementar conexão real com Supabase
- [ ] Adicionar sistema de pontuação
- [ ] Permitir compartilhamento de soluções
- [ ] Expandir tipos de desafios
- [ ] Adicionar suporte a Gemini

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch com sua feature (`git checkout -b feature/fooBar`)
3. Commit suas mudanças (`git commit -am 'Add some fooBar'`)
4. Push para a branch (`git push origin feature/fooBar`)
5. Abra um Pull Request
