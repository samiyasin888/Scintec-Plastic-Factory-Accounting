# Global Accounting - دليل المستخدم الشامل
# Global Accounting - Complete User Guide

---

## العربية

---

# دليل المستخدم الشامل لبرنامج Global Accounting

## المحتويات
1. مقدمة عن البرنامج
2. متطلبات النظام والتثبيت
3. الشاشة الرئيسية والتنقل
4. إدارة الفواتير
5. إدارة المخزون
6. إدارة الرواتب
7. التقارير
8. الإعدادات
9. استكشاف الأخطاء والحلول
10. نصائح مهمة

---

## 1. مقدمة عن البرنامج

### ما هو Global Accounting؟

Global Accounting هو نظام محاسبي ومخزني متكامل يُسهّل إدارة العمليات اليومية للشركات والمصانع. يوفر البرنامج أدوات سهلة الاستخدام لإدارة:
- الفواتير والعمليات البيعية
- المخزون والمنتجات
- الرواتب والموظفين
- التقارير والإحصائيات

### المميزات الرئيسية

- **إدارة كاملة:** فواتير، مخزون، رواتب، تقارير في مكان واحد
- **دعم عربي/إنجليزي:** واجهة كاملة بالعربية والإنجليزية
- **قاعدة بيانات محلية:** جميع البيانات محفوظة على جهازك بأمان
- **سهل الاستخدام:** واجهة بسيطة ومفهومة
- **قابل للتخصيص:** تخصيص كامل لبيانات شركتك

---

## 2. متطلبات النظام والتثبيت

### متطلبات النظام

| المتطلب | الحد الأدنى |
|--------|-----------|
| نظام التشغيل | Windows 7 SP1 أو أحدث |
| الذاكرة (RAM) | 256 ميجابايت |
| مساحة التخزين | 100 ميجابايت |
| دقة الشاشة | 1024 × 768 بكسل |
| الإنترنت | غير مطلوب |

### خطوات التثبيت

#### الطريقة الأولى: استخدام المثبت (موصى به)

```
1. انقر نقراً مزدوجاً على ملف: GlobalAccounting-Setup-1.0.0.exe
2. قد يطلب منك السماح بتشغيل البرنامج - انقر "Yes" (نعم)
3. ستظهر نافذة معالج التثبيت
4. اقرأ اتفاقية الترخيص وانقر "I Agree" (أوافق)
5. اختر موقع التثبيت (الافتراضي: C:\Program Files\Global Accounting)
6. اختر ما إذا كنت تريد اختصار على سطح المكتب
7. انقر "Install" لبدء التثبيت
8. انتظر انتهاء العملية
9. انقر "Finish" (انتهى)
10. سيتم تشغيل البرنامج تلقائياً
```

#### الطريقة الثانية: ملف قابل للتشغيل (محمول)

```
1. انسخ ملف GlobalAccounting.exe إلى أي مجلد من اختيارك
2. انقر نقراً مزدوجاً على الملف لتشغيله
3. البرنامج جاهز للاستخدام فوراً
4. لا تحتاج إلى تثبيت أو خطوات إضافية
```

### التشغيل الأول

عند تشغيل البرنامج لأول مرة:
- سيتم إنشاء قاعدة البيانات تلقائياً
- ستُحفظ في: `C:\Users\[اسم المستخدم]\AppData\Local\GlobalAccounting\global.db`
- ستظهر إعدادات افتراضية
- يمكنك البدء باستخدام البرنامج مباشرة

---

## 3. الشاشة الرئيسية والتنقل

### واجهة المستخدم

