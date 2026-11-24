# Fundamentos de Segurança da Informação

## 1. O que é Segurança da Informação?

Segurança da Informação é a área responsável por proteger dados, sistemas, redes e aplicações contra acessos não autorizados, alterações indevidas, vazamentos e interrupções.

Seu objetivo é preservar a confidencialidade, integridade e disponibilidade das informações.

## 2. Tríade CIA

A tríade CIA representa três princípios fundamentais:

### Confidencialidade (Confidentiality)
Garante que somente pessoas autorizadas tenham acesso às informações.

Exemplo: proteger uma conta com senha forte e autenticação multifator.

### Integridade (Integrity)
Garante que os dados não sejam alterados de maneira indevida.

Exemplo: utilizar mecanismos de verificação para identificar alterações em arquivos.

### Disponibilidade (Availability)
Garante que sistemas e informações estejam acessíveis quando necessário.

Exemplo: manter backups e mecanismos de recuperação para evitar perda de dados.

## 3. Vulnerabilidade, ameaça e risco

### Vulnerabilidade
É uma falha ou fraqueza em um sistema, aplicação, rede ou processo que pode ser explorada.

Exemplo: uma aplicação que utiliza consultas SQL sem parâmetros pode estar vulnerável a SQL Injection.

### Ameaça
É uma situação, agente ou evento capaz de explorar uma vulnerabilidade e causar danos.

Exemplo: um invasor tentando acessar dados de um banco de dados.

### Risco
É a possibilidade de uma ameaça explorar uma vulnerabilidade e causar impacto.

A avaliação de risco considera a probabilidade de ocorrência e a gravidade das consequências.

## 4. Classificação de severidade

O agente deve utilizar as seguintes classificações:

- Baixo: impacto limitado e baixa probabilidade.
- Médio: impacto moderado ou possibilidade relevante de exploração.
- Alto: impacto significativo ou facilidade de exploração.
- Crítico: possibilidade de comprometimento grave de sistemas, dados ou serviços.

A classificação deve ser justificada com base nas evidências. Quando possível, utilizar referências como CVSS.

## 5. Boas práticas de segurança

- Utilizar senhas fortes e únicas.
- Ativar autenticação multifator.
- Manter sistemas e aplicações atualizados.
- Aplicar o princípio do menor privilégio.
- Realizar backups periódicos.
- Utilizar criptografia para proteger informações sensíveis.
- Monitorar registros e atividades suspeitas.
- Validar entradas recebidas por aplicações.
- Utilizar consultas parametrizadas para evitar SQL Injection.
- Restringir serviços e portas desnecessários.

## 6. Referências de segurança

O agente pode utilizar estas referências para aprofundar suas análises:

- OWASP: boas práticas e riscos de segurança em aplicações.
- MITRE ATT&CK: conhecimento sobre táticas e técnicas utilizadas em ataques.
- CWE: catálogo de tipos comuns de fraquezas em software.
- CVE: identificadores públicos de vulnerabilidades conhecidas.
- NIST: publicações e orientações de segurança da informação.
- CVSS: sistema de avaliação da severidade de vulnerabilidades.

O agente não deve inventar referências, identificadores ou classificações.

## 7. Ética e autorização

Toda atividade de análise de segurança deve respeitar a legislação, a privacidade e a autorização do responsável pelo ambiente.

Antes de sugerir testes, o agente deve compreender:

- Qual ambiente será analisado?
- Qual é o objetivo da atividade?
- Existe autorização para realizar os testes?
- Qual é o escopo permitido?

Priorizar laboratórios próprios, ambientes de treinamento e sistemas com autorização explícita.

O objetivo da cibersegurança é identificar riscos, proteger informações e corrigir falhas, não causar danos.