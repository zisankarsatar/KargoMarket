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

    diger = License(license_name="Diğer Lisanslar", license_description="Herhangi lisans")
    diger.save()

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

    # DRIVER USER BEGIN --->>>>>>>>>
    # Create a new Driver user
    driver_user = User(is_superuser=False)
    driver_user.username = "zisankarsatar"
    driver_user.set_password("zisan123")
    driver_user.email = "driver@driver.com"
    driver_user.first_name = "Zişan"
    driver_user.last_name = "Karsatar"
    driver_user.date_joined = localdate()

    driver_user.save()

    # Create a new Driver profile, and associate with above driver user
    dp = DriverProfile()
    dp.phone_number = "+9053412556"
    dp.facebookUrl = "www.facebook.com"
    dp.websiteUrl = "www.website.com"
    dp.age="21"
    dp.nationality = "Türk"
    dp.experience= "4 yıl"
    
    dp.truck_model = "Mercedes Benz"
    dp.truck_brand = "Mercedes"
    dp.truck_fuel = "Dizel"
    dp.truck_gear = "8+1"
    dp.max_capacity = 25.8
    dp.languages= "Türkçe,İngilzce"
    dp.profile_pic="https://images.unsplash.com/photo-1558898479-33c0057a5d12?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"
    dp.user = driver_user
    dp.save()
    dp.driving_licenses.add(b,c,c1e)
    dp.licenses.add(patlayici)

    # Create a new Driver user
    driver_user2 = User(is_superuser=False)
    driver_user2.username = "dursunyılmaz"
    driver_user2.set_password("zisan123")
    driver_user2.email = "dursun@yilmaz.com"
    driver_user2.first_name = "Dursun"
    driver_user2.last_name = "Yılmaz"
    driver_user2.date_joined = localdate()

    driver_user2.save()

    # Create a new Driver profile, and associate with above driver user
    dp2 = DriverProfile()
    dp2.phone_number = "+9053221263"
    dp2.facebookUrl = "www.facebook.com"
    dp2.websiteUrl = "www.website.com"
    dp2.age="47"
    dp2.nationality = "Türk"
    dp2.experience= "10 yıl"
    
    dp2.truck_model = "Mercedes Benz"
    dp2.truck_brand = "Mercedes"
    dp2.truck_fuel = "Dizel"
    dp2.truck_gear = "8+1"
    dp2.max_capacity = 25.8
    dp2.languages= "Türkçe,İngilzce, İspanyolca"
    dp2.profile_pic="https://images.unsplash.com/photo-1557862921-37829c790f19?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1051&q=80"
    dp2.user = driver_user2
    dp2.save()
    dp2.driving_licenses.add(b,c,c1e)
    dp2.licenses.add(patlayici)

     # Create a new Driver user
    driver_user3 = User(is_superuser=False)
    driver_user3.username = "kamurantasci"
    driver_user3.set_password("zisan123")
    driver_user3.email = "kamuran@tasci.com"
    driver_user3.first_name = "Kamuran"
    driver_user3.last_name = "Taşçı"
    driver_user3.date_joined = localdate()

    driver_user3.save()

    # Create a new Driver profile, and associate with above driver user
    dp3 = DriverProfile()
    dp3.phone_number = "+9053244263"
    dp3.facebookUrl = "www.facebook.com"
    dp3.websiteUrl = "www.website.com"
    dp3.age="37"
    dp3.nationality = "Türk"
    dp3.experience= "7 yıl"
    
    dp3.truck_model = "Mercedes Benz"
    dp3.truck_brand = "Mercedes"
    dp3.truck_fuel = "Dizel"
    dp3.truck_gear = "8+1"
    dp3.max_capacity = 25.8
    dp3.languages= "Türkçe,İspanyolca"
    dp3.profile_pic="https://images.unsplash.com/photo-1528763380143-65b3ac89a3ff?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=635&q=80"
    dp3.user = driver_user3
    dp3.save()
    dp3.driving_licenses.add(b,c,c1e)
    dp3.licenses.add(patlayici, diger)

     # Create a new Driver user
    driver_user4 = User(is_superuser=False)
    driver_user4.username = "Asya Yaren"
    driver_user4.set_password("zisan123")
    driver_user4.email = "asya@yaren.com"
    driver_user4.first_name = "Asya"
    driver_user4.last_name = "Yaren"
    driver_user4.date_joined = localdate()

    driver_user4.save()

    # Create a new Driver profile, and associate with above driver user
    dp4 = DriverProfile()
    dp4.phone_number = "+9053221263"
    dp4.facebookUrl = "www.facebook.com"
    dp4.websiteUrl = "www.website.com"
    dp4.age="57"
    dp4.nationality = "Türk"
    dp4.experience= "25 yıl"
    
    dp4.truck_model = "Mercedes Benz"
    dp4.truck_brand = "Mercedes"
    dp4.truck_fuel = "Dizel"
    dp4.truck_gear = "8+1"
    dp4.max_capacity = 25.8
    dp4.languages= "Türkçe,İspanyolca"
    dp4.profile_pic="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80"
    dp4.user = driver_user4
    dp4.save()
    dp4.driving_licenses.add(b,c,c1e)
    dp4.licenses.add(patlayici, diger)

    # <<<<<------ DRIVER USER END

    # COMPANY USER BEGIN ---->>>>>>>
    # Create a new Company user
    company_user = User(is_superuser=False)
    company_user.username = "deryamelek"
    company_user.set_password("zisan123")
    company_user.email = "company@company.com"
    company_user.first_name = "Derya"
    company_user.last_name = "Melek"
    company_user.date_joined = localdate()
    company_user.save()

    # Create a new Company profile and associate with above company user
    cp = CompanyProfile()
    cp.phone_number = "+90555"
    cp.address = "Istanbul Maslak"
    cp.vd_no = "3764783"
    cp.facebookUrl = "www.facebook.com"
    cp.websiteUrl = "www.website.com"
    cp.explain = "ikinci El ürünleri uygun fiyatta pazarlama"
    cp.picture = "https://images.unsplash.com/photo-1592486694952-da117c1dad0f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=967&q=80"
    cp.user = company_user
    cp.save()
    
    #Create a new Advertisement 
    adp = Advertisement()
    adp.ad_title = 'Cam'
    adp.ad_explain = 'Hızlı teslimat gerekir, cam içerir.'
    adp.from_city = 'Kahramanmaraş'
    adp.to_city = 'İzmir'
    adp.publish_date = localdate()
    adp.last_date = localdate()
    adp.total_weight = '900 Kg'
    adp.total_volume = '50 '
    adp.ad_show = '5'
    adp.img = 'https://images.unsplash.com/photo-1469981283837-561b3779462f?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
    adp.user = company_user
    
    adp.save()
    
    adp.licenses.add(diger)
    adp.save()

    #Create a new Advertisement 
    adp2 = Advertisement()
    adp2.ad_title = 'Demir'
    adp2.ad_explain = 'Ham madde taşınması, Ağır metal içerir.'
    adp2.from_city = 'İstanbul'
    adp2.to_city = 'İzmir'
    adp2.publish_date = localdate()
    adp2.last_date = localdate()
    adp2.total_weight = '900 Kg'
    adp2.total_volume = '50 '
    adp2.img = "https://images.unsplash.com/photo-1523027737707-96c0e1fd54e4?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=967&q=80"
    adp2.user = company_user
    
    adp2.save()
    
    adp2.licenses.add(patlayici)
    adp2.save()

