import os
from pathlib import Path;
from fastapi import HTTPException, status;
from dataclasses import dataclass;
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig;
from fastapi_mail.email_utils import DefaultChecker;
from model.app_schema.user_schema import UserBase;

@dataclass
class Mailer:

    env = os.environ;
    config: ConnectionConfig = ConnectionConfig(
        MAIL_USERNAME = env.get("MAIL_USERNAME"),
        MAIL_PASSWORD = env.get("MAIL_PASSWORD"),
        MAIL_FROM = env.get("MAIL_FROM"),
        MAIL_PORT = int(env.get("MAIL_PORT")),
        MAIL_SERVER = env.get("MAIL_SERVER"),
        MAIL_TLS = True,
        MAIL_SSL = False,
        # USE_CREDENTIALS = True,
        # VALIDATE_CERTS = True
        # TEMPLATE_FOLDER = Path(__file__).parent / 'views'
    )

    @classmethod
    async def sendMail(cls, email: str, body: dict=None) -> dict:
        html = """<p>Hi this test mail, thanks for using Fastapi-mail</p>""";

        message: MessageSchema = MessageSchema(subject="From Benkaf", recipients=[email], body=body, subtype="html");
        fm = FastMail(cls.config)
        await fm.send_message(message, template_name="signup_email_template.html")

        return {"message":"email sent"}