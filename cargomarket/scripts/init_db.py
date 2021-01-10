import django
from account.models import DriverProfile, CompanyProfile, License, DrivingLicense
from advertisement.models import Advertisement #, ProductType
from django.contrib.auth.models import User
from django.conf import settings
from django.core.management import call_command

from cargomarket import settings as cargomarket_settings
from chatapp.models import Chat, Message
from datetime import date
from django.utils.timezone import localdate




def migrate():
    if not settings.configured:
        settings.configure(cargomarket_settings)
    django.setup()
    call_command("makemigrations", "account")
    call_command("makemigrations", "advertisement")
    call_command("makemigrations", "chatapp")
    call_command("migrate")


def run():
    migrate()

    # Create some dummy licenses
    patlayici = License(license_name="Patlayici Lisans", license_description="Patlayici tasiyabilir")
    patlayici.save()

    yanici = License(license_name="Yanici Lisans", license_description="Yanici tasiyabilir")
    yanici.save()

    # Create some dummy driving licenses
    b = DrivingLicense(driving_name="B", driving_description="Otomobil ve Kamyonet")
    b.save()

    c1 = DrivingLicense(driving_name="C1", driving_description="7500 kg’a Kadar Kamyon ve Çekici")
    c1.save()

    c1e = DrivingLicense(driving_name="C1E", driving_description="12000 KG’A Kadar Kamyon ve Çekici")
    c1e.save()

    c = DrivingLicense(driving_name="C", driving_description="Kamyon ve Çekici")
    c.save()
    
    d1 = DrivingLicense(driving_name="D1", driving_description="Minübüs")
    d1.save()

    # Create some dummy product Type

    #yuksek = ProductType(risk_degree=3, risk_explain='Cam, Elektronikvb. çabuk zarar görebilecek hassas ürünler.')
    #yuksek.save()

    #orta = ProductType(risk_degree=2, risk_explain='Bakliyat, Sebze, Meyve vb. çabuk iletilmesi gereken ürünler.')
    #orta.save()

    #dusuk = ProductType(risk_degree=1, risk_explain='Pamul, Metal gibi bozulmayan ve kırılma riski olmayan ürünler.')
    #dusuk.save()

    # DRIVER USER BEGIN --->>>>>>>>>
    # Create a new Driver user
    driver_user = User(is_superuser=False)
    driver_user.username = "driver"
    driver_user.set_password("zisan123")
    driver_user.email = "driver@driver.com"
    driver_user.first_name = "Driver"
    driver_user.last_name = "Surucu"
    # driver_user.date_joined = "01.01.2010"

    driver_user.save()

    # Create a new Driver profile, and associate with above driver user
    dp = DriverProfile()
    dp.phone_number = "+90212"
    dp.age="21"
    dp.gender = "Kadın"
    dp.nationality = "Türk"
    dp.experience= "4 yıl"
    dp.facebookUrl = "www.facebook.com"
    dp.websiteUrl = "www.website.com"
    dp.truck_model = "Mercedes Benz"

    dp.max_capacity = 25.8
    dp.languages= "Türkçe,İngilzce"
    dp.user = driver_user
    dp.save()
    dp.driving_licenses.add(b,c,c1e)
    dp.licenses.add(patlayici)

    # <<<<<------ DRIVER USER END

    # COMPANY USER BEGIN ---->>>>>>>
    # Create a new Company user
    company_user = User(is_superuser=False)
    company_user.username = "company"
    company_user.set_password("zisan123")
    company_user.email = "company@company.com"
    company_user.first_name = "Company"
    company_user.last_name = "Firma"

    # company_user.date_joined = "01.01.2010"
    company_user.save()

    # Create a new Company profile and associate with above company user
    cp = CompanyProfile()
    cp.phone_number = "+90555"
    cp.address = "Istanbul Maslak"
    cp.vd_no = "VD No: 3764783"
    cp.facebook = "www.facebook.com"
    cp.website = "www.website.com"
    cp.explain = "İp ve hali dokuma"
    cp.user = company_user
    cp.save()

    #Create a new Advertisement 
    adp = Advertisement()
    adp.ad_explain = 'Hızlı teslimat gerekir, cam içerir.'
    adp.from_city = 'Kahramanmaraş'
    adp.to_city = 'İzmir'
    adp.publish_date = localdate()
    adp.last_date = localdate()
    adp.total_weight = '900 Kg'
    adp.total_volume = '50 '
    adp.user = company_user
    
    adp.save()
    
    #adp.product_type.add(yuksek)
    adp.licenses.add(patlayici)
    adp.save()

    cp.age= "21"
    cp.gender = "Kadın"
    cp.address= "Onikişubat/Kahramanmaraş"
    cp.nationality = "Türk"
    cp.experience= "4 yıl"
    cp.facebook = "www.facebook.com"
    cp.save()



    # CHAT APP Example Messaging
    
    # Create a user without profile to test chatapp
    surucu_user = User()
    surucu_user.username = "surucu"
    surucu_user.set_password("zisan123")
    surucu_user.email = "surucu@surucu.com"
    surucu_user.first_name = "surucu"
    surucu_user.last_name = "App"
    surucu_user.save()

    # # CHAT 1 
    # chat_surucu_company = Chat()
    # # Before to assign users to chat, you should save
    # chat_surucu_company.save()
    # chat_surucu_company.members.add(surucu_user, company_user)
    # chat_surucu_company.save()

    # # message_from_surucu = Message()
    # # message_from_surucu.chat = chat_surucu_company
    # # message_from_surucu.sender = surucu_user
    # # message_from_surucu.message_text = "Hello I'm Surucu"
    # # message_from_surucu.save()

    # # message_from_company = Message()
    # # message_from_company.chat = chat_surucu_company
    # # message_from_company.sender = company_user
    # # message_from_company.message_text = "Hello I'm Company, Surucu"
    # # message_from_company.save()




    # CHAT 2 
    chat_driver_company = Chat()
    chat_driver_company.save()

    chat_driver_company.members.add(driver_user, company_user)
    chat_driver_company.save()

    message_from_driver = Message()
    message_from_driver.chat = chat_driver_company
    message_from_driver.sender = driver_user
    message_from_driver.message_text = "Hello I'm Driver"
    message_from_driver.save()


    message_from_company = Message()
    message_from_company.chat = chat_driver_company
    message_from_company.sender = company_user
    message_from_company.message_text = "Hello I'm Company, Driver"
    message_from_company.save()


    # README EXAMPLE QUERIES
    # Get `driver_user` and `company_user` chat
    # Chat.objects.filter(members__in=[company_user]).filter(members__in=[driver_user])

    # Get chats of `driver_user`
    # driver_user.chats.all()

    # Get 10 messages of a chat in ordered `send_time` DESC
    # Message.objects.filter(chat=chat_surucu_company).order_by('-send_time')[:10]