```
┌─────────────────────────────────────────┐
│  Global Accounting v1.0.0               │
├─────────────────────────────────────────┤
│ [ Dashboard ] [ Invoices ] [ Inventory ]│
│ [ Payroll ] [ Reports ] [ Settings ]    │
├─────────────────────────────────────────┤
│                                         │
│        محتوى التبويب المختار            │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

### التبويبات الرئيسية

| التبويب | الوصف |
|--------|------|
| **Dashboard** | عرض ملخص ومؤشرات الأداء الرئيسية |
| **Invoices** | إنشاء وإدارة الفواتير |
| **Inventory** | إدارة المنتجات والمخزون |
| **Payroll** | حساب رواتب الموظفين |
| **Reports** | عرض وتصدير التقارير |
| **Settings** | تخصيص إعدادات البرنامج |

### التنقل بين التبويبات

```
1. ابحث عن أزرار التبويبات في أعلى النافذة
2. انقر على أي تبويب للانتقال إليه
3. سيتم عرض محتوى التبويب المختار
```

---

## 4. إدارة الفواتير (Invoices)

### ماذا تفعل هنا؟

في هذا القسم تستطيع:
- إنشاء فواتير جديدة
- إضافة المنتجات والأسعار
- حساب الضريبة تلقائياً
- معاينة الفواتير
- تصدير الفواتير كملفات CSV

### خطوات إنشاء فاتورة

```
الخطوة 1: الذهاب إلى قسم الفواتير
────────────────────────────
1. انقر على تبويب "Invoices"

الخطوة 2: إنشاء فاتورة جديدة
────────────────────────────
1. ابحث عن زر "Add Invoice" أو "Create New"
2. انقر عليه

الخطوة 3: إضافة المنتجات
────────────────────────────
1. اختر المنتج من القائمة
2. أدخل الكمية
3. أدخل سعر الوحدة
4. انقر "Add Item" لإضافة السطر

الخطوة 4: التحقق والحفظ
────────────────────────────
1. تحقق من البيانات
2. سيتم حساب الضريبة تلقائياً
3. انقر "Save" للحفظ
4. ستظهر رسالة تأكيد

الخطوة 5: المعاينة والتصدير
────────────────────────────
1. انقر "Preview" لمعاينة الفاتورة
2. انقر "Export as CSV" لتصدير الفاتورة
3. اختر موقع الحفظ
4. سيتم حفظ الفاتورة كملف Excel
```

### إضافة منتجات جديدة من هنا

إذا لم توجد المنتجات في القائمة:
```
1. انقر على "Add Product" أو أيقونة "+"
2. أدخل بيانات المنتج:
   - اسم المنتج
   - كود المنتج (اختياري)
   - سعر الوحدة
   - وصف (اختياري)
3. انقر "Save"
4. سيظهر المنتج في الفواتير القادمة
```

### حذف أو تعديل فاتورة

```
1. ابحث عن الفاتورة في القائمة
2. انقر على الفاتورة للتحديد
3. انقر على زر "Edit" (تعديل) أو "Delete" (حذف)
4. أكمل العملية
```

---

## 5. إدارة المخزون (Inventory)

### ماذا تفعل هنا؟

في هذا القسم تستطيع:
- إضافة منتجات جديدة
- تعديل بيانات المنتج
- مراقبة كميات المخزون
- تعيين الحد الأدنى للأسهم
- عرض سعر التكلفة والسعر البيعي

### خطوات إضافة منتج جديد

```
الخطوة 1: الذهاب إلى قسم المخزون
──────────────────────────────
1. انقر على تبويب "Inventory"

الخطوة 2: إضافة منتج جديد
──────────────────────────────
1. ابحث عن زر "Add Product"
2. انقر عليه

الخطوة 3: ملء بيانات المنتج
──────────────────────────────
1. اسم المنتج (مثل: "بلاستيك أزرق 5 ملم")
2. كود المنتج (مثل: "PL-001")
3. الفئة (مثل: "مواد خام")
4. وحدة القياس (مثل: "كيلو" أو "قطعة")
5. سعر التكلفة (السعر الذي اشتريت به)
6. سعر البيع (السعر الذي تبيع به)
7. الكمية الحالية
8. الحد الأدنى للأسهم (تنبيه عندما تنخفض الكمية)

