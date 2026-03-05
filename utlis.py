# import streamlit as st

# def apply_modern_theme():
#     st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
#     .stApp {
#         background: #f8fafc;
#         font-family: 'Inter', sans-serif;
#     }
    
#     .main .block-container {
#         padding: 1rem;
#         max-width: 100%;
#     }
    
#     .stButton>button {
#         border-radius: 8px;
#         font-weight: 600;
#         border: none;
#         padding: 0.5rem 1rem;
#     }
    
#     .stButton>button:hover {
#         transform: translateY(-1px);
#         transition: all 0.2s ease;
#     }
    
#     h1, h2, h3 {
#         font-family: 'Inter', sans-serif;
#         font-weight: 700;
#         color: #1e293b;
#     }
    
#     h1 {
#         text-align: center;
#         margin-bottom: 0.5rem;
#         color: #1e293b;
#     }
    
#     .stDataFrame {
#         border-radius: 8px !important;
#         border: 1px solid #e2e8f0 !important;
#     }
    
#     .stTabs [data-baseweb="tab-list"] {
#         gap: 2px;
#         background: #f1f5f9;
#         padding: 4px;
#         border-radius: 8px;
#     }
    
#     .stTabs [data-baseweb="tab"] {
#         border-radius: 6px;
#         font-weight: 500;
#         padding: 8px 16px;
#     }
    
#     .stTabs [aria-selected="true"] {
#         background: #3b82f6 !important;
#         color: white !important;
#     }
    
#     /* Compact layout */
#     [data-testid="stVerticalBlock"] {
#         gap: 0.5rem;
#     }
#     </style>
#     """, unsafe_allow_html=True)
import streamlit as st

def apply_modern_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Base Styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #f8fafc 100%);
        font-family: 'Inter', sans-serif;
        color: #e2e8f0;
    }
    
    .main .block-container {
        padding: 1.5rem;
        max-width: 100%;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        margin: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06b6d4 100%);
        padding: 2rem 1rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-header h1 {
        font-size: 2.2rem;
        margin: 0;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-header p {
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-weight: 400;
    }
    
    /* Button Styling */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        border: none;
        padding: 0.75rem 1.5rem;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
    }
    
    /* Secondary Buttons */
    .stButton>button[kind="secondary"] {
        background: linear-gradient(135deg, #475569 0%, #64748b 100%);
        box-shadow: 0 4px 12px rgba(71, 85, 105, 0.3);
    }
    
    .stButton>button[kind="secondary"]:hover {
        background: linear-gradient(135deg, #64748b 0%, #475569 100%);
        box-shadow: 0 6px 20px rgba(71, 85, 105, 0.4);
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.4);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #f1f5f9;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 0.5rem 0 0 0;
        font-weight: 600;
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        opacity: 0.9;
    }
    
    /* Section Headers */
    .section-header {
        color: #f1f5f9;
        border-bottom: 2px solid #334155;
        padding-bottom: 0.75rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
        font-size: 1.3rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Dataframe Styling */
    .stDataFrame {
        border-radius: 12px !important;
        border: 1px solid #334155 !important;
        background: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(10px);
    }
    
    /* Input Fields */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #f1f5f9 !important;
        padding: 0.75rem !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stNumberInput>div>div>input:focus,
    .stSelectbox>div>div>select:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #f1f5f9 !important;
        font-weight: 600;
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid #334155 !important;
        border-top: none !important;
        border-radius: 0 0 8px 8px !important;
    }
    
    /* Success/Warning/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #10b98120 0%, #05966920 100%) !important;
        border: 1px solid #10b981 !important;
        border-left: 4px solid #10b981 !important;
        color: #a7f3d0 !important;
        border-radius: 8px;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #f59e0b20 0%, #d9770620 100%) !important;
        border: 1px solid #f59e0b !important;
        border-left: 4px solid #f59e0b !important;
        color: #fde68a !important;
        border-radius: 8px;
    }
    
    .stError {
        background: linear-gradient(135deg, #ef444420 0%, #dc262620 100%) !important;
        border: 1px solid #ef4444 !important;
        border-left: 4px solid #ef4444 !important;
        color: #fecaca !important;
        border-radius: 8px;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #3b82f620 0%, #1d4ed820 100%) !important;
        border: 1px solid #3b82f6 !important;
        border-left: 4px solid #3b82f6 !important;
        color: #93c5fd !important;
        border-radius: 8px;
    }
    
    /* Quick Actions Box */
    .quick-actions-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Navigation Sidebar */
    .css-1d391kg {
        background: rgba(15, 23, 42, 0.9) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid #334155;
    }
    
    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e293b;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
    }
    
    /* Text Colors */
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    
    p, label, div {
        color: #e2e8f0;
    }
    
    /* Compact spacing */
    [data-testid="stVerticalBlock"] {
        gap: 0.75rem;
    }
    
    /* Download buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
    }
    
    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #047857 0%, #059669 100%) !important;
        box-shadow: 0 6px 20px rgba(5, 150, 105, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def create_metric_card(label, value, icon):
    """Create a modern metric card with glassmorphism effect"""
    return f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """
