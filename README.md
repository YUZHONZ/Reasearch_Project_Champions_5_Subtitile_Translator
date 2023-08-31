## Reasearch_Project_Champions_5_Subtitile_Translator
Deliverable of UTS 32933 Research Project Autumn 2020

Supervisor: Dr. Wei liu

Group: Champion 5


### Project Goal
The goal of this project is to design a subtitle translation model between Chinese and English. The model is based on the 
GNMT which is Seq2Seq model.


### Dataset
The Dataset of the project is from the YYets which is a drama and moive subtitle websites. 

YYets Link: http://www.yyets.com/

The total number of the data we collected was 586086 for both Chinese and English. The unique words of 
Chinese words are 104854 and English words are 42220. The data can find in the nmt folder for detail.

### Data Pre-Processing
For our project, we implement data precessing on colab, the share link shows below. You can easily run the code on colab.
https://colab.research.google.com/drive/193JRvBy7Veg6N8USsomJuEb3jezuewVz?usp=sharing

### Model
The model detail can find in https://github.com/tensorflow/nmt

And the pretrained model can be found at google drive file:
https://drive.google.com/drive/folders/1_mK70MN733_GSPcHn3Qjpjh7N61-wSt7?usp=sharing

For the model traning, we trained our model on the colab pro. If you want to save the model on your google drive, you would 
better buy more storage. The code link shows below:

https://colab.research.google.com/drive/1G2QVOLej1SvtadB6kGp52W6MEkvo_N5X?usp=sharing
 
Pre-request of the model: 
* Tf 1.x
* PyTorch
* GPU base

The parameter setting of the model:

attention: scaled_luong

attention_architecture: gnmt_v2

unit_type: lstm

pass_hidden_state: true

optimizer: adam

num_train_steps: 50000

num_layers: 2

num_units: 620

Dropout	0.2

Batch_size: 64

colocate_gradients_with_ops: ture

init_op: uniform

init_weight: 0.1

forget+bias:0.1

beam_width: 10

num_buckets: 5

length_penalty_weight: 1

max_gradient_norm: 5

learning_rate: 0.0005

metrics: Bleu

### Experiments 
In order to find the better model, we setup 3 control groups.
* Law number of data VS large number of data
* With stop words dataset VS without stop words dataset
* Change branch size and learning rate 

After three experiments, we found the branch size = 80 and with stop words has a better bleu which is 18.7.

### Web Design
For the web design, we used flask to design the website. The flask is based on the local server.
* download the flask by: pip install flask

 
### Project Demo
The project Demo video:
https://youtu.be/hLBpYjhSdwo


