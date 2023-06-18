# config for training Quer quart conjunt de XMLs (437M)
# launch as the following


wandb_log = True
#wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-deu-433M'

# these make the total batch size be ~0.5M
# 4 batch size * 1024 block size * 32 gradaccum * 1 GPUs = 131,072  tokens/iter
# deu has 437,861,700 tokens, so 1 epoch ~= 325314 iters
#train has 433,969,971 tokens
#val has 48,200,546 tokens

batch_size = 4
block_size = 1024
gradient_accumulation_steps = 32 * 1


# this makes total number of tokens be  ~=419M   (tokens/iter*max_iters)   (131072*3200=419M)
max_iters = 3200
lr_decay_iters = 500

# eval stuff
eval_interval = 100
eval_iters = 600
log_interval = 1

# weight decay
weight_decay = 1e-1

dataset = 'deu'
out_dir = 'out-10'

#n_layer = 6
#n_head = 6
learning_rate=3e-5
#init_from = 'resume'



# 4 batch size * 4096 block size * 32 gradaccum * 1 GPUs = 524,288  tokens/iter
# deu has 867,861,700 tokens, so 1 epoch ~= 1655,3 iters

