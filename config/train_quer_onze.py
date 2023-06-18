# config for training Quer onze conjunt de XMLs (10M)
# launch as the following

dataset = 'onze'
out_dir = 'out-onze'
wandb_log = True
#wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-onze-10M'


# these make the total batch size be ~0.5M
# 4 batch size * 1024 block size * 32 gradaccum * 1 GPUs = 131,072  tokens/iter
# onze has 10,316,624 tokens, so 1 epoch ~= 79 iters
#train has 10,316,624 tokens
#val has 1,145,972 tokens


batch_size = 16
block_size = 256
gradient_accumulation_steps = 32 * 1


# this makes total number of tokens be  ~=130M   (tokens/iter*max_iters)   (131072*1000=130M)
max_iters = 1000
lr_decay_iters = 1000

# eval stuff
eval_interval = 100
eval_iters = 200
log_interval = 1

# weight decay
weight_decay = 1e-1


#n_layer = 6
#n_head = 6
learning_rate=3e-5
#init_from = 'resume'

warmup_iters=50 
dropout = 0.2


