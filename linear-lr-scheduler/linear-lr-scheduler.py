def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    LR = 0       # Learning Rate
    t  = step       # t: current step (-based)
    
    if t < warmup_steps:    # Phase 1: Warmup
        print("Phase 1")
        if warmup_steps == 0:
            print(f"warmup_steps: {warmup_steps}")
            LR = initial_lr
        else:
            LR = (t * initial_lr) / warmup_steps

    elif (t >= warmup_steps) and (t <= total_steps):      # Phase 2: Decay
        print("Phase 2")
        try:
            LR = final_lr + (initial_lr - final_lr) * ((total_steps - t) / (total_steps - warmup_steps))
        except ZeroDivisionError:
            LR = final_lr
        print(f"{t}: LR = {LR}")

    
    else: # Post-training  (t > total_steps)
        print("Phase 3")
        LR = final_lr
        print(f"{t}: LR = {LR}")

    return LR
        