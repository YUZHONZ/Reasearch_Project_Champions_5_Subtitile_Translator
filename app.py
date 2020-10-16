from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
import stanza
import joblib
import tensorflow as tf
from nmt import nmt
import argparse

app = Flask(__name__)

stanza.download("en")
stanza.download("zh")
nlp = stanza.Pipeline(lang='en', processors='tokenize, lemma')
nlp_zh = stanza.Pipeline(lang='zh', processors='tokenize')


def english_process(sentence):
    lemm_list = []
    tocken = nlp(sentence)
    for sent in tocken.sentences:
        for word in sent.words:
            lemm_list.append(word.lemma)
    return lemm_list


def zhong_process(sentence):
    token_list = []
    tocken = nlp_zh(sentence)
    for sent in tocken.sentences:
        for word in sent.words:
            token_list.append(word.text)
    return token_list


def is_contain_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


@app.route('/')
def home():
    return render_template('homw.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Alternative Usage of Saved Model
    # joblib.dump(clf, 'NB_spam_model.pkl')
    # NB_spam_model = open('NB_spam_model.pkl','rb')
    # clf = joblib.load(NB_spam_model)
    if request.method == 'POST':
        message = request.form['message']
        data = message
    if is_contain_chinese(data) == True:
        token_list = zhong_process(data)

        with open('nmt/nmt_result/input.zh', 'w', encoding="utf-8") as f:
            f.write(' '.join([str(elem) for elem in token_list]))

        file_path = 'nmt/nmt_result/input.zh'
        src = 'zh'
        tgt = 'en'
        output_path = "./nmt/nmt_result/zh_en_result"
        model_path = "./nmt/nmt_zh_en_model"

    else:
        token_list = english_process(data)
        with open('nmt/nmt_result/input.en', 'w') as f:
            f.write(' '.join([str(elem) for elem in token_list]))

        file_path = 'nmt/nmt_result/input.en'
        src = 'en'
        tgt = 'vi'
        output_path = "./nmt/nmt_result/en_zh_result"
        model_path = "./nmt/nmt_en_zh_model"

    def predicted(file_path, output_path, model_path, src, tgt):
        add_arg = nmt.add_arguments
        nmt_parser = argparse.ArgumentParser()
        add_arg(nmt_parser)
        FLAGS, unparsed = nmt_parser.parse_known_args(
            ['--src', src, '--tgt', tgt, '--vocab_prefix', 'nmt/testdata/voc_50w', '--out_dir',
             model_path,
             '--inference_input_file', file_path, '--inference_output_file', output_path])
        default_hparams = nmt.create_hparams(FLAGS)
        train_fn = nmt.train.train
        inference_fn = nmt.inference.inference
        nmt.run_main(FLAGS, default_hparams, train_fn, inference_fn)

        with open(output_path, 'r', encoding="utf-8") as file:
            prediction = file.read().replace('\n', '')
            if is_contain_chinese(prediction) == True:
                result = str(prediction).replace(' ', '')
            else:
                result = str(prediction)
        return result

    prediction = predicted(file_path, output_path, model_path, src, tgt)
    print(prediction)
    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
