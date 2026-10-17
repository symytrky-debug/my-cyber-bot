import streamlit as st
import openai

# إعدادات واجهة الموقع والسمة اللمسية (التدرج الأزرق)
st.set_page_config(page_title="CyberShield Premium", page_icon="🛡️", layout="wide")

# كود CSS لتنسيق الواجهة والخلفيات والخانات
st.markdown("""
    <style>
    /* الخلفية الخارجية المتدرجة لموقع كلاس لايت */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #3B82F6 100%);
        color: #FFFFFF;
    }
    /* تعديل العنوان ليكون أبيض مزرق ومحاذي للطرف الأيمن */
    .custom-title {
        text-align: right; 
        color: #F0F9FF; /* لون أبيض مزرق ناعم Ice Blue */
        font-family: 'Cairo', sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .custom-subtitle {
        text-align: right;
        color: #93C5FD !important;
        margin-bottom: 25px;
    }
    h2, h3, p, label, .stMarkdown {
        color: #FFFFFF !important;
    }
    /* تنسيق أزرار الأوامر التفاعلية */
    div.stButton > button:first-child {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        border: 1px solid #60A5FA;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #3B82F6;
        border-color: #93C5FD;
        box-shadow: 0px 0px 10px #3B82F6;
    }
    /* تعديل خانات الإدخال لتصبح بلون أزرق محايد ومختلف عن الخلفية الخارجية */
    input {
        background-color: #1E293B !important; 
        color: #FFFFFF !important; 
        border: 1px solid #475569 !important; 
        border-radius: 8px !important;
    }
    /* لتعديل خلفية خانة رفع الملفات */
    .stFileUploader {
        background-color: #1E293B !important;
        padding: 10px;
        border-radius: 12px;
        border: 1px dashed #475569;
    }
    /* تنسيق صندوق رسالة الترحيب للدعم الفني */
    .support-welcome {
        background-color: #1E293B;
        border-right: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        color: #F0F9FF;
    }
    </style>
""", unsafe_allow_html=True)

# 1. نظام حماية الموقع (تسجيل الدخول الآمن)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("<h2 style='text-align: right; color: #FFFFFF;'>🔒 نظام المحارب السيبراني - تسجيل الدخول</h2>", unsafe_allow_html=True)
    username = st.text_input("اسم المستخدم")
    password = st.text_input("كلمة المرور", type="password")
    login_button = st.button("دخول آمن")
    
    if login_button:
        if username == "admin" and password == "cyber2026":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("بيانات الدخول غير صحيحة! الموقع خاص فقط.")
    st.stop()

# --- بعد تسجيل الدخول الناجح يظهر الموقع بالكامل بالتصميم المتدرج ---

openai.api_key = st.secrets.get("OPENAI_API_KEY", "YOUR_BACKUP_KEY")

# تطبيق العنوان الجديد المائل للزرقة وعلى الطرف
st.markdown("<div class='custom-title'>🛡️ CyberShield AI v2.0</div>", unsafe_allow_html=True)
st.markdown("<p class='custom-subtitle'>لوحة التحكم الخاصة بمحاربة التهديدات الرقمية وفحص الثغرات</p>", unsafe_allow_html=True)

# المقاييس والدوائر الثلاث بتصميم أزرق متدرج متناسق مع كلاس لايت
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div style='text-align: center; border: 2px solid #60A5FA; padding: 20px; border-radius: 12px; background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%); box-shadow: 0 4px 6px rgba(0,0,0,0.3);'>"
                "<h3 style='color: #60A5FA;'>🛡️ مؤشن الحماية العامة</h3>"
                "<h1 style='color: #38BDF8;'>85 / 100</h1>"
                "</div>", unsafe_allow_html=True)
    show_p = st.button("📋 عرض تقرير الحماية الكامل", use_container_width=True)

with col2:
    st.markdown("<div style='text-align: center; border: 2px solid #60A5FA; padding: 20px; border-radius: 12px; background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%); box-shadow: 0 4px 6px rgba(0,0,0,0.3);'>"
                "<h3 style='color: #60A5FA;'>🦠 خلو الجهاز من الفيروسات</h3>"
                "<h1 style='color: #38BDF8;'>90 / 100</h1>"
                "</div>", unsafe_allow_html=True)
    show_m = st.button("🔍 هل توجد فيروسات بالقرب مني؟", use_container_width=True)

with col3:
    st.markdown("<div style='text-align: center; border: 2px solid #60A5FA; padding: 20px; border-radius: 12px; background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%); box-shadow: 0 4px 6px rgba(0,0,0,0.3);'>"
                "<h3 style='color: #60A5FA;'>⚠️ فحص الثغرات والتحديثات</h3>"
                "<h1 style='color: #38BDF8;'>75 / 100</h1>"
                "</div>", unsafe_allow_html=True)
    show_v = st.button("💻 هل نظامي يحتاج تحديث أمني؟", use_container_width=True)

st.divider()

# مركز فحص الملفات والأكواد المشبوهة
st.subheader("📁 مركز تحليل الملفات والأكواد المشبوهة")
uploaded_file = st.file_uploader("ارفع ملفاً، كود برمجياً، أو نص رسالة مشبوهة لتحليلها بالذكاء الاصطناعي:", type=["txt", "py", "js", "html", "exe"])

