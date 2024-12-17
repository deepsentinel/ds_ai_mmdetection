_base_ = './rtmdet_l_convnext_b_4xb32-100e_coco.py'

default_hooks = dict(visualization=dict(type='DetVisualizationHook', draw=True))

vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='WandbVisBackend',
         init_kwargs={
            'project': 'mmdetection',
            'group': 'rtmdet-l-convnext-b-4xb32-100e-coco'
         })
]
visualizer = dict(vis_backends=vis_backends)
