# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os


class Config:

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.getenv("SECRET_KEY", "S#perS3crEt_007")

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = (
        f"{os.getenv('DB_ENGINE', 'postgresql')}://"
        f"{os.getenv('DB_USERNAME', 'mzelezny_baza_user')}:"
        f"{os.getenv('DB_PASS', 'rf00O9pjhuHSkjbeAcD2YbayHIEBOZ1r')}@"
        f"{os.getenv('DB_HOST', 'dpg-clogbf946foc73c6g4k0-a.frankfurt-postgres.render.com')}:"
        f"{os.getenv('DB_PORT', '5432')}/"
        f"{os.getenv('DB_NAME', 'mzelezny_baza')}"
    )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {"Production": ProductionConfig, "Debug": DebugConfig}
