import streamlit as st
import time
import os
from typing import Dict, Any, Optional
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Adm Academy - Análise Financeira Alpha Serviços",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Importações condicionais para evitar erros
try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Configuração do Gemini AI
def configure_gemini():
    """Configura a API do Gemini"""
    try:
        api_key = None
        if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
            api_key = st.secrets['GEMINI_API_KEY']
        elif 'GEMINI_API_KEY' in os.environ:
            api_key = os.environ['GEMINI_API_KEY']
        elif 'gemini_api_key' in st.session_state:
            api_key = st.session_state.gemini_api_key
        
        if api_key and GEMINI_AVAILABLE:
            genai.configure(api_key=api_key)
            return True
        return False
    except Exception as e:
        return False

def get_gemini_response(prompt: str, context: str = "") -> Optional[str]:
    """Obtém resposta do Gemini AI"""
    try:
        if not GEMINI_AVAILABLE or not configure_gemini():
            return "IA não disponível. Configure a chave da API do Gemini para usar esta funcionalidade."
        
        model = genai.GenerativeModel('gemini-pro')
        system_prompt = f"""
        Você é um consultor financeiro especializado em análise de demonstrações contábeis.
        Contexto: Análise da empresa Alpha Serviços LTDA - {context}
        
        Diretrizes:
        - Use linguagem técnica mas didática
        - Forneça interpretações práticas dos indicadores
        - Relacione com a situação real da empresa
        - Sugira ações de melhoria quando relevante
        - Seja conciso mas informativo
        
        Pergunta: {prompt}
        """
        
        response = model.generate_content(system_prompt)
        return response.text
    except Exception as e:
        return f"Erro ao consultar IA: {str(e)}"

