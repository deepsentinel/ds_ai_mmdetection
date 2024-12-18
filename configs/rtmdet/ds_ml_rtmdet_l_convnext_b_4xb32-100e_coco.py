_base_ = './rtmdet_l_convnext_b_4xb32-100e_coco.py'

visualization = _base_.default_hooks.visualization
visualization.update(dict(draw=True, show=True))

vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='WandbVisBackend',
         init_kwargs={
            'project': 'platform-validation',
            'group': 'mock', # rtmdet-l-convnext-b-4xb16-100e
            'tags': ['rtmdet', 'convnext-l', 'batch-16', 'ds-yolov4-subsample']
         })
]
visualizer = dict(vis_backends=vis_backends)

# fp16 settings
optim_wrapper = dict(type='AmpOptimWrapper', loss_scale='dynamic')

interval = 1  # validate every 1 epoch
train_cfg = dict(val_interval=interval)
checkpoint = _base_.default_hooks.checkpoint
checkpoint.update(dict(interval=interval, max_keep_ckpts=3))