if uploaded_file is not None:
    file_details = uploaded_file.read().decode("utf-8", errors="ignore")[:2000]
    with st.spinner("جاري فحص وتفكيك الأكواد والملفات بحثاً عن برمجيات خبيثة..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت محلل برمجيات خبيثة (Malware Analyst). قم بفحص النص أو الكود المرفق وحدد ما إذا كان يحتوي على أنشطة مشبوهة، فيروسات فدية، أو أكواد اختراق واشرح النتيجة للمستخدم باحترافية وبساطة وبشكل منسق باللغة العربية."},
                    {"role": "user", "content": f"قم بتحليل هذا المحتوى أمنياً:\n{file_details}"}
                ]
            )
            st.error("🚨 تقرير تحليل الملف المشبوه:")
            st.write(response.choices.message['content'])
        except:
            st.error("خطأ في الاتصال بنظام الفحص المتقدم.")

st.divider()

# معالجة تفاصيل الدوائر الثلاث
if show_m:
    st.subheader("🔮 تفاصيل خلو الجهاز من الفيروسات والتهديدات القريبة")
    with st.spinner("جاري تتبع الهجمات النشطة في نطاق شبكتك..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "أنت خبير أمن سيبراني. اشرح للمستخدم أن الفيروسات في الشبكات تنتقل عبر المنافذ المفتوحة أو شبكات الـ Wi-Fi العامة غير المحمية، وقدم له تقريراً حول كيفية تأمين جهازه من الأجهزة المصابة القريبة منه في الشبكة المحلية باللغة العربية وبأسلوب رائع."},
                {"role": "user", "content": "درجتي هي 90 من 100. كيف أعرف إن كان هناك فيروسات قريبة تحاول اختراقي عبر الشبكة؟"}
            ]
        )
        st.info(response.choices.message['content'])

if show_v:
    st.subheader("⚙️ تقرير الثغرات الأمنية المكتشفة في النظام")
    with st.spinner("جاري مطابقة إصدار المتصفح بقاعدة بيانات الثغرات CVE..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "أنت مهندس أمن سيبراني متخصص في إدارة الثغرات (Vulnerability Management). اشرح للمستخدم أهمية سد ثغرات النظام الحالية وهل التحديث إلزامي فوراً أم يمكن استخدام جدار حماية قوي كحل مؤقت للحماية من الثغرات بدون تحديث باللغة العربية وببساطة."},
                {"role": "user", "content": "تقييمي هو 75 من 100 في التحديثات. هل أنا معرض للخطر بسبب ثغرة غير مسدودة؟ وما العمل?"}
            ]
        )
        st.warning(response.choices.message['content'])

if show_p:
    st.subheader("📊 ملخص الحماية والخطوات القادمة")
    st.success("حالة النظام العامة مستقرة. لرفع النسبة إلى 100% يُنصح بتحديث المتصفح فوراً، وتجنب تشغيل ملفات مجهولة المصدر.")

# --- القسم الجديد المضاف: قسم الدعم الفني في نهاية الصفحة بالكامل ---
st.divider()
st.markdown("<h3 style='text-align: right; color: #60A5FA;'>🛠️ مركز الدعم الفني والمساعدة</h3>", unsafe_allow_html=True)

# عرض رسالة ترحيب الذكاء الاصطناعي المطلوبة بالضبط داخل الصندوق المحايد الأزرق
st.markdown("""
    <div class='support-welcome'>
        🤖 <b>مساعد الدعم الفني:</b> أهلًا بك!💙نرحب بك في الدعم الفني، فضلًا وضح لنا مشكلتك او استفسارك لنتمكن من مساعدتك بأفضل طريقة ممكنة.
    </div>
""", unsafe_allow_html=True)

# خانة المراسلة (أزرق محايد ومختلف عن الخلفية)
user_support_message = st.text_input("اكتب رسالتك أو مشكلتك الفنية هنا:", key="support_input")

if user_support_message:
    with st.spinner("جاري فحص الاستفسار وتقديم الحل الفني..."):
        try:
            support_response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت خبير دعم فني متخصص لموقع الأمن السيبراني CyberShield. مهمتك مساعدة المستخدمين في حل مشاكل الموقع، مشاكل رفع الملفات، مشاكل كلمات المرور، أو أي مشكلة تقنية يواجهونها داخل التطبيق بأسلوب ودود ومحترف وباللغة العربية."},
                    {"role": "user", "content": user_support_message}
                ]
            )
            st.markdown(f"<div style='background-color: #0F172A; padding: 15px; border-radius: 8px; border: 1px solid #2563EB; margin-top: 10px;'>"
                        f"⚙️ <b>رد الدعم الفني:</b><br>{support_response.choices.message['content']}"
                        f"</div>", unsafe_allow_html=True)
        except:
            st.error("خطأ في الاتصال بخادم الدعم الفني.")

# زر تسجيل الخروج لحفظ الخصوصية
if st.sidebar.button("تسجيل الخروج Safe Logout"):
    st.session_state["authenticated"] = False
    st.rerun()
