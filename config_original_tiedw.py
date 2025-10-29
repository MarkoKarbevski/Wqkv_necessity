model_args = {
    "block_size": 1024,
    "vocab_size": 50304,
    "n_layer": 12,
    "num_heads": 12,
    "n_embd": 768,
    "tie_weights": True,
    "head_size": 64,
    "dropout": 0.0,
    "batch_size": 12,
    "accumulation_size": 30,
    "bias": False,
    "use_query_weights": True,
    "learning_rate": 6e-4,
    "weight_decay": 1e-1,
    "beta1": 0.9,
    "beta2": 0.95,
    "grad_clip": 1.0,  # clip gradients at this value, or disable if == 0.0
    "decay_lr": True,  # whether to decay the learning rate
    "warmup_iters": 2000,  # how many steps to warm up for
    "lr_decay_iters": 600000,  # should be ~= max_iters per Chinchilla
    "min_lr": 6e-5
}
