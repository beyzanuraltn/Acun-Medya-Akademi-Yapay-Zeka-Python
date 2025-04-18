
# 🌳 Decision Tree ve Random Forest Algoritmaları

Makine öğrenmesinde sınıflandırma ve regresyon problemlerinde yaygın olarak kullanılan iki algoritma: **Decision Tree (Karar Ağacı)** ve **Random Forest (Rastgele Orman)**. Bu iki algoritma, özellikle yorumlanabilirlik ve doğruluk açısından sıklıkla karşılaştırılır. Bu dokümanda her iki algoritmanın temel prensipleri, avantajları ve karşılaştırmaları ele alınacaktır.

---

## 🧠 Decision Tree (Karar Ağacı)

### 📌 Tanım
Karar ağacı, verileri **ağaç yapısında** bölen denetimli bir makine öğrenimi algoritmasıdır. Düğümlerde veriler belirli özelliklere göre bölünür ve yapraklarda tahmin yapılır.


### ⚙️ Çalışma Mantığı
- En iyi özelliği seçmek için genellikle **Gini Impurity** veya **Entropy** kullanılır.
- Her bölünme, veri kümesini daha homojen alt kümelere ayırmayı hedefler.
- Ağaç yapısı **kök düğüm**, **karar düğümleri** ve **yaprak düğümlerden** oluşur.

### ✅ Avantajları
- Kolay anlaşılır ve görselleştirilebilir.
- Kategorik ve sayısal verilerle çalışabilir.
- Özellik ölçekleme gerekmez.

### ❌ Dezavantajları
- Aşırı öğrenme (overfitting) eğilimi yüksektir.
- Küçük veri değişikliklerine duyarlıdır.

### 🔍 Örnek Kullanım
```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 🌲 Random Forest (Rastgele Orman)

### 📌 Tanım
Random Forest, birçok karar ağacından oluşan **ensemble (topluluk) öğrenme yöntemidir**. Her bir ağaç rastgele veri alt kümeleriyle eğitilir ve nihai karar, tüm ağaçların oy birliğiyle veya ortalamasıyla verilir.


### ⚙️ Çalışma Mantığı
- Bootstrap yöntemi ile veri alt kümeleri oluşturulur.
- Her ağaç farklı özellik kombinasyonlarıyla eğitilir.
- Sonuçlar birleştirilerek daha doğru tahmin yapılır.

### ✅ Avantajları
- Aşırı öğrenmeyi azaltır.
- Daha doğru ve kararlı sonuçlar verir.
- Outlier’lara ve gürültüye karşı daha dayanıklıdır.

### ❌ Dezavantajları
- Eğitilmesi daha uzun sürebilir.
- Yorumlanması zordur (karar ağacı kadar anlaşılır değildir).

### 🔍 Örnek Kullanım
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## ⚖️ Karşılaştırma Tablosu

| Özellik                | Decision Tree       | Random Forest         |
|------------------------|---------------------|------------------------|
| Hızlı Eğitim           | ✅                  | ❌                    |
| Aşırı Öğrenme          | ❌ (eğilimli)        | ✅ (azaltılmış)       |
| Yorumlanabilirlik      | ✅                  | ❌                    |
| Doğruluk               | Orta                | Yüksek                |
| Gürültüye Dayanıklılık | Düşük               | Yüksek                |



## ✍️ Notlar
- Her zaman model performansını çapraz doğrulama (cross-validation) ile değerlendirin.
- Özellik önemi (feature importance) için Random Forest oldukça kullanışlıdır.
