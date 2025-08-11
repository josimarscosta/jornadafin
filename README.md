# 🎓 Adm Academy - Análise Financeira Alpha Serviços

## 📊 Versão Aprimorada com Dados Reais

Esta é uma versão aprimorada do aplicativo de análise financeira, desenvolvida especificamente para estudantes de Administração e Ciências Contábeis da Unifor, utilizando dados reais da empresa Alpha Serviços LTDA.

## 🏢 Sobre a Alpha Serviços LTDA

**Empresa Real de Estudo de Caso:**
- **Razão Social:** Alpha Serviços LTDA
- **Segmento:** Comércio e prestação de serviços especializados em manutenção de móveis e eletrodomésticos
- **Porte:** Empresa de Pequeno Porte
- **Situação:** Crescimento no volume de clientes sem controle rigoroso de custos e despesas
- **Desafio:** Sócios com dificuldade para interpretar informações contábeis e financeiras

## 🎯 Funcionalidades Principais

### 📊 **Demonstrações Contábeis Reais**
- **Balanço Patrimonial** completo com dados de 31/03/2025
- **DRE (Demonstração do Resultado do Exercício)** detalhada
- Visualizações interativas com gráficos Plotly
- Dados organizados e formatados profissionalmente

### 📈 **Análise de Indicadores Financeiros**

#### 💧 **Indicadores de Liquidez**
- **Liquidez Corrente:** 1,33
- **Liquidez Geral:** 0,89
- **Capital de Giro:** R$ 20.000,00
- Simulador interativo de cenários
- Interpretações práticas e didáticas

#### 💰 **Indicadores de Rentabilidade**
- **Margem Bruta:** 48,15%
- **Margem Operacional:** 16,30%
- **Margem Líquida:** 11,96%
- Gráficos comparativos
- Decomposição da receita

#### ⚖️ **Estrutura de Capital**
- **Dívida/Patrimônio Líquido:** 1,00
- Análise da composição do financiamento
- Recomendações baseadas nos indicadores

### 🎯 **Análise Integrada**
- Dashboard completo de indicadores
- Radar de performance financeira
- Matriz SWOT financeira
- Recomendações prioritárias por prazo

### 🤖 **Consultoria com IA (Gemini)**
- Assistente especializado em análise financeira
- Perguntas sugeridas contextualizadas
- Respostas técnicas e didáticas
- Histórico de consultorias

## 🎨 **Design e UX Aprimorados**

### **Identidade Visual Unifor**
- Logo da Unifor integrada
- Cores institucionais
- Tipografia profissional (Inter + Poppins)

### **Navegação Otimizada para Alunos**
- Interface intuitiva e responsiva
- Navegação por seções temáticas
- Sidebar com informações resumidas
- Barra de progresso visual

### **Elementos Visuais**
- Cards informativos com hover effects
- Indicadores coloridos por status (verde/amarelo/vermelho)
- Gráficos interativos e profissionais
- Layout responsivo para mobile e desktop

## 🚀 **Instalação e Uso**

### **Pré-requisitos:**
```bash
Python 3.8+
pip
```

### **Instalação Local:**
```bash
# Clone ou extraia o projeto
cd streamlit_app_aprimorado

# Instale dependências
pip install -r requirements.txt

# Configure a chave da API do Gemini (opcional)
# Edite .streamlit/secrets.toml

# Execute o aplicativo
streamlit run app.py
```

### **Deploy no Streamlit Cloud:**
1. Faça upload para GitHub
2. Conecte ao Streamlit Cloud
3. Configure Secrets (se usar IA):
   ```
   GEMINI_API_KEY = "sua_chave_da_api"
   ```
4. Deploy automático

## 📚 **Valor Educacional**

### **Para Estudantes:**
- **Dados Reais:** Experiência com empresa real do mercado
- **Cálculos Práticos:** Fórmulas e interpretações detalhadas
- **Simuladores:** Teste de cenários e "what-if"
- **IA Educacional:** Esclarecimento de dúvidas em tempo real

### **Para Professores:**
- **Ferramenta Pedagógica:** Apoio às aulas de análise financeira
- **Caso Prático:** Empresa real para discussões
- **Metodologia Ativa:** Aprendizagem baseada em problemas
- **Avaliação:** Base para exercícios e provas

### **Competências Desenvolvidas:**
- Interpretação de demonstrações contábeis
- Cálculo e análise de indicadores financeiros
- Tomada de decisão baseada em dados
- Pensamento crítico em finanças empresariais

## 🔧 **Aspectos Técnicos**

### **Tecnologias Utilizadas:**
- **Streamlit:** Framework web para Python
- **Plotly:** Visualizações interativas
- **Pandas/NumPy:** Manipulação de dados
- **Google Gemini AI:** Assistente inteligente

### **Arquitetura:**
- **Modular:** Funções separadas por funcionalidade
- **Responsiva:** Adaptável a diferentes dispositivos
- **Escalável:** Fácil adição de novas funcionalidades
- **Robusta:** Tratamento de erros e fallbacks

### **Performance:**
- **Cache:** Configurações e cálculos otimizados
- **Lazy Loading:** Carregamento sob demanda
- **Responsive Design:** Interface fluida

## 📊 **Dados da Alpha Serviços**

### **Balanço Patrimonial (31/03/2025):**
- **Total do Ativo:** R$ 180.000,00
- **Ativo Circulante:** R$ 80.000,00
- **Ativo não Circulante:** R$ 100.000,00
- **Passivo Circulante:** R$ 60.000,00
- **Passivo não Circulante:** R$ 30.000,00
- **Patrimônio Líquido:** R$ 90.000,00

### **DRE:**
- **Receita Líquida:** R$ 135.000,00
- **Lucro Bruto:** R$ 65.000,00
- **Resultado Operacional:** R$ 22.000,00
- **Lucro Líquido:** R$ 16.150,00

## 🎯 **Casos de Uso**

### **Disciplinas Aplicáveis:**
- Análise das Demonstrações Contábeis
- Administração Financeira
- Contabilidade Gerencial
- Controladoria
- Gestão Empresarial

### **Atividades Sugeridas:**
- Análise individual dos indicadores
- Comparação com benchmarks do setor
- Elaboração de relatórios gerenciais
- Simulação de cenários futuros
- Propostas de melhoria financeira

## 🔄 **Atualizações Futuras**

### **Planejadas:**
- Comparação com dados de mercado
- Análise temporal (múltiplos períodos)
- Novos indicadores financeiros
- Integração com dados reais de APIs
- Módulo de projeções financeiras

### **Melhorias Contínuas:**
- Interface ainda mais intuitiva
- Novos casos de empresas
- Gamificação educacional
- Relatórios exportáveis

## 📞 **Suporte e Contato**

**Desenvolvido para:**
- Universidade de Fortaleza (Unifor)
- Cursos de Administração e Ciências Contábeis

**Metodologia:**
- Adm Academy - Aprendizagem heutagógica
- Metodologias ativas de ensino
- Aprendizagem baseada em projetos reais

---

**🎓 Adm Academy - Transformando Educação Financeira com Dados Reais**

*"Os sonhos de um homem não têm fim!" - Marshall D. Teach*