الخطوة 4: الحفظ
──────────────────────────────
1. تحقق من البيانات
2. انقر "Save"
3. سيظهر المنتج في قائمة المخزون
```

### تحديث كمية المخزون

```
الطريقة 1: يدوياً
─────────────
1. ابحث عن المنتج في القائمة
2. انقر عليه
3. عدّل الكمية
4. انقر "Save"

الطريقة 2: تلقائياً
────────────────
1. عندما تنشئ فاتورة وتضيف المنتج
2. سيتم تقليل الكمية تلقائياً
3. لا تحتاج إلى تحديث يدوي
```

### البحث عن منتج

```
1. في قائمة المخزون، ابحث عن حقل البحث
2. اكتب اسم المنتج أو الكود
3. سيتم عرض المنتجات المطابقة
```

---

## 6. إدارة الرواتب (Payroll)

### ماذا تفعل هنا؟

في هذا القسم تستطيع:
- إضافة الموظفين
- تعيين الراتب والبدلات والخصومات
- حساب الراتب الشهري
- عرض سجل الرواتب
- تصدير قائمة الرواتب

### خطوات إضافة موظف

```
الخطوة 1: الذهاب إلى قسم الرواتب
──────────────────────────────
1. انقر على تبويب "Payroll"

الخطوة 2: إضافة موظف جديد
──────────────────────────────
1. ابحث عن زر "Add Employee"
2. انقر عليه

الخطوة 3: ملء بيانات الموظف
──────────────────────────────
1. الاسم الكامل (مثل: "أحمد محمد")
2. رقم الموظف (اختياري)
3. الراتب الأساسي (مثل: 3000)
4. البدلات (مثل: بدل مواصلات، بدل سكن)
5. الخصومات (مثل: ضريبة دخل، ضريبة تأمين)
6. الراتب الثابت أم بالساعة

الخطوة 4: الحفظ
──────────────────────────────
1. تحقق من البيانات
2. انقر "Save"
3. سيظهر الموظف في قائمة الرواتب
```

### حساب الراتب الشهري

```
الخطوة 1: اختيار الشهر
──────────────────────
1. حدد الشهر المطلوب من القائمة
2. أو اختر "Generate Payroll for Month"

الخطوة 2: حساب الرواتب
──────────────────────
1. انقر "Calculate" أو "Generate"
2. سيتم حساب الراتب تلقائياً:
   - الراتب الأساسي
   + البدلات
   - الخصومات
   = الراتب الصافي

الخطوة 3: المراجعة والتصدير
──────────────────────────────
1. تحقق من الرواتب المحسوبة
2. انقر "Export" لتصدير القائمة
3. سيتم حفظها كملف CSV
```

### تعديل راتب الموظف

```
1. ابحث عن الموظف في القائمة
2. انقر عليه
3. عدّل البيانات المطلوبة
4. انقر "Save"
```

---

## 7. التقارير (Reports)

### ماذا تفعل هنا؟

في هذا القسم تستطيع:
- عرض ملخص الأداء
- إحصائيات المبيعات
- تقارير المخزون
- تقارير الرواتب
- تصدير التقارير

### أنواع التقارير

```
التقرير الموجز (Summary)
───────────────────────
- إجمالي المنتجات
- إجمالي المخزون
- إجمالي الفواتير
- إجمالي المبيعات
- عدد الموظفين

تقرير المبيعات (Sales)
──────────────────────
- عدد الفواتير في الفترة
- المبيعات الإجمالية
- متوسط الفاتورة
- الضرائب المحسوبة

تقرير المخزون (Inventory)
──────────────────────────
- قيمة المخزون الإجمالية
- المنتجات التي تحتاج إعادة تموين
- المنتجات البطيئة الحركة

تقرير الرواتب (Payroll)
───────────────────────
- إجمالي الرواتب المدفوعة
- إجمالي البدلات
- إجمالي الخصومات
```

### خطوات إنشاء تقرير

```
الخطوة 1: الذهاب إلى التقارير
───────────────────────
1. انقر على تبويب "Reports"

الخطوة 2: اختيار نوع التقرير
───────────────────────
1. اختر نوع التقرير من القائمة
2. مثل: "Summary Report" أو "Sales Report"

