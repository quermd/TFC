# config for training Quer XMLs (124M) 
# launch as the following 


wandb_log = True
#wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-124M'

# these make the total batch size be ~0.5M
# 6 batch size * 1024 block size * 5 gradaccum * 1 GPUs = 30,720
batch_size = 4
block_size = 1024
gradient_accumulation_steps = 5 * 8

# this makes total number of tokens be 300B ?
max_iters = 500
lr_decay_iters = 500

# eval stuff
eval_interval = 100
eval_iters = 200
log_interval = 1

# weight decay
weight_decay = 1e-1

dataset = 'third'
out_dir = 'out4'

n_layer = 6
n_head = 6
learning_rate=0.1
#init_from = 'resume'
