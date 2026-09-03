import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="منصة بَيِّنَة الذكية",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تحسين تصميم الواجهة والخطوط (CSS Modern UI)
css_code = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    html, body, [class*="css"], font, span, div, p, h1, h2, h3, input, button {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    .main-header {
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        text-align: center !important;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
        margin-bottom: 2rem;
    }

    .stTextInput input {
        border-radius: 12px !important;
        border: 2px solid #cbd5e1 !important;
        padding: 12px 16px !important;
        font-size: 1.05rem !important;
    }

    .stSuccess {
        background-color: #f0fdf4 !important;
        border: 1px solid #bbf7d0 !important;
        border-right: 6px solid #16a34a !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
    }

    .stSuccess div {
        color: #064e3b !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
    }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("💡 عن المنصة")
    
    sidebar_html = """
    <div style="background-color: #f1f5f9; padding: 1.2rem; border-radius: 12px; border-right: 4px solid #1e3a8a; margin-bottom: 1rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <h4 style="color: #1e3a8a; margin: 0; font-weight: 700;">منصة بَيِّنَة الذكية</h4>
            <span style="background-color: #fef3c7; color: #d97706; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 6px; border: 1px solid #fde68a;">نسخة تجريبية</span>
        </div>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom: 0.8rem;">
            منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة لضمان أعلى درجات الموثوقية والحد من الاجتهاد الخارجي.
        </p>
        <p style="color: #0f172a; font-size: 0.9rem; font-weight: 700; text-align: center; background: #e2e8f0; padding: 6px; border-radius: 8px; margin: 0;">
            "فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ"
        </p>
    </div>
    
    <div style="background-color: #ffffff; padding: 1rem; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
        <p style="margin: 0; font-size: 0.85rem; color: #64748b;">تطوير وبرمجة:</p>
        <p style="margin: 4px 0 0 0; font-size: 1rem; font-weight: 700; color: #0f172a;">م. خالد علي الجهني</p>
    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<b>📖 المرجع النشط:</b> كتاب فقه العبادات", unsafe_allow_html=True)

# 4. الهيدر الرئيسي
header_html = """
<div class="main-header">
    <h1 style="margin:0; font-size: 2.2rem; font-weight: 800;">منصة بَيِّنَة للبحث والاستدلال الفقهي</h1>
    <p style="margin-top: 10px; font-size: 1.1rem; opacity: 0.9;">مساعدك الذكي لإستخراج الأحكام الشرعية المدعومة بالنصوص المباشرة</p>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# 5. منطقة التفاعل والاستعلام
user_query = st.text_input("أدخل مسألتك الفقهية هنا:", placeholder="مثال: ما حكم صلاة المسافر في الطائرة؟")

if user_query:
    st.success(f"جاري البحث والاستدلال عن: **{user_query}**")