الخطوة 3: تحديد الفترة الزمنية
──────────────────────────
1. اختر تاريخ البداية
2. اختر تاريخ النهاية
3. أو اختر خيار معرف: "This Month" (هذا الشهر)

الخطوة 4: إنشاء التقرير
──────────────────────
1. انقر "Generate Report"
2. سيتم حساب البيانات
3. سيظهر التقرير على الشاشة

الخطوة 5: التصدير
──────────────────
1. انقر "Export as CSV"
2. اختر موقع الحفظ
3. سيتم حفظ التقرير
```

### قراءة التقرير

```
التقرير يحتوي على:
────────────────
- عنوان التقرير والفترة الزمنية
- ملخص المؤشرات الرئيسية
- جداول بالبيانات المفصلة
- إجماليات وملخصات
```

---

## 8. الإعدادات (Settings)

### ماذا تفعل هنا؟

في هذا القسم تستطيع:
- تخصيص اسم الشركة
- تحديد الدولة والعملة
- ضبط رسبة الضريبة
- اختيار اللغة
- حفظ الإعدادات

### خطوات تخصيص البرنامج

```
الخطوة 1: الذهاب إلى الإعدادات
───────────────────────
1. انقر على تبويب "Settings"

الخطوة 2: تعديل بيانات الشركة
──────────────────────────
1. اسم الشركة:
   أدخل اسم شركتك الفعلي

2. الدولة:
   اختر دولة عملك من القائمة

3. العملة:
   اختر العملة (USD, SAR, AED, إلخ)

4. رسبة الضريبة:
   أدخل النسبة كرقم (مثل: 15 لـ 15%)

الخطوة 3: اختيار اللغة
──────────────────────
1. انقر على "Language"
2. اختر:
   - "en" للإنجليزية
   - "ar" للعربية

الخطوة 4: حفظ الإعدادات
──────────────────────────
1. تحقق من البيانات
2. انقر "Save"
3. ستظهر رسالة تأكيد
4. قد تحتاج إلى إعادة تشغيل البرنامج
```

### متى تتطبق الإعدادات؟

```
- اسم الشركة: يظهر في الفواتير والتقارير
- الضريبة: تُحسب في الفواتير الجديدة تلقائياً
- اللغة: تُطبق بعد إعادة تشغيل البرنامج
- العملة: تظهر في الفواتير والتقارير
```

---

## 9. استكشاف الأخطاء والحلول

### المشكلة: البرنامج لا يشتغل

**الأسباب المحتملة والحلول:**

```
السبب 1: نسخة Windows قديمة جداً
──────────────────────────
الحل:
- تأكد من استخدام Windows 7 SP1 أو أحدث
- إذا كان أقدم، يجب تحديث النظام

السبب 2: لم يتم التثبيت بشكل صحيح
──────────────────────────
الحل:
1. احذف البرنامج من Control Panel
2. أعد تشغيل الكمبيوتر
3. ثبّت البرنامج مرة أخرى

السبب 3: مشاكل في الصلاحيات
──────────────────────────
الحل:
1. انقر بالزر الأيمن على أيقونة البرنامج
2. اختر "Run as Administrator"
3. انقر "Yes" للموافقة
```

### المشكلة: البيانات لا تُحفظ

**الأسباب المحتملة والحلول:**

```
السبب 1: لا توجد مساحة على القرص الصلب
──────────────────────────
الحل:
1. افتح "My Computer"
2. انقر بالزر الأيمن على محرك C:
3. اختر "Properties"
4. تحقق من المساحة المتبقية
5. احذف الملفات غير المهمة

السبب 2: مشاكل في الصلاحيات
──────────────────────────
الحل:
1. اذهب إلى: C:\Users\[اسم المستخدم]\AppData\Local\
2. انقر بالزر الأيمن على مجلد GlobalAccounting
3. اختر "Properties" ثم "Security"
4. تأكد من وجود صلاحيات الكتابة

