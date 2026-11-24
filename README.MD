# DIO Agent — Mentor de Cibersegurança

Projeto desenvolvido como desafio prático da DIO, com o objetivo de personalizar o DIO Agent para atuar como um mentor de cibersegurança, auxiliando nos estudos, na análise de vulnerabilidades e na adoção de boas práticas de segurança.

## 🎯 Objetivo do projeto

Especializar o agente para atuar como um mentor de segurança da informação, capaz de:

- Identificar e explicar vulnerabilidades.
- Apresentar recomendações de correção segura.
- Ensinar conceitos fundamentais de cibersegurança.
- Orientar análises de segurança de forma didática.
- Verificar autorização e escopo antes de orientar atividades práticas.

## 📁 Estrutura do projeto

```text
dio-agent/
├── AGENTS.md
├── skills/
│   └── vulnerability-analysis/
│       ├── SKILL.md
│       └── README.md
└── agent/
    ├── app.py
    ├── test_sqli.py
    ├── persona.md
    └── knowledge/
        └── security-basics.md
```

## 🧠 Personalização do agente

### 1. Skill — vulnerability-analysis

Foi criada uma skill especializada em análise de vulnerabilidades, com orientações para identificar falhas, explicar seus riscos e recomendar correções.

Arquivos:
- `SKILL.md`: instruções e definição da skill.
- `README.md`: documentação da finalidade da skill.

### 2. Base de conhecimento

Arquivo: `agent/knowledge/security-basics.md`

Contém conceitos fundamentais de segurança da informação, incluindo:

- Vulnerabilidades, ameaças e riscos.
- Tríade CIA: confidencialidade, integridade e disponibilidade.
- Boas práticas de segurança.

### 3. Persona do agente

Arquivo: `agent/persona.md`

Define a identidade do agente como mentor de tecnologia e cibersegurança, com comunicação didática, orientação responsável e foco no aprendizado.

### 4. Instruções gerais

Arquivo: `AGENTS.md`

Contém as instruções gerais do agente e a relação das skills disponíveis, incluindo `vulnerability-analysis`.

## 🔐 Projeto prático — SQL Injection

Durante o desafio, foi utilizado um exemplo de autenticação em Python com SQLite para estudar a vulnerabilidade SQL Injection.

O código inicial utilizava interpolação direta de valores recebidos do usuário na consulta SQL. Essa prática pode permitir que uma entrada maliciosa altere a estrutura da consulta.

A correção utiliza consultas parametrizadas:

```python
cursor.execute(
    """
    SELECT 1
    FROM usuarios
    WHERE username = ? AND password = ?
    LIMIT 1
    """,
    (usuario, senha),
)
```

Os parâmetros são enviados separadamente da instrução SQL, ajudando a impedir que entradas sejam interpretadas como parte do comando.

**Referência técnica:**
- CWE-89 — Improper Neutralization of Special Elements used in an SQL Command.
- MITRE ATT&CK T1190 — Exploit Public-Facing Application, quando aplicável ao contexto de uma aplicação exposta.

## 🧪 Testes com SQLite

Foi criado o arquivo `agent/test_sqli.py` para testar a autenticação utilizando um banco SQLite temporário em memória (`:memory:`).

Resultados observados:

```text
Teste 1: True
Teste 2: False
Teste 3: False
Teste 4: False
```

Os testes demonstram que a consulta parametrizada do exemplo aceita as credenciais corretas e rejeita as entradas incorretas utilizadas no teste.

Para executar:

```bash
python agent/test_sqli.py
```

## 🤖 Execução do agente

O projeto utiliza o Hermes Agent como ambiente para executar e testar o agente personalizado.

Fluxo geral:

1. Abrir o terminal na pasta do projeto.
2. Iniciar o Hermes conforme a configuração instalada.
3. Interagir com o agente pelo terminal.
4. Solicitar análises de segurança em arquivos e exemplos próprios.
5. Avaliar as respostas e recomendações da skill especializada.

Os comandos de inicialização podem variar conforme a instalação e a versão do Hermes.


## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram praticados:

- Fundamentos de Python.
- Utilização do SQLite.
- Identificação e prevenção de SQL Injection.
- Consultas SQL parametrizadas.
- Organização de skills e bases de conhecimento.
- Personalização de agentes de inteligência artificial.
- Análise de vulnerabilidades e boas práticas de AppSec.

## 👨‍💻 Sobre o desafio

Este projeto faz parte do desafio prático da DIO, com a proposta de transformar o DIO Agent em um mentor especializado em cibersegurança.

**Desenvolvido por Adriano José da Costa.**