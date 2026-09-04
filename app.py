import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="منصة بَيِّنَة الذكية",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تحسين تصميم الواجهة والخطوط
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    html, body, [class*="css"], font, span, div, p, h1, h2, h3, input, button {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    .main-header {
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        padding: 2rem 1rem;
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
</style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("💡 عن المنصة")
    
    st.info("""
    **منصة بَيِّنَة الذكية** (نسخة تجريبية)
    
    منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة لضمان أعلى درجات الموثوقية والحد من الاجتهاد الخارجي.
    
    > *"فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ"*
    """)
    
    st.markdown("---")
    st.caption("تطوير وبرمجة:")
    st.markdown("**م. خالد علي الجهني**")
    st.divider()
    st.markdown("<b>📖 المرجع النشط:</b> كتاب فقه العبادات", unsafe_allow_html=True)

# 4. الهيدر الرئيسي
st.markdown("""
<div class="main-header">
    <h1 style="margin:0; font-size: 1.8rem; font-weight: 800; color: white;">منصة بَيِّنَة للبحث والاستدلال الفقهي</h1>
    <p style="margin-top: 10px; font-size: 1rem; opacity: 0.9; color: #e2e8f0;">مساعدك الذكي لإستخراج الأحكام الشرعية المدعومة بالنصوص المباشرة</p>
</div>
""", unsafe_allow_html=True)

# 5. منطقة التفاعل والاستعلام
user_query = st.text_input("أدخل مسألتك الفقهية هنا:", placeholder="مثال: ما حكم صلاة المسافر في الطائرة؟")

if user_query:
    st.success(f"جاري البحث والاستدلال عن: **{user_query}**")