السبب 3: قاعدة البيانات تالفة
──────────────────────────
الحل:
1. أغلق البرنامج تماماً
2. اذهب إلى مجلد البيانات
3. احذف ملف global.db التالف
4. شغّل البرنامج - سيتم إنشاء قاعدة جديدة
```

### المشكلة: الفاتورة لا تُصدّر

**الحل:**

```
1. تأكد من اختيار موقع تصدير صحيح
2. حاول التصدير إلى سطح المكتب (Desktop)
3. تأكد من عدم فتح الملف في برنامج آخر
4. تحقق من المساحة المتبقية على القرص
5. أعد تشغيل البرنامج وحاول مرة أخرى
```

### المشكلة: اللغة لا تتغير

**الحل:**

```
1. غيّر اللغة من Settings
2. انقر Save
3. أغلق البرنامج تماماً
4. شغّل البرنامج مرة أخرى
5. ستكون اللغة قد تغيرت الآن
```

---

## 10. نصائح مهمة

### نصائح للاستخدام الفعّال

```
✓ النصيحة 1: النسخ الاحتياطية المنتظمة
──────────────────────────────
- قم بعمل نسخة احتياطية يومياً
- احفظها على جهاز خارجي أو السحابة
- لا تنسَ الملفات المهمة

✓ النصيحة 2: التدريب الأولي
──────────────────────────────
- اقرأ هذا الدليل بعناية
- مارس البرنامج على بيانات تجريبية أولاً
- ثم استخدمه للبيانات الفعلية

✓ النصيحة 3: الإعدادات الصحيحة
──────────────────────────────
- ضبط نسبة الضريبة الصحيحة
- اختيار العملة الصحيحة
- تخصيص اسم الشركة

✓ النصيحة 4: تنظيم المنتجات
──────────────────────────────
- استخدم أكواد واضحة للمنتجات
- صنّف المنتجات بفئات منطقية
- حدّث الأسعار بانتظام

✓ النصيحة 5: مراقبة المخزون
──────────────────────────────
- تحقق من الكميات منخفضة الأسهم
- عدّل الحد الأدنى حسب احتياجاتك
- لا تترك المخزون ينتهي

✓ النصيحة 6: التقارير المنتظمة
──────────────────────────────
- أنشئ تقرير شهري للمبيعات
- راجع تقرير المخزون أسبوعياً
- حلّل الأرقام واتخذ قرارات مبنية عليها

✓ النصيحة 7: الأمان
──────────────────
- احم كلمة مرور حسابك
- لا تشارك بيانات حسابك
- احذر من الملفات المشبوهة
```

### أفضل الممارسات

```
1. استخدم أسماء واضحة ومحددة
   ✓ صحيح: "بلاستيك شفاف 2 ملم"
   ✗ خطأ: "مادة"

2. حدّث البيانات بانتظام
   - أضف الفواتير يومياً
   - حدّث المخزون فوراً
   - حافظ على البيانات دقيقة

3. استخدم الأكواد الموحدة
   - اختر نظام ترميز متسق
   - استخدمه بنفس الطريقة دائماً
   - سهّل البحث عن المنتجات

4. احتفظ بسجلات محدثة
   - راجع البيانات أسبوعياً
   - اكتشف الأخطاء مبكراً
   - صحّحها فوراً

5. استخدم التقارير بذكاء
   - استخدمها لاتخاذ قرارات
   - ركّز على المؤشرات المهمة
   - خطّط بناءً على البيانات
```

---

## 11. معلومات الدعم والمساعدة

### طرق الحصول على الدعم

```
📧 البريد الإلكتروني
    support@scintec.com
    
📞 الهاتف
    [رقم الهاتف]
    ساعات العمل: من السبت إلى الخميس
    من 9 صباحاً إلى 5 مساءً
    
🌐 الموقع الإلكتروني
    www.scintec.com
    
💬 نموذج التواصل
    www.scintec.com/contact
