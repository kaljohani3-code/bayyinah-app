import os
import re
import streamlit as st

# 1. إعداد الصفحة وتفعيل التصميم التجاوبي
st.set_page_config(
    page_title="منصة بَيِّنَة - الاستدلال الموثوق",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إضافة لمسات وتصميم CSS مخصص للواجهة
st.markdown("""
    <style>
    /* خلفية وتنسيق رئيسي */
    .main {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* الهيدر الرئيسي */
    .title-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 2rem;
    }
    .title-header h1 {
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .title-header p {
        color: #e0e0e0;
        font-size: 1.1rem;
    }

    /* بطاقة النتيجة المقتبسة */
    .result-card {
        background-color: #ffffff;
        border-right: 5px solid #2a5298;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease;
    }
    .result-card:hover {
        transform: translateY(-2px);
    }
    .result-meta {
        display: inline-block;
        background-color: #eef2f7;
        color: #1e3c72;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 0.8rem;
    }
    .result-body {
        color: #333333;
        font-size: 1.05rem;
        line-height: 1.8;
        white-space: pre-line;
    }

    /* القائمة الجانبية */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-left: 1px solid #e9ecef;
    }
    </style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/isometric/512/scale.png", width=100)
    st.title("عن المنصة")
    st.info("""
    ** منصة بَيِّنَة الذكية**
    
    منظومة استدلال فقهي تعتمد النص المباشر والمشروط من المراجع المعتمدة، لضمان أعلى درجات الموثوقية والحد من الاجتهاد الخارجي.
    """)
    st.divider()
    st.markdown("<b>المرجع النشط:</b><br>📖 كتاب فقه العبادات", unsafe_allow_html=True)

# 4. واجهة الصفحة الرئيسية
st.markdown("""
    <div class="title-header">
        <h1> منصة بَيِّنَة الذكية</h1>
        <p>للاستدلال الفقهي والفتوى الموثوقة من المراجع الرسمية مباشرة</p>
    </div>
""", unsafe_allow_html=True)

text_path = "sample_reference.txt"

def clean_arabic(text):
    if not text:
        return ""
    text = re.sub(r'[\u064B-\u0652]', '', text)
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ة', 'ه', text)
    return text

def load_reference_data():
    if not os.path.exists(text_path):
        return []
    
    with open(text_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    raw_pages = content.split("[صفحة ")
    pages_data = []
    
    for p in raw_pages:
        if not p.strip():
            continue
        parts = p.split("]\n", 1)
        page_num = parts[0]
        text_body = parts[1] if len(parts) > 1 else parts[0]
        
        pages_data.append({
            "page": page_num,
            "raw_text": text_body.strip(),
            "cleaned_text": clean_arabic(text_body)
        })
        
    return pages_data

pages_data = load_reference_data()

if not pages_data:
    st.error("لم يتم العثور على الملف النصي المرجعي `sample_reference.txt`!")
    st.stop()

# 5. منطقة صندوق البحث
st.markdown("### 🔍 بحث في المرجع الفقهي المعتمد")
user_query = st.text_input("", placeholder="اكتب سؤالك هنا (مثال: ما هي أركان الوضوء، حكم الصلاة...)")

if user_query:
    with st.spinner("جاري استخراج الأدلة والنصوص المباشرة..."):
        cleaned_query = clean_arabic(user_query)
        search_words = [w.strip() for w in cleaned_query.split() if len(w.strip()) > 1]
        
        matches = []
        for p in pages_data:
            score = 0
            for w in search_words:
                if w in p["cleaned_text"]:
                    score += p["cleaned_text"].count(w) * 3
            
            if score > 0:
                matches.append((score, p))
                
        matches.sort(key=lambda x: x[0], reverse=True)
        relevant_pages = [m[1] for m in matches[:3]]
        
        st.markdown("<br><h4>📋 النصوص والاستدلالات المباشرة:</h4>", unsafe_allow_html=True)
        
        if not relevant_pages:
            st.warning("⚠️ (لا توجد معلومة موثوقة في المراجع المعتمدة لهذه المسألة)")
        else:
            for i, p in enumerate(relevant_pages, 1):
                # عرض النتائج في بطاقات أنيقة
                st.markdown(f"""
                    <div class="result-card">
                        <div class="result-meta">المصدر: كتاب فقه العبادات | صفحة {p['page']}</div>
                        <div class="result-body">{p['raw_text']}</div>
                    </div>
                """, unsafe_allow_html=True)
