import os

emailCr = os.environ['MICROSOFT_EMAIL']
passwordCr = os.environ['MICROSOFT_PASSWORD']
telegramAPI = os.environ['TELEGRAM_API']
telegramUSERID = os.environ['TELEGRAM_USERID']

credentials = dict(
    email = emailCr,
    password = passwordCr,
    telegram_api_token = telegramAPI,
    telegram_userid = telegramUSERID
)