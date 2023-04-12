import sys

if __name__ == '__main__':
    hyp_set = int(sys.argv[1])

    if hyp_set == 1:
        with open('hyp_template_1.yaml', 'r') as f:
            text = f.read()
    
            thresholds = [0.2, 0.3, 0.4]
            learning_rates = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1]

            for i in range(len(thresholds)):
                for j in range(len(learning_rates)):
                    pre = f'# YOLOv5 by Ultralytics, GPL-3.0 license\n\niou_t: {thresholds[i]}  # IoU training threshold\nlr0: {learning_rates[j]}  # initial learning rate (SGD=1E-2, Adam=1E-3)\n\n'
                    new_f = open(f'hyps\hyp_{i}_{j}.yaml', 'w')
                    new_f.write(pre + text)
                    new_f.close()
    if hyp_set == 2:
        with open('hyp_template_2.yaml', 'r') as f:
            text = f.read()
    
            learning_rates = [0.001, 0.002, 0.005, 0.01, 0.02]
            box_losses = [0.05, 0.1, 0.15, 0.2]
            cls_losses = [0.3, 0.4, 0.5, 0.6, 0.7]
            obj_losses =  [0.6, 0.7, 0.8, 0.9, 1.0]

            for i in range(len(learning_rates)):
                for j in range(len(box_losses)):
                    for k in range(len(cls_losses)):
                        for l in range(len(obj_losses)):
                            pre = f'# YOLOv5 by Ultralytics, GPL-3.0 license\n\nlr0: {learning_rates[i]}  # initial learning rate (SGD=1E-2, Adam=1E-3)\nbox: {box_losses[j]}  # box loss gain\ncls: {cls_losses[k]}  # cls loss gain\nobj: {obj_losses[l]}  # obj loss gain (scale with pixels)\n\n'
                            new_f = open(f'hyps\hyp_0_{i}_{j}_{k}_{l}.yaml', 'w')
                            new_f.write(pre + text)
                            new_f.close()
    