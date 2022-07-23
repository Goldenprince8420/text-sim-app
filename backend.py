#importing flask
from flask import Flask, render_template,request
#Importing the summarizer
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer