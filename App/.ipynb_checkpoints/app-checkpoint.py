from flask import Flask, render_template, request
import socket
import ssl
import requests
import json
import pickle
import numpy as np
import string
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from nltk.corpus import stopwords
import nltk
import time