# config for training Quer quart conjunt de XMLs (175M)
# launch as the following


wandb_log = True
#wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-quart-175M-B'

# these make the total batch size be ~0.5M
# 4 batch size * 1024 block size * 32 gradaccum * 1 GPUs = 131,072  tokens/iter
batch_size = 4
block_size = 1024
gradient_accumulation_steps = 32 * 1

# quart has 174,863,759 tokens, so 1 epoch ~= 1334 iters

# this makes total number of tokens be ~=400M
max_iters = 2000
lr_decay_iters = 500

# eval stuff
eval_interval = 100
eval_iters = 600
log_interval = 1

# weight decay
weight_decay = 1e-1

dataset = 'quart'
out_dir = 'out4-B'

#n_layer = 6
#n_head = 6
learning_rate=3e-5
#init_from = 'resume'

