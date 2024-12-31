
transform turn_norcol:
    ease 0.2 matrixcolor IdentityMatrix()

transform turn_dark:
    ease 0.2 matrixcolor SaturationMatrix(0.4) * BrightnessMatrix(-0.2)