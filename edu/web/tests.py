from django.test import TestCase
import smtplib
# Create your tests here.

try:
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login('formdeneme23@gmail.com', 'dsxi zava dqfp uwnn')
    print("Bağlantı başarılı")
    connection.quit()
except smtplib.SMTPAuthenticationError:
    print("Kimlik doğrulama hatası: Kullanıcı adı veya şifre yanlış")
except Exception as e:
    print("SMTP sunucusuna bağlanırken bir hata oluştu:", e)
