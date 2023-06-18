# config for training Quer quart conjunt de XMLs (432M)
# launch as the following


wandb_log = True
#wandb_log = True
wandb_project = 'owt'
wandb_run_name='gpt2-tretze-7M'

dataset = 'tretze'
out_dir = 'out-13'

# these make the total batch size be ~0.5M
# 6 batch size * 1024 block size * 16 gradaccum * 1 GPUs = 98,304  tokens/iter

#train has 7,7M tokens, so 1 epoch ~= 78 iters
#val has 48,067,861 tokens


batch_size = 6
block_size = 1024
gradient_accumulation_steps = 32 * 1
warmup_iters=100 
dropout = 0.2

# this makes total number of tokens be  ~=76M   (tokens/iter*max_iters)   (98,304*780~=76M)
max_iters = 1400
lr_decay_iters = 1200

# eval stuff
eval_interval = 100
eval_iters = 600
log_interval = 1

# weight decay
weight_decay = 1e-1

#n_layer = 6
#n_head = 6
learning_rate=3e-5
init_from = 'resume'



