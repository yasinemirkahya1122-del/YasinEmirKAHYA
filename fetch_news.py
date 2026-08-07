import os
import json
import google.generativeai as genai

# API anahtarını ortam değişkeninden alır
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Gemini Flash 1.5 Kullanımı
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
Bugünün en önemli global ve yerel 3 teknoloji haberini özetle.
Çıktıyı SADECE geçerli bir JSON formatında ver. Ekstra açıklama veya markdown backtick (```) ekleme.

İstediğim JSON Yapısı:
{
  "title": "Günlük Teknoloji Haberleri",
  "articles": [
    {"headline": "Haber Başlığı 1", "content": "Detaylı haber metni..."},
    {"headline": "Haber Başlığı 2", "content": "Detaylı haber metni..."},
    {"headline": "Haber Başlığı 3", "content": "Detaylı haber metni..."}
  ],
  "sources": "Örn: TechCrunch, Verge, Anadolu Ajansı",
  "author": "Yasin Emir KAHYA"
}
"""

try:
    response = model.generate_content(prompt)
    clean_text = response.text.replace("```json", "").replace("```", "").strip()
    data = json.loads(clean_text)
    
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Haberler başarıyla news.json dosyasına yazıldı.")
except Exception as e:
    print(f"Hata oluştu: {e}")
