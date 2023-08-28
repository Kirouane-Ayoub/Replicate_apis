import replicate
import os 
os.environ["REPLICATE_API_TOKEN"] = "api_key"
destination = "" # The model to push the trained version to.
train_data = "" # json file 
train_batch_size = 4
gradient_accumulation_steps = 8
num_train_epochs = 50
warmup_ratio=0.03
version="a16z-infra/llama-2-7b-chat:4f0b260b6a13eb53a6b1891f089d57c08f41003ae79458be5011303d81a394dc"# {username}/{model}:{version}
def train(destination , train_data , train_batch_size , gradient_accumulation_steps , num_train_epochs , warmup_ratio) : 
    training = replicate.trainings.create(
    version=version,
    input={
        "train_data":train_data,
        "train_batch_size" : train_batch_size ,
        "gradient_accumulation_steps" : gradient_accumulation_steps , 
        "num_train_epochs" : num_train_epochs , 
        "warmup_ratio" : warmup_ratio 
    },
    destination=destination
    )
    return training