# CSS customizado aprimorado
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&display=swap');
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E40AF;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .company-card {
        background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%);
        border-radius: 1rem;
        padding: 2rem;
        margin: 2rem 0;
        color: white;
        box-shadow: 0 10px 25px rgba(30, 64, 175, 0.2);
    }
    
    .company-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .company-info {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        line-height: 1.6;
        text-align: center;
        opacity: 0.9;
    }
    
    .metric-card {
        background: white;
        border: 2px solid #E2E8F0;
        border-radius: 0.75rem;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #3B82F6;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
        transform: translateY(-2px);
    }
    
    .metric-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #3B82F6;
        margin-bottom: 0.5rem;
    }
    
    .metric-interpretation {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: #64748B;
        line-height: 1.4;
    }
    
    .status-good {
        color: #059669 !important;
    }
    
    .status-warning {
        color: #D97706 !important;
    }
    
    .status-danger {
        color: #DC2626 !important;
    }
    
    .navigation-card {
        background: linear-gradient(135deg, #F8FAFC 0%, #E2E8F0 100%);
        border: 2px solid #CBD5E1;
        border-radius: 1rem;
        padding: 1.5rem;
        margin: 1rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .navigation-card:hover {
        border-color: #3B82F6;
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
    }
    
    .nav-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    
    .nav-description {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #64748B;
        line-height: 1.5;
    }
    
    .ai-chat-container {
        background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
        border: 2px solid #0EA5E9;
        border-radius: 1rem;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .ai-response {
        background: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3B82F6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .data-table {
        font-family: 'Inter', sans-serif;
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }
    
    .data-table th, .data-table td {
        border: 1px solid #E2E8F0;
        padding: 0.75rem;
        text-align: left;
    }
    
    .data-table th {
        background-color: #F8FAFC;
        font-weight: 600;
        color: #1E293B;
    }
    
    .unifor-logo {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 2rem;
    }
    
    .progress-indicator {
        background: linear-gradient(90deg, #3B82F6 0%, #1E40AF 100%);
        height: 4px;
        border-radius: 2px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Dados reais da Alpha Serviços LTDA
ALPHA_DATA = {
    "company_info": {
        "name": "Alpha Serviços LTDA",
        "segment": "Comércio e prestação de serviços especializados em manutenção de móveis e eletrodomésticos",
        "size": "Empresa de Pequeno Porte",
        "challenge": "Crescimento no volume de clientes sem controle rigoroso de custos e despesas"
    },
    "balance_sheet": {
        "ativo_circulante": 80000,
        "ativo_nao_circulante": 100000,
        "total_ativo": 180000,
        "passivo_circulante": 60000,
        "passivo_nao_circulante": 30000,
        "patrimonio_liquido": 90000,
        "total_passivo": 180000
    },
    "income_statement": {
        "receita_bruta": 150000,
        "deducoes": 15000,
        "receita_liquida": 135000,
        "custo_mercadorias": 70000,
        "lucro_bruto": 65000,
        "despesas_vendas": 20000,
        "despesas_administrativas": 18000,
        "depreciacao": 5000,
        "resultado_operacional": 22000,
        "receitas_financeiras": 1000,
        "despesas_financeiras": 4000,
        "resultado_antes_ir": 19000,
        "ir_csll": 2850,
        "lucro_liquido": 16150
    }
}

# Cálculo dos indicadores
def calculate_indicators():
    """Calcula todos os indicadores financeiros"""
    bs = ALPHA_DATA["balance_sheet"]
    is_ = ALPHA_DATA["income_statement"]
    
    indicators = {
        "liquidez_corrente": {
            "value": bs["ativo_circulante"] / bs["passivo_circulante"],
            "formula": "Ativo Circulante / Passivo Circulante",
            "calculation": f"R$ {bs['ativo_circulante']:,.0f} / R$ {bs['passivo_circulante']:,.0f}",
            "interpretation": "Para cada R$ 1,00 de dívida de curto prazo, a empresa possui R$ {:.2f} de recursos de curto prazo"
        },
        "liquidez_geral": {
            "value": bs["ativo_circulante"] / (bs["passivo_circulante"] + bs["passivo_nao_circulante"]),
            "formula": "Ativo Circulante / (Passivo Circulante + Passivo não Circulante)",
            "calculation": f"R$ {bs['ativo_circulante']:,.0f} / (R$ {bs['passivo_circulante']:,.0f} + R$ {bs['passivo_nao_circulante']:,.0f})",
            "interpretation": "Para cada R$ 1,00 de dívida total, a empresa possui R$ {:.2f} de recursos"
        },
        "capital_giro": {
            "value": bs["ativo_circulante"] - bs["passivo_circulante"],
            "formula": "Ativo Circulante - Passivo Circulante",
            "calculation": f"R$ {bs['ativo_circulante']:,.0f} - R$ {bs['passivo_circulante']:,.0f}",
            "interpretation": "A empresa possui R$ {:.0f} de recursos próprios para financiar suas operações"
        },
        "margem_bruta": {
            "value": (is_["lucro_bruto"] / is_["receita_liquida"]) * 100,
            "formula": "(Lucro Bruto / Receita Líquida) × 100",
            "calculation": f"(R$ {is_['lucro_bruto']:,.0f} / R$ {is_['receita_liquida']:,.0f}) × 100",
            "interpretation": "{:.2f}% da receita líquida se transforma em lucro bruto"
        },
        "margem_operacional": {
            "value": (is_["resultado_operacional"] / is_["receita_liquida"]) * 100,
            "formula": "(Resultado Operacional / Receita Líquida) × 100",
            "calculation": f"(R$ {is_['resultado_operacional']:,.0f} / R$ {is_['receita_liquida']:,.0f}) × 100",
            "interpretation": "{:.2f}% da receita líquida se transforma em resultado operacional"
        },
        "margem_liquida": {
            "value": (is_["lucro_liquido"] / is_["receita_liquida"]) * 100,
            "formula": "(Lucro Líquido / Receita Líquida) × 100",
            "calculation": f"(R$ {is_['lucro_liquido']:,.0f} / R$ {is_['receita_liquida']:,.0f}) × 100",
            "interpretation": "{:.2f}% da receita líquida se transforma em lucro líquido"
        },
        "divida_patrimonio": {
            "value": (bs["passivo_circulante"] + bs["passivo_nao_circulante"]) / bs["patrimonio_liquido"],
            "formula": "(Passivo Circulante + Passivo não Circulante) / Patrimônio Líquido",
            "calculation": f"(R$ {bs['passivo_circulante']:,.0f} + R$ {bs['passivo_nao_circulante']:,.0f}) / R$ {bs['patrimonio_liquido']:,.0f}",
            "interpretation": "Para cada R$ 1,00 de patrimônio líquido, a empresa possui R$ {:.2f} de dívidas"
        }
    }
    
    # Formatar interpretações com valores
    for key, indicator in indicators.items():
        if "{" in indicator["interpretation"]:
            if key == "capital_giro":
                indicator["interpretation"] = indicator["interpretation"].format(indicator["value"])
            else:
                indicator["interpretation"] = indicator["interpretation"].format(indicator["value"])
    
    return indicators

def get_status_class(indicator_name, value):
    """Retorna a classe CSS baseada no status do indicador"""
    if indicator_name == "liquidez_corrente":
        if value >= 1.5:
            return "status-good"
        elif value >= 1.0:
            return "status-warning"
        else:
            return "status-danger"
    elif indicator_name == "liquidez_geral":
        if value >= 1.0:
            return "status-good"
        elif value >= 0.8:
            return "status-warning"
        else:
            return "status-danger"
    elif indicator_name == "capital_giro":
        if value > 0:
            return "status-good"
        else:
            return "status-danger"
    elif indicator_name in ["margem_bruta", "margem_operacional", "margem_liquida"]:
        if value >= 20:
            return "status-good"
        elif value >= 10:
            return "status-warning"
        else:
            return "status-danger"
    elif indicator_name == "divida_patrimonio":
        if value <= 0.5:
            return "status-good"
        elif value <= 1.0:
            return "status-warning"
        else:
            return "status-danger"
    
    return ""

# Inicialização do estado da sessão
def init_session_state():
    """Inicializa o estado da sessão"""
    if 'current_section' not in st.session_state:
        st.session_state.current_section = 'home'
    if 'ai_chat_history' not in st.session_state:
        st.session_state.ai_chat_history = []

def show_company_overview():
    """Exibe visão geral da empresa"""
    info = ALPHA_DATA["company_info"]
    
    st.markdown(f"""
    <div class="company-card">
        <h2 class="company-title">📊 {info["name"]}</h2>
        <div class="company-info">
            <p><strong>Segmento:</strong> {info["segment"]}</p>
            <p><strong>Porte:</strong> {info["size"]}</p>
            <p><strong>Desafio:</strong> {info["challenge"]}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_navigation():
    """Exibe menu de navegação"""
    st.markdown("## 🧭 Navegação da Análise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Demonstrações Contábeis", use_container_width=True):
            st.session_state.current_section = 'statements'
            st.rerun()
        
        if st.button("📈 Indicadores de Liquidez", use_container_width=True):
            st.session_state.current_section = 'liquidity'
            st.rerun()
        
        if st.button("💰 Indicadores de Rentabilidade", use_container_width=True):
            st.session_state.current_section = 'profitability'
            st.rerun()
    
    with col2:
        if st.button("⚖️ Estrutura de Capital", use_container_width=True):
            st.session_state.current_section = 'capital_structure'
            st.rerun()
        
        if st.button("🎯 Análise Integrada", use_container_width=True):
            st.session_state.current_section = 'integrated_analysis'
            st.rerun()
        
        if st.button("🤖 Consultoria IA", use_container_width=True):
            st.session_state.current_section = 'ai_consultant'
            st.rerun()

def show_statements():
    """Exibe as demonstrações contábeis"""
    st.markdown("## 📊 Demonstrações Contábeis")
    
    tab1, tab2 = st.tabs(["🏛️ Balanço Patrimonial", "📈 DRE"])
    
    with tab1:
        st.markdown("### Balanço Patrimonial - Alpha Serviços LTDA")
        
        bs = ALPHA_DATA["balance_sheet"]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### ATIVO")
            st.markdown(f"""
            **Ativo Circulante:** R$ {bs['ativo_circulante']:,.2f}
            - Disponibilidades: R$ 25.000,00
            - Clientes: R$ 40.000,00
            - Estoques: R$ 15.000,00
            
            **Ativo não Circulante:** R$ {bs['ativo_nao_circulante']:,.2f}
            - Imobilizado: R$ 100.000,00
            
            **TOTAL DO ATIVO:** R$ {bs['total_ativo']:,.2f}
            """)
        
        with col2:
            st.markdown("#### PASSIVO + PL")
            st.markdown(f"""
            **Passivo Circulante:** R$ {bs['passivo_circulante']:,.2f}
            - Fornecedores: R$ 35.000,00
            - Obrigações Trabalhistas: R$ 10.000,00
            - Empréstimos CP: R$ 15.000,00
            
            **Passivo não Circulante:** R$ {bs['passivo_nao_circulante']:,.2f}
            - Empréstimos LP: R$ 30.000,00
            
            **Patrimônio Líquido:** R$ {bs['patrimonio_liquido']:,.2f}
            - Capital Social: R$ 73.850,00
            - Lucros Acumulados: R$ 16.150,00
            
            **TOTAL:** R$ {bs['total_passivo']:,.2f}
            """)
        
        # Gráfico do Balanço
        if PLOTLY_AVAILABLE:
            fig = make_subplots(
                rows=1, cols=2,
                specs=[[{"type": "pie"}, {"type": "pie"}]],
                subplot_titles=("Composição do Ativo", "Composição do Passivo + PL")
            )
            
            # Ativo
            fig.add_trace(go.Pie(
                labels=["Ativo Circulante", "Ativo não Circulante"],
                values=[bs['ativo_circulante'], bs['ativo_nao_circulante']],
                name="Ativo",
                marker_colors=['#3B82F6', '#1E40AF']
            ), row=1, col=1)
            
            # Passivo + PL
            fig.add_trace(go.Pie(
                labels=["Passivo Circulante", "Passivo não Circulante", "Patrimônio Líquido"],
                values=[bs['passivo_circulante'], bs['passivo_nao_circulante'], bs['patrimonio_liquido']],
                name="Passivo + PL",
                marker_colors=['#EF4444', '#F97316', '#10B981']
            ), row=1, col=2)
            
            fig.update_layout(
                title="Estrutura Patrimonial da Alpha Serviços LTDA",
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown("### Demonstração do Resultado do Exercício")
        
        is_ = ALPHA_DATA["income_statement"]
        
        # Tabela da DRE
        dre_data = [
            ["Receita Bruta de Vendas", f"R$ {is_['receita_bruta']:,.2f}"],
            ["(-) Deduções da Receita", f"R$ {is_['deducoes']:,.2f}"],
            ["(=) Receita Líquida", f"R$ {is_['receita_liquida']:,.2f}"],
            ["(-) Custo das Mercadorias/Serviços", f"R$ {is_['custo_mercadorias']:,.2f}"],
            ["(=) Lucro Bruto", f"R$ {is_['lucro_bruto']:,.2f}"],
            ["(-) Despesas com Vendas", f"R$ {is_['despesas_vendas']:,.2f}"],
            ["(-) Despesas Administrativas", f"R$ {is_['despesas_administrativas']:,.2f}"],
            ["(-) Depreciação", f"R$ {is_['depreciacao']:,.2f}"],
            ["(=) Resultado Operacional", f"R$ {is_['resultado_operacional']:,.2f}"],
            ["(+) Receitas Financeiras", f"R$ {is_['receitas_financeiras']:,.2f}"],
            ["(-) Despesas Financeiras", f"R$ {is_['despesas_financeiras']:,.2f}"],
            ["(=) Resultado Antes do IRPJ e CSLL", f"R$ {is_['resultado_antes_ir']:,.2f}"],
            ["(-) IRPJ/CSLL", f"R$ {is_['ir_csll']:,.2f}"],
            ["(=) Lucro Líquido do Período", f"R$ {is_['lucro_liquido']:,.2f}"]
        ]
        
        df_dre = pd.DataFrame(dre_data, columns=["Item", "Valor"])
        st.dataframe(df_dre, use_container_width=True, hide_index=True)
        
        # Gráfico Waterfall da DRE
        if PLOTLY_AVAILABLE:
            fig = go.Figure(go.Waterfall(
                name="DRE",
                orientation="v",
                measure=["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "total"],
                x=["Receita Líquida", "Custo", "Desp. Vendas", "Desp. Admin", "Depreciação", "Rec. Financ.", "Desp. Financ.", "IRPJ/CSLL", "", "", "Lucro Líquido"],
                textposition="outside",
                text=[f"R$ {is_['receita_liquida']:,.0f}", f"-R$ {is_['custo_mercadorias']:,.0f}", 
                      f"-R$ {is_['despesas_vendas']:,.0f}", f"-R$ {is_['despesas_administrativas']:,.0f}",
                      f"-R$ {is_['depreciacao']:,.0f}", f"R$ {is_['receitas_financeiras']:,.0f}",
                      f"-R$ {is_['despesas_financeiras']:,.0f}", f"-R$ {is_['ir_csll']:,.0f}",
                      "", "", f"R$ {is_['lucro_liquido']:,.0f}"],
                y=[is_['receita_liquida'], -is_['custo_mercadorias'], -is_['despesas_vendas'], 
                   -is_['despesas_administrativas'], -is_['depreciacao'], is_['receitas_financeiras'],
                   -is_['despesas_financeiras'], -is_['ir_csll'], 0, 0, is_['lucro_liquido']],
                connector={"line": {"color": "rgb(63, 63, 63)"}},
            ))
            
            fig.update_layout(
                title="Formação do Resultado - Alpha Serviços LTDA",
                showlegend=False,
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)

def show_liquidity_indicators():
    """Exibe indicadores de liquidez"""
    st.markdown("## 💧 Indicadores de Liquidez")
    
    indicators = calculate_indicators()
    
    col1, col2, col3 = st.columns(3)
    
    # Liquidez Corrente
    with col1:
        lc = indicators["liquidez_corrente"]
        status_class = get_status_class("liquidez_corrente", lc["value"])
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💧 Liquidez Corrente</div>
            <div class="metric-value {status_class}">{lc["value"]:.2f}</div>
            <div class="metric-interpretation">{lc["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {lc["formula"]}<br>
            <strong>Cálculo:</strong> {lc["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    # Liquidez Geral
    with col2:
        lg = indicators["liquidez_geral"]
        status_class = get_status_class("liquidez_geral", lg["value"])
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🌊 Liquidez Geral</div>
            <div class="metric-value {status_class}">{lg["value"]:.2f}</div>
            <div class="metric-interpretation">{lg["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {lg["formula"]}<br>
            <strong>Cálculo:</strong> {lg["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    # Capital de Giro
    with col3:
        cg = indicators["capital_giro"]
        status_class = get_status_class("capital_giro", cg["value"])
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Capital de Giro</div>
            <div class="metric-value {status_class}">R$ {cg["value"]:,.0f}</div>
            <div class="metric-interpretation">{cg["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {cg["formula"]}<br>
            <strong>Cálculo:</strong> {cg["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    # Simulador de Liquidez
    st.markdown("### 🧪 Simulador de Cenários de Liquidez")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Ajuste os Valores:")
        ativo_circ = st.slider("Ativo Circulante (R$ mil)", 50, 150, 80, key="ac_sim")
        passivo_circ = st.slider("Passivo Circulante (R$ mil)", 30, 100, 60, key="pc_sim")
    
    with col2:
        # Recalcular indicadores
        lc_sim = (ativo_circ * 1000) / (passivo_circ * 1000)
        cg_sim = (ativo_circ * 1000) - (passivo_circ * 1000)
        
        st.markdown("#### Resultados da Simulação:")
        st.metric("Liquidez Corrente", f"{lc_sim:.2f}", f"{lc_sim - indicators['liquidez_corrente']['value']:.2f}")
        st.metric("Capital de Giro", f"R$ {cg_sim:,.0f}", f"R$ {cg_sim - indicators['capital_giro']['value']:,.0f}")
        
        # Status
        if lc_sim >= 1.5:
            st.success("✅ Situação de liquidez saudável")
        elif lc_sim >= 1.0:
            st.warning("⚠️ Situação de liquidez de atenção")
        else:
            st.error("❌ Situação de liquidez preocupante")

def show_profitability_indicators():
    """Exibe indicadores de rentabilidade"""
    st.markdown("## 📈 Indicadores de Rentabilidade")
    
    indicators = calculate_indicators()
    
    col1, col2, col3 = st.columns(3)
    
    # Margem Bruta
    with col1:
        mb = indicators["margem_bruta"]
        status_class = get_status_class("margem_bruta", mb["value"])
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📊 Margem Bruta</div>
            <div class="metric-value {status_class}">{mb["value"]:.2f}%</div>
            <div class="metric-interpretation">{mb["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {mb["formula"]}<br>
            <strong>Cálculo:</strong> {mb["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    # Margem Operacional
    with col2:
        mo = indicators["margem_operacional"]
        status_class = get_status_class("margem_operacional", mo["value"])
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⚙️ Margem Operacional</div>
            <div class="metric-value {status_class}">{mo["value"]:.2f}%</div>
            <div class="metric-interpretation">{mo["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {mo["formula"]}<br>
            <strong>Cálculo:</strong> {mo["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    # Margem Líquida
    with col3:
        ml = indicators["margem_liquida"]
        status_class = get_status_class("margem_liquida", ml["value"])
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💎 Margem Líquida</div>
            <div class="metric-value {status_class}">{ml["value"]:.2f}%</div>
            <div class="metric-interpretation">{ml["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {ml["formula"]}<br>
            <strong>Cálculo:</strong> {ml["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    # Gráfico de Margens
    if PLOTLY_AVAILABLE:
        fig = go.Figure()
        
        margens = ["Margem Bruta", "Margem Operacional", "Margem Líquida"]
        valores = [mb["value"], mo["value"], ml["value"]]
        cores = ['#10B981', '#3B82F6', '#8B5CF6']
        
        fig.add_trace(go.Bar(
            x=margens,
            y=valores,
            marker_color=cores,
            text=[f"{v:.1f}%" for v in valores],
            textposition='auto',
        ))
        
        fig.update_layout(
            title="Evolução das Margens de Rentabilidade",
            yaxis_title="Percentual (%)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Análise de Rentabilidade
    st.markdown("### 📊 Análise de Rentabilidade")
    
    is_ = ALPHA_DATA["income_statement"]
    
    # Decomposição da Receita
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Decomposição da Receita Líquida")
        
        if PLOTLY_AVAILABLE:
            fig = go.Figure(data=[go.Pie(
                labels=['Lucro Líquido', 'Custos e Despesas'],
                values=[is_['lucro_liquido'], is_['receita_liquida'] - is_['lucro_liquido']],
                hole=.3,
                marker_colors=['#10B981', '#EF4444']
            )])
            
            fig.update_layout(
                title="Composição da Receita",
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Estrutura de Custos e Despesas")
        
        custos_despesas = {
            'Custo das Mercadorias': is_['custo_mercadorias'],
            'Despesas de Vendas': is_['despesas_vendas'],
            'Despesas Administrativas': is_['despesas_administrativas'],
            'Depreciação': is_['depreciacao'],
            'Despesas Financeiras Líquidas': is_['despesas_financeiras'] - is_['receitas_financeiras'],
            'IRPJ/CSLL': is_['ir_csll']
        }
        
        if PLOTLY_AVAILABLE:
            fig = go.Figure(data=[go.Pie(
                labels=list(custos_despesas.keys()),
                values=list(custos_despesas.values()),
                hole=.3
            )])
            
            fig.update_layout(
                title="Estrutura de Custos",
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)

def show_capital_structure():
    """Exibe análise da estrutura de capital"""
    st.markdown("## ⚖️ Estrutura de Capital")
    
    indicators = calculate_indicators()
    bs = ALPHA_DATA["balance_sheet"]
    
    # Indicador Dívida/Patrimônio
    dp = indicators["divida_patrimonio"]
    status_class = get_status_class("divida_patrimonio", dp["value"])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⚖️ Dívida/Patrimônio Líquido</div>
            <div class="metric-value {status_class}">{dp["value"]:.2f}</div>
            <div class="metric-interpretation">{dp["interpretation"]}</div>
            <hr>
            <strong>Fórmula:</strong> {dp["formula"]}<br>
            <strong>Cálculo:</strong> {dp["calculation"]}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Gráfico da Estrutura de Capital
        if PLOTLY_AVAILABLE:
            fig = go.Figure(data=[go.Pie(
                labels=['Patrimônio Líquido', 'Passivo Circulante', 'Passivo não Circulante'],
                values=[bs['patrimonio_liquido'], bs['passivo_circulante'], bs['passivo_nao_circulante']],
                marker_colors=['#10B981', '#EF4444', '#F97316'],
                hole=.4
            )])
            
            fig.update_layout(
                title="Estrutura de Financiamento",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # Análise Detalhada
    st.markdown("### 📊 Análise da Estrutura de Capital")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        participacao_pl = (bs['patrimonio_liquido'] / bs['total_passivo']) * 100
        st.metric("Participação do PL", f"{participacao_pl:.1f}%")
        
    with col2:
        participacao_pc = (bs['passivo_circulante'] / bs['total_passivo']) * 100
        st.metric("Participação do PC", f"{participacao_pc:.1f}%")
        
    with col3:
        participacao_pnc = (bs['passivo_nao_circulante'] / bs['total_passivo']) * 100
        st.metric("Participação do PNC", f"{participacao_pnc:.1f}%")
    
    # Recomendações
    st.markdown("### 💡 Recomendações")
    
    if dp["value"] > 1.0:
        st.warning("""
        ⚠️ **Atenção**: A empresa possui mais dívidas que patrimônio líquido. 
        Recomendações:
        - Reduzir o endividamento
        - Aumentar o capital próprio
        - Renegociar prazos das dívidas
        """)
    elif dp["value"] > 0.5:
        st.info("""
        ℹ️ **Moderado**: Estrutura de capital equilibrada, mas com espaço para melhoria.
        Recomendações:
        - Monitorar evolução do endividamento
        - Avaliar oportunidades de reinvestimento dos lucros
        """)
    else:
        st.success("""
        ✅ **Excelente**: Estrutura de capital conservadora e saudável.
        Recomendações:
        - Manter disciplina financeira
        - Avaliar oportunidades de crescimento
        """)

def show_integrated_analysis():
    """Exibe análise integrada"""
    st.markdown("## 🎯 Análise Integrada")
    
    indicators = calculate_indicators()
    
    # Dashboard de Indicadores
    st.markdown("### 📊 Dashboard de Indicadores")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        lc = indicators["liquidez_corrente"]
        status = "🟢" if lc["value"] >= 1.5 else "🟡" if lc["value"] >= 1.0 else "🔴"
        st.metric("Liquidez Corrente", f"{lc['value']:.2f}", delta=None, help=lc["interpretation"])
        st.markdown(f"Status: {status}")
    
    with col2:
        ml = indicators["margem_liquida"]
        status = "🟢" if ml["value"] >= 20 else "🟡" if ml["value"] >= 10 else "🔴"
        st.metric("Margem Líquida", f"{ml['value']:.1f}%", delta=None, help=ml["interpretation"])
        st.markdown(f"Status: {status}")
    
    with col3:
        cg = indicators["capital_giro"]
        status = "🟢" if cg["value"] > 0 else "🔴"
        st.metric("Capital de Giro", f"R$ {cg['value']:,.0f}", delta=None, help=cg["interpretation"])
        st.markdown(f"Status: {status}")
    
    with col4:
        dp = indicators["divida_patrimonio"]
        status = "🟢" if dp["value"] <= 0.5 else "🟡" if dp["value"] <= 1.0 else "🔴"
        st.metric("Dívida/PL", f"{dp['value']:.2f}", delta=None, help=dp["interpretation"])
        st.markdown(f"Status: {status}")
    
    # Radar Chart dos Indicadores
    if PLOTLY_AVAILABLE:
        st.markdown("### 🎯 Radar dos Indicadores")
        
        # Normalizar indicadores para o radar (0-100)
        radar_data = {
            'Liquidez Corrente': min(lc["value"] * 50, 100),  # Normalizar para 0-100
            'Liquidez Geral': min(indicators["liquidez_geral"]["value"] * 100, 100),
            'Margem Bruta': min(indicators["margem_bruta"]["value"] * 2, 100),
            'Margem Líquida': min(ml["value"] * 5, 100),
            'Estrutura Capital': max(100 - (dp["value"] * 50), 0)  # Inverter para que menor dívida = melhor
        }
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=list(radar_data.values()),
            theta=list(radar_data.keys()),
            fill='toself',
            name='Alpha Serviços',
            line_color='#3B82F6'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="Radar de Performance Financeira",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Matriz SWOT Financeira
    st.markdown("### 🔍 Matriz SWOT Financeira")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 💪 Forças
        - Margem bruta saudável (48,15%)
        - Capital de giro positivo
        - Crescimento no volume de clientes
        - Liquidez corrente acima de 1,0
        """)
        
        st.markdown("""
        #### ⚠️ Fraquezas
        - Controle de custos insuficiente
        - Margem líquida baixa (11,96%)
        - Alto endividamento relativo
        - Falta de interpretação gerencial
        """)
    
    with col2:
        st.markdown("""
        #### 🚀 Oportunidades
        - Melhoria no controle de custos
        - Otimização de despesas administrativas
        - Renegociação de dívidas
        - Implementação de sistema de gestão
        """)
        
        st.markdown("""
        #### ⚡ Ameaças
        - Dependência de financiamentos
        - Pressão sobre margens
        - Concorrência no setor
        - Instabilidade econômica
        """)
    
    # Recomendações Prioritárias
    st.markdown("### 🎯 Recomendações Prioritárias")
    
    st.markdown("""
    #### 🔥 Ações Imediatas (0-3 meses)
    1. **Implementar controle rigoroso de custos e despesas**
    2. **Capacitar sócios na interpretação de demonstrações financeiras**
    3. **Renegociar prazos de fornecedores para melhorar fluxo de caixa**
    
    #### 📈 Ações de Médio Prazo (3-12 meses)
    1. **Reduzir despesas administrativas em 10-15%**
    2. **Implementar sistema de gestão financeira**
    3. **Diversificar fontes de financiamento**
    
    #### 🚀 Ações de Longo Prazo (12+ meses)
    1. **Aumentar capital próprio através de reinvestimento de lucros**
    2. **Expandir operações com base em análise de viabilidade**
    3. **Implementar indicadores de performance (KPIs) regulares**
    """)

def show_ai_consultant():
    """Exibe consultoria com IA"""
    st.markdown("## 🤖 Consultoria Financeira com IA")
    
    # Verificar configuração da IA
    if not configure_gemini():
        st.warning("⚠️ Configure a chave da API do Gemini para usar a consultoria com IA.")
        
        with st.expander("🔧 Como configurar"):
            st.markdown("""
            1. Obtenha sua chave em: https://makersuite.google.com/app/apikey
            2. Para uso local: adicione em `.streamlit/secrets.toml`
            3. Para Streamlit Cloud: adicione nos Secrets do app
            """)
        
        api_key = st.text_input("Chave da API do Gemini:", type="password")
        if api_key:
            st.session_state.gemini_api_key = api_key
            if configure_gemini():
                st.success("✅ IA configurada com sucesso!")
                st.rerun()
        return
    
    st.success("✅ Consultoria IA ativa - Especialista em Alpha Serviços LTDA")
    
    # Interface de chat
    st.markdown("### 💬 Consulte o Especialista")
    
    # Perguntas sugeridas
    st.markdown("#### 💡 Perguntas Sugeridas:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Como melhorar a liquidez da empresa?"):
            question = "Como a Alpha Serviços pode melhorar seus indicadores de liquidez?"
            st.session_state.ai_question = question
        
        if st.button("Análise da estrutura de custos"):
            question = "Faça uma análise detalhada da estrutura de custos da Alpha Serviços e sugira melhorias."
            st.session_state.ai_question = question
    
    with col2:
        if st.button("Estratégias para reduzir endividamento"):
            question = "Quais estratégias a Alpha Serviços pode adotar para reduzir seu endividamento?"
            st.session_state.ai_question = question
        
        if st.button("Como aumentar a rentabilidade?"):
            question = "Como a Alpha Serviços pode aumentar suas margens de rentabilidade?"
            st.session_state.ai_question = question
    
    # Campo de pergunta personalizada
    user_question = st.text_area(
        "Ou faça sua pergunta personalizada:",
        value=st.session_state.get('ai_question', ''),
        placeholder="Ex: Como interpretar o indicador de liquidez corrente de 1,33?",
        key="custom_question"
    )
    
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("🚀 Consultar IA", type="primary"):
            if user_question:
                with st.spinner("🧠 Analisando dados da Alpha Serviços..."):
                    context = "Empresa de pequeno porte no setor de manutenção de móveis e eletrodomésticos com crescimento de clientes mas problemas de controle de custos"
                    response = get_gemini_response(user_question, context)
                    
                    st.session_state.ai_chat_history.append({
                        "question": user_question,
                        "answer": response,
                        "timestamp": time.time()
                    })
                st.rerun()
    
    with col2:
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.ai_chat_history = []
            st.rerun()
    
    # Histórico de conversas
    if st.session_state.ai_chat_history:
        st.markdown("### 📚 Histórico de Consultorias")
        
        for i, chat in enumerate(reversed(st.session_state.ai_chat_history[-3:])):  # Últimas 3 conversas
            with st.expander(f"💬 Consulta {len(st.session_state.ai_chat_history) - i}: {chat['question'][:50]}..."):
                st.markdown(f"**👤 Pergunta:** {chat['question']}")
                st.markdown(f"""
                <div class="ai-response">
                    <strong>🤖 Resposta do Especialista:</strong><br>
                    {chat['answer']}
                </div>
                """, unsafe_allow_html=True)

def main():
    """Função principal do aplicativo"""
    try:
        # Inicializar estado da sessão
        init_session_state()
        
        # Cabeçalho com logo da Unifor
        st.markdown("""
        <div class="unifor-logo">
            <img src="https://www.unifor.br/documents/392178/3101527/logo.png" width="200" alt="Unifor">
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h1 class="main-header">🎓 Adm Academy - Análise Financeira</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Análise Prática da Alpha Serviços LTDA</p>', unsafe_allow_html=True)
        
        # Barra de progresso baseada na seção atual
        sections = ['home', 'statements', 'liquidity', 'profitability', 'capital_structure', 'integrated_analysis', 'ai_consultant']
        current_index = sections.index(st.session_state.current_section) if st.session_state.current_section in sections else 0
        progress = (current_index + 1) / len(sections)
        
        st.markdown(f'<div class="progress-indicator" style="width: {progress * 100}%;"></div>', unsafe_allow_html=True)
        
        # Navegação principal
        if st.session_state.current_section == 'home':
            show_company_overview()
            show_navigation()
            
        elif st.session_state.current_section == 'statements':
            if st.button("← Voltar ao Menu", key="back_statements"):
                st.session_state.current_section = 'home'
                st.rerun()
            show_statements()
            
        elif st.session_state.current_section == 'liquidity':
            if st.button("← Voltar ao Menu", key="back_liquidity"):
                st.session_state.current_section = 'home'
                st.rerun()
            show_liquidity_indicators()
            
        elif st.session_state.current_section == 'profitability':
            if st.button("← Voltar ao Menu", key="back_profitability"):
                st.session_state.current_section = 'home'
                st.rerun()
            show_profitability_indicators()
            
        elif st.session_state.current_section == 'capital_structure':
            if st.button("← Voltar ao Menu", key="back_capital"):
                st.session_state.current_section = 'home'
                st.rerun()
            show_capital_structure()
            
        elif st.session_state.current_section == 'integrated_analysis':
            if st.button("← Voltar ao Menu", key="back_integrated"):
                st.session_state.current_section = 'home'
                st.rerun()
            show_integrated_analysis()
            
        elif st.session_state.current_section == 'ai_consultant':
            if st.button("← Voltar ao Menu", key="back_ai"):
                st.session_state.current_section = 'home'
                st.rerun()
            show_ai_consultant()
        
        # Sidebar com informações
        with st.sidebar:
            st.markdown("### 📊 Informações da Empresa")
            st.markdown(f"""
            **Nome:** {ALPHA_DATA['company_info']['name']}
            **Segmento:** {ALPHA_DATA['company_info']['segment'][:30]}...
            **Porte:** {ALPHA_DATA['company_info']['size']}
            """)
            
            st.markdown("---")
            st.markdown("### 🎯 Indicadores Resumo")
            
            indicators = calculate_indicators()
            
            st.metric("Liquidez Corrente", f"{indicators['liquidez_corrente']['value']:.2f}")
            st.metric("Margem Líquida", f"{indicators['margem_liquida']['value']:.1f}%")
            st.metric("Capital de Giro", f"R$ {indicators['capital_giro']['value']:,.0f}")
            st.metric("Dívida/PL", f"{indicators['divida_patrimonio']['value']:.2f}")
            
            st.markdown("---")
            st.markdown("### 🧭 Navegação Rápida")
            
            if st.button("🏠 Início", use_container_width=True):
                st.session_state.current_section = 'home'
                st.rerun()
            
            if st.button("📊 Demonstrações", use_container_width=True):
                st.session_state.current_section = 'statements'
                st.rerun()
            
            if st.button("💧 Liquidez", use_container_width=True):
                st.session_state.current_section = 'liquidity'
                st.rerun()
            
            if st.button("📈 Rentabilidade", use_container_width=True):
                st.session_state.current_section = 'profitability'
                st.rerun()
            
            if st.button("⚖️ Estrutura Capital", use_container_width=True):
                st.session_state.current_section = 'capital_structure'
                st.rerun()
            
            if st.button("🎯 Análise Integrada", use_container_width=True):
                st.session_state.current_section = 'integrated_analysis'
                st.rerun()
            
            if st.button("🤖 Consultoria IA", use_container_width=True):
                st.session_state.current_section = 'ai_consultant'
                st.rerun()
            
            st.markdown("---")
            st.markdown("### ℹ️ Sobre")
            st.markdown("""
            **Adm Academy** - Plataforma educacional para análise financeira com dados reais.
            
            Desenvolvido para estudantes de Administração e Ciências Contábeis da Unifor.
            """)
                
    except Exception as e:
        st.error(f"Erro na aplicação: {str(e)}")
        st.markdown("**Detalhes do erro para debug:**")
        st.code(str(e))

if __name__ == "__main__":
    main()