```

### معلومات مهمة لتقديم الدعم

عند التواصل مع الدعم، أرسل:
```
1. رقم الإصدار: v1.0.0
2. نسخة Windows المثبتة
3. وصف المشكلة بالتفصيل
4. خطوات إعادة إنتاج المشكلة
5. صورة شاشة إن أمكن
6. ملف السجل (إن وجد)
```

---

## الملاحق

### الملحق أ: اختصارات لوحة المفاتيح

```
Ctrl + S      حفظ
Ctrl + N      جديد
Ctrl + P      طباعة
Ctrl + E      تصدير
F5            تحديث البيانات
Esc           إلغاء العملية
```

### الملحق ب: معاني الرموز والألوان

```
🟢 أخضر = تم بنجاح / البيانات صحيحة
🔴 أحمر = خطأ / تحذير
🟡 أصفر = تنبيه / نقص المخزون
⚪ رمادي = معطّل / غير متاح
```

### الملحق ج: المتطلبات المالية (اختياري)

```
للاستخدام الأمثل للبرنامج، ستحتاج:
- بيانات دقيقة عن المخزون
- سجل الموظفين الكامل
- الأسعار المحدثة
- البيانات التاريخية (إن وجدت)
```

---

## نهاية الدليل

**شكراً لاستخدامك Global Accounting!**

إذا كانت لديك أسئلة أو اقتراحات، لا تتردد في التواصل معنا.

**إصدار الدليل:** 1.0
**تاريخ النشر:** أكتوبر 2026
**آخر تحديث:** أكتوبر 2026

---

---

## English

---

# Complete User Guide for Global Accounting

## Table of Contents
1. Introduction to the Program
2. System Requirements and Installation
3. Main Screen and Navigation
4. Invoice Management
5. Inventory Management
6. Payroll Management
7. Reports
8. Settings
9. Troubleshooting
10. Important Tips

---

## 1. Introduction to the Program

### What is Global Accounting?

Global Accounting is a comprehensive accounting and inventory management system that simplifies the daily operations of companies and factories. The program provides easy-to-use tools for managing:
- Invoices and sales transactions
- Inventory and products
- Payroll and employees
- Reports and statistics

### Key Features

- **Complete Management:** Invoices, inventory, payroll, reports all in one place
- **Bilingual Support:** Full interface in both Arabic and English
- **Local Database:** All data is stored safely on your machine
- **Easy to Use:** Simple and intuitive interface
- **Customizable:** Full customization for your company's needs

---

## 2. System Requirements and Installation

### System Requirements

| Requirement | Minimum |
|-------------|---------|
| Operating System | Windows 7 SP1 or later |
| RAM | 256 MB |
| Storage | 100 MB |
| Screen Resolution | 1024 × 768 pixels |
| Internet | Not required |

### Installation Steps

#### Method 1: Using the Installer (Recommended)

```
1. Double-click: GlobalAccounting-Setup-1.0.0.exe
2. You may be asked to allow the program to run - Click "Yes"
3. The installation wizard window will appear
4. Read the license agreement and click "I Agree"
5. Choose installation location (Default: C:\Program Files\Global Accounting)
6. Choose if you want a desktop shortcut
7. Click "Install" to start installation
8. Wait for the process to complete
9. Click "Finish"
10. The program will launch automatically
```

#### Method 2: Portable Executable

```
1. Copy GlobalAccounting.exe to any folder
2. Double-click the file to run
3. Program is ready to use immediately
4. No installation needed
```

### First Launch

On first run:
- Database will be created automatically
- It will be stored in: `C:\Users\[username]\AppData\Local\GlobalAccounting\global.db`
- Default settings will appear
- You can start using the program right away

---

## 3. Main Screen and Navigation

### User Interface

```
┌─────────────────────────────────────────┐
│  Global Accounting v1.0.0               │
├─────────────────────────────────────────┤
│ [ Dashboard ] [ Invoices ] [ Inventory ]│
│ [ Payroll ] [ Reports ] [ Settings ]    │
├─────────────────────────────────────────┤
│                                         │
│        Content of Selected Tab          │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

### Main Tabs

