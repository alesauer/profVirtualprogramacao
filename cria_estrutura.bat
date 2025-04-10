@echo off

REM Cria os diretórios do projeto
mkdir streamlit_app
mkdir streamlit_app\components
mkdir streamlit_app\services
mkdir config

REM Cria os arquivos __init__.py para tornar os diretórios pacotes
type nul > streamlit_app\__init__.py
type nul > streamlit_app\components\__init__.py
type nul > streamlit_app\services\__init__.py

REM Cria o arquivo main.py com um conteúdo placeholder
echo # main.py placeholder > streamlit_app\main.py

REM Cria o arquivo code_editor.py com um conteúdo placeholder
echo # code_editor.py placeholder > streamlit_app\components\code_editor.py

REM Cria o arquivo supabase_service.py com um conteúdo placeholder
echo # supabase_service.py placeholder > streamlit_app\services\supabase_service.py

REM Cria o arquivo openai_service.py com um conteúdo placeholder
echo # openai_service.py placeholder > streamlit_app\services\openai_service.py

REM Cria o arquivo secrets.toml com um conteúdo placeholder
echo # secrets.toml placeholder > config\secrets.toml

REM Cria o arquivo requirements.txt com dependências iniciais
echo streamlit > requirements.txt
echo openai >> requirements.txt

echo Estrutura do projeto criada com sucesso!
pause