# Create a new Company user
    company_user2 = User(is_superuser=False)
    company_user2.username = "sahanlarahsap"
    company_user2.set_password("zisan123")
    company_user2.email = "company2@company2.com"
    company_user2.first_name = "Şahin"
    company_user2.last_name = "Yavuz"
    company_user2.date_joined = localdate()
    company_user2.save()

    # Create a new Company profile and associate with above company user
    cp2 = CompanyProfile()
    cp2.phone_number = "+90555"
    cp2.address = "Konya Ereğli"
    cp2.vd_no = "3764783"
    cp2.facebookUrl = "www.facebook.com"
    cp2.websiteUrl = "www.website.com"
    cp2.explain = "Konsol, sandık yapılır."
    cp2.picture = "https://images.unsplash.com/photo-1577670772839-befb49f0bee5?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1051&q=80"
    cp2.user = company_user2
    cp2.save()
    
    #Create a new Advertisement 
    adp3 = Advertisement()
    adp3.ad_title = 'Sandık'
    adp3.ad_explain = 'ürün deformasyonu yaşanmaması için özenle paketlenmeli.'
    adp3.from_city = 'Diyarbakır'
    adp3.to_city = 'Muğla'
    adp3.publish_date = localdate()
    adp3.last_date = localdate()
    adp3.total_weight = '900 Kg'
    adp3.total_volume = '50 '
    adp3.ad_show = '5'
    adp3.img = 'https://images.unsplash.com/photo-1588982775664-556d8f975938?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
    adp3.user = company_user2

    adp3.save()
    adp3.licenses.add(diger)
    adp3.save()

    #Create a new Advertisement 
    adp4 = Advertisement()
    adp4.ad_title = 'Sokak saksılar'
    adp4.ad_explain = 'Sokaklara konulacağı için belediyeye teslim edilmeli.'
    adp4.from_city = 'Şanlıurfa'
    adp4.to_city = 'Van'
    adp4.publish_date = localdate()
    adp4.last_date = localdate()
    adp4.total_weight = '900 Kg'
    adp4.total_volume = '50 '
    adp4.img = "https://images.unsplash.com/photo-1576511518925-6f97cdc28145?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80"
    adp4.user = company_user2

    adp4.save()
    adp4.licenses.add(diger)
    adp4.save()


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