| Tab | Description |
|-----|-------------|
| **Dashboard** | View summary and key performance indicators |
| **Invoices** | Create and manage invoices |
| **Inventory** | Manage products and stock |
| **Payroll** | Calculate employee salaries |
| **Reports** | View and export reports |
| **Settings** | Customize program settings |

### Navigation Between Tabs

```
1. Look for tab buttons at the top of the window
2. Click any tab to navigate to it
3. The selected tab's content will be displayed
```

---

## 4. Invoice Management

### What Can You Do Here?

In this section you can:
- Create new invoices
- Add products and prices
- Calculate tax automatically
- Preview invoices
- Export invoices as CSV files

### Steps to Create an Invoice

```
Step 1: Go to Invoices Section
────────────────────────
1. Click on "Invoices" tab

Step 2: Create New Invoice
────────────────────────
1. Look for "Add Invoice" or "Create New" button
2. Click it

Step 3: Add Products
────────────────────
1. Select product from list
2. Enter quantity
3. Enter unit price
4. Click "Add Item" to add the line

Step 4: Verify and Save
────────────────────────
1. Verify the data
2. Tax will be calculated automatically
3. Click "Save"
4. A confirmation message will appear

Step 5: Preview and Export
────────────────────────
1. Click "Preview" to see the invoice
2. Click "Export as CSV" to export
3. Choose save location
4. Invoice will be saved as Excel file
```

---

## 5. Inventory Management

### What Can You Do Here?

In this section you can:
- Add new products
- Edit product information
- Monitor inventory quantities
- Set minimum stock levels
- View cost and selling prices

### Steps to Add a New Product

```
Step 1: Go to Inventory Section
─────────────────────────
1. Click on "Inventory" tab

Step 2: Add New Product
─────────────────────
1. Look for "Add Product" button
2. Click it

Step 3: Enter Product Information
──────────────────────────────
1. Product name (e.g., "Blue plastic 5mm")
2. Product code (e.g., "PL-001")
3. Category (e.g., "Raw Materials")
4. Unit of measurement (e.g., "kg" or "piece")
5. Cost price (what you bought it for)
6. Selling price (what you sell it for)
7. Current quantity
8. Minimum stock level (alert when quantity drops)

Step 4: Save
──────────────
1. Verify data
2. Click "Save"
3. Product will appear in inventory list
```

---

## 6. Payroll Management

### What Can You Do Here?

In this section you can:
- Add employees
- Set salaries, bonuses, and deductions
- Calculate monthly payroll
- View payroll history
- Export payroll list

### Steps to Add an Employee

```
Step 1: Go to Payroll Section
────────────────────
1. Click on "Payroll" tab

Step 2: Add New Employee
────────────────────
1. Look for "Add Employee" button
2. Click it

Step 3: Enter Employee Information
──────────────────────────────
1. Full name (e.g., "Ahmed Mohammed")
2. Employee number (optional)
3. Base salary (e.g., 3000)
4. Allowances (e.g., transportation, housing)
5. Deductions (e.g., income tax, insurance)
6. Salary type (Fixed or Hourly)

Step 4: Save
──────────────
1. Verify data
2. Click "Save"
3. Employee will appear in payroll list
```

### Calculate Monthly Payroll

```
Step 1: Select Month
─────────────
1. Select desired month from list
2. Or choose "Generate Payroll for Month"

Step 2: Calculate Salaries
────────────────────
1. Click "Calculate" or "Generate"
2. Salaries will be calculated automatically:
   - Base salary
   + Allowances
   - Deductions
   = Net salary

Step 3: Review and Export
──────────────────────
1. Verify calculated salaries
2. Click "Export" to save list
3. File will be saved as CSV
```

---

## 7. Reports

### What Can You Do Here?

In this section you can:
- View performance summary
- Sales statistics
- Inventory reports
- Payroll reports
- Export reports

### Steps to Generate a Report

