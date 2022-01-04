from rest_framework.serializers import ModelSerializer
from accounts.models import User, ControleOTP
import random
import string
import smtplib
import email.message


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =  ["id", "username", "email", "codigo", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        
        try: 
            email_verificacao = ControleOTP.objects.get(email=validated_data["email"])
            if email_verificacao.codigo == validated_data["codigo"]:
                user = User.objects.create_user(
                    username=validated_data["username"],
                    password=validated_data["password"],
                    email=validated_data["email"],
                    codigo=validated_data["codigo"]
                )
                return user

        except:
            return

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

class OTPSerializer(ModelSerializer):
    class Meta:
        model = ControleOTP
        fields = ["id", "email"]

    def create(self, validated_data):
        codigo = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(6))
        body_email = f"""
        <div class="inner" style='background-color: white'><h3 id="text23" style='text-transform: uppercase; color: #FFFFFF;font-family: 'Sora', sans-serif;letter-spacing: 0.1rem; width: calc(100% + 0.1rem);font-size: 1em; line-height: 1.625; font-weight: 600;'>Código de Verificação</h3><h1 id="text24" style='color: white;font-family: 'Sora', sans-serif;letter-spacing: 0.025rem; width: calc(100% + 0.025rem);font-size: 4.375em;    line-height: 1.25; font-weight: 700;'>{codigo}</h1><p id="text18" style='color: white; font-family: 'Inter',sans-serif; font-size: 1.375em; line-height: 1.75; font-weight: 400;'>Yoo, jás aqui o código de verificação para cadastrar em minha API, bom proveito!</p><ul id="buttons01" class="buttons"><li></div>
        """
        msg = email.message.Message()
        msg["Subject"] = "Código de Verificão"
        msg["From"] = "testespython281@gmail.com"
        msg["To"] = validated_data["email"]
        password = "testespython1"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(body_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode('utf-8'))

        otp = ControleOTP.objects.create(
            email=validated_data["email"],
            codigo=codigo
        )
        
        return otp