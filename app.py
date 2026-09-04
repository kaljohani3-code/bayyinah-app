import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="منصة بَيِّنَة الذكية",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تطبيق الخط والتنسيقات الآمنة للشاشات
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

    html, body, [class*="css"], font, span, div, p, h1, h2, h3, input, button {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    .main-card {
        background: linear-gradient(135deg, #1e3a8a, #0f172a);
        padding: 2rem 1.2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        margin-bottom: 1.5rem;
    }

    .main-card h1 {
        color: #ffffff !important;
        font-size: 1.7rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
    }

    .main-card p {
        color: #cbd5e1 !important;
        font-size: 0.95rem !important;
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("💡 عن المنصة")
    
    st.info("""
    **منصة بَيِّنَة الذكية** (نسخة تجريبية)
    
    منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة لضمان أعلى درجات الموثوقية والحد من الاخطاء.
    
    > *"فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ"*
    """)
    
    st.markdown("---")
    st.caption("تطوير وبرمجة:")
    st.markdown("**م. خالد علي الجهني**")
    st.divider()
    st.markdown("📖 **المرجع النشط:** كتاب فقه العبادات")

# 4. الواجهة الرئيسية (الكارت الأزرق)
st.markdown("""
<div class="main-card">
    <h1>منصة بَيِّنَة للبحث والاستدلال الفقهي</h1>
    <p>مساعدك الذكي لإستخراج الأحكام الشرعية المدعومة بالنصوص المباشرة</p>
</div>
""", unsafe_allow_html=True)

# 5. منطقة التفاعل والاستعلام
user_query = st.text_input("أدخل مسألتك الفقهية هنا:", placeholder="مثال: ما حكم صلاة المسافر في الطائرة؟")

if user_query:
    st.success(f"جاري البحث والاستدلال عن: **{user_query}**")