```
Step 1: Go to Reports
────────────
1. Click on "Reports" tab

Step 2: Select Report Type
────────────────────
1. Choose report type from list
2. e.g., "Summary Report" or "Sales Report"

Step 3: Set Time Period
──────────────────
1. Select start date
2. Select end date
3. Or choose preset option: "This Month"

Step 4: Generate Report
──────────────────
1. Click "Generate Report"
2. Data will be calculated
3. Report will appear on screen

Step 5: Export
──────────
1. Click "Export as CSV"
2. Choose save location
3. Report will be saved
```

---

## 8. Settings

### What Can You Do Here?

In this section you can:
- Customize company name
- Set country and currency
- Adjust tax rate
- Choose language
- Save settings

### Steps to Customize the Program

```
Step 1: Go to Settings
──────────────
1. Click on "Settings" tab

Step 2: Edit Company Information
───────────────────────────
1. Company Name:
   Enter your actual company name

2. Country:
   Select your country from list

3. Currency:
   Select currency (USD, SAR, AED, etc.)

4. Tax Rate:
   Enter percentage (e.g., 15 for 15%)

Step 3: Select Language
──────────────────
1. Click on "Language"
2. Choose:
   - "en" for English
   - "ar" for Arabic

Step 4: Save Settings
────────────────
1. Verify data
2. Click "Save"
3. Confirmation message will appear
4. May need to restart program
```

---

## 9. Troubleshooting

### Problem: Program Won't Start

**Possible Causes and Solutions:**

```
Cause 1: Very Old Windows Version
────────────────────────
Solution:
- Ensure you have Windows 7 SP1 or later
- If older, you need to update

Cause 2: Installation Failed
────────────────────────
Solution:
1. Uninstall program from Control Panel
2. Restart computer
3. Reinstall program

Cause 3: Permission Issues
────────────────────────
Solution:
1. Right-click on program icon
2. Select "Run as Administrator"
3. Click "Yes" to confirm
```

### Problem: Data Not Saving

**Possible Causes and Solutions:**

```
Cause 1: No Disk Space
────────────────────
Solution:
1. Open "My Computer"
2. Right-click on C: drive
3. Select "Properties"
4. Check remaining space
5. Delete unnecessary files

Cause 2: Permission Issues
────────────────────────
Solution:
1. Go to: C:\Users\[username]\AppData\Local\
2. Right-click GlobalAccounting folder
3. Select "Properties" then "Security"
4. Ensure write permissions are set

Cause 3: Corrupted Database
────────────────────────
Solution:
1. Close program completely
2. Go to data folder
3. Delete corrupted global.db file
4. Run program - new database will be created
```

---

## 10. Important Tips

### Tips for Effective Use

```
✓ Tip 1: Regular Backups
──────────────────
- Create backup daily
- Save to external device or cloud
- Don't forget important files

✓ Tip 2: Initial Training
──────────────────
- Read this guide carefully
- Practice with test data first
- Then use actual data

✓ Tip 3: Correct Settings
──────────────────
- Set correct tax rate
- Choose correct currency
- Customize company name

✓ Tip 4: Organize Products
──────────────────
- Use clear product codes
- Categorize products logically
- Update prices regularly

✓ Tip 5: Monitor Inventory
──────────────────
- Check low stock items
- Adjust minimum levels as needed
- Don't let inventory run out

✓ Tip 6: Regular Reports
──────────────────
- Create monthly sales report
- Review inventory weekly
- Analyze numbers and make decisions

✓ Tip 7: Security
──────────────────
- Protect your password
- Don't share account details
- Be careful with suspicious files
```

---

## Support Information

### Ways to Get Support

```
📧 Email
    support@scintec.com
    
📞 Phone
    [Phone Number]
    Hours: Saturday to Thursday
    9 AM to 5 PM
    
🌐 Website
    www.scintec.com
```

---

## End of Guide

**Thank you for using Global Accounting!**

If you have questions or suggestions, please contact us.

**Guide Version:** 1.0
**Published:** October 2026

---

**Document Language:** Arabic & English (العربية والإنجليزية)
**Status:** Complete and Ready for Use
