# config for training Quer quart conjunt de XMLs (432M)
# launch as the following


wandb_log = True
#wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-dotze-432M'

dataset = 'dotze'
out_dir = 'out-12'

# these make the total batch size be ~0.5M
# 4 batch size * 1024 block size * 32 gradaccum * 1 GPUs = 131,072  tokens/iter


# 3 batch size * 2048 block size * 32 gradaccum * 1 GPUs = 196,608  tokens/iter
#train has 432,754,089 tokens, so 1 epoch ~= 2197 iters
#val has 48,067,861 tokens


batch_size = 4
block_size = 1024
gradient_accumulation_steps = 32 * 1
warmup_iters=400 
dropout = 0.2

# this makes total number of tokens be  ~=865M   (tokens/iter*max_iters)   (131072*3200=865.075.200 )
max_iters = 3200
lr_decay_iters = 2000

# eval stuff
eval_interval = 100
eval_iters = 600
log_interval = 1

# weight decay
weight_decay = 1e-1

#n_layer = 6
#n_head = 6
learning_rate=3e-5
#init_from = 'resume'



