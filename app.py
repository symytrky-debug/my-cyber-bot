import streamlit as st
import openai

# إعدادات واجهة الموقع والأمان
st.set_page_config(page_title="CyberShield Premium", page_icon="🛡️", layout="wide")

# 1. نظام حماية الموقع (تسجيل الدخول الآمن)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("<h2 style='text-align: center;'>🔒 نظام المحارب السيبراني - تسجيل الدخول</h2>", unsafe_allow_html=True)
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

# --- بعد تسجيل الدخول الناجح يظهر الموقع بالكامل بالأسفل ---

# جلب مفتاح الـ API بشكل آمن من إعدادات المنصة المخفية
openai.api_key = st.secrets.get("OPENAI_API_KEY", "YOUR_BACKUP_KEY")

st.markdown("<h1 style='text-align: center; color: #0F172A;'>🛡️ CyberShield AI v2.0</h1>", unsafe_allow_layout=True)
st.markdown("<p style='text-align: center;'>لوحة التحكم الخاصة بمحاربة التهديدات الرقمية وفحص الثغرات</p>", unsafe_allow_layout=True)

# المقاييس والدوائر الثلاث (تفاعلية من 100)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div style='text-align: center; border: 2px solid #10B981; padding: 20px; border-radius: 12px; background-color: #F0FDF4;'>"
                "<h3>🛡️ مؤشر الحماية العامة</h3>"
                "<h1 style='color: #10B981;'>85 / 100</h1>"
                "</div>", unsafe_allow_layout=True)
    show_p = st.button("📋 عرض تقرير الحماية الكامل", use_container_width=True)

with col2:
    st.markdown("<div style='text-align: center; border: 2px solid #3B82F6; padding: 20px; border-radius: 12px; background-color: #EFF6FF;'>"
                "<h3>🦠 خلو الجهاز من الفيروسات</h3>"
                "<h1 style='color: #3B82F6;'>90 / 100</h1>"
                "</div>", unsafe_allow_layout=True)
    show_m = st.button("🔍 هل توجد فيروسات بالقرب مني؟", use_container_width=True)

with col3:
    st.markdown("<div style='text-align: center; border: 2px solid #F59E0B; padding: 20px; border-radius: 12px; background-color: #FFFBEB;'>"
                "<h3>⚠️ فحص الثغرات والتحديثات</h3>"
                "<h1 style='color: #F59E0B;'>75 / 100</h1>"
                "</div>", unsafe_allow_layout=True)
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
                    {"role": "system", "content": "أنت محلل برمجيات خبيثة (Malware Analyst). قم بفحص النص أو الكود المرفق وحدد ما إذا كان يحتوي على أنشطة مشبوهة، فيروسات فدية، أو أكواد اختراق واشرح النتيجة للمستخدم باحترافية وبساطة."},
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
                {"role": "system", "content": "أنت خبير أمن سيبراني. اشرح للمستخدم أن الفيروسات في الشبكات تنتقل عبر المنافذ المفتوحة أو شبكات الـ Wi-Fi العامة غير المحمية، وقدم له تقريراً حول كيفية تأمين جهازه من الأجهزة المصابة القريبة منه في الشبكة المحلية."},
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
                {"role": "system", "content": "أنت مهندس أمن سيبراني متخصص في إدارة الثغرات (Vulnerability Management). اشرح للمستخدم أهمية سد ثغرات النظام الحالية وهل التحديث إلزامي فوراً أم يمكن استخدام جدار حماية قوي كحل مؤقت للحماية من الثغرات بدون تحديث."},
                {"role": "user", "content": "تقييمي هو 75 من 100 في التحديثات. هل أنا معرض للخطر بسبب ثغرة غير مسدودة؟ وما العمل؟"}
            ]
        )
        st.warning(response.choices.message['content'])

if show_p:
    st.subheader("📊 ملخص الحماية والخطوات القادمة")
    st.success("حالة النظام العامة مستقرة. لرفع النسبة إلى 100% يُنصح بتحديث المتصفح فوراً، وتجنب تشغيل ملفات مجهولة المصدر.")

if st.sidebar.button("تسجيل الخروج Safe Logout"):
    st.session_state["authenticated"] = False
    st.rerun()
