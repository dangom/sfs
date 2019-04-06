"""
Compute Signal Fluctuation Sensitivity (SFS) for a NIfTI in MNI.
Assumes MNI because of brain mask and developed to (eventually) target fMRIPREP
preprocessed data.

Reports results for ROIs from the Yeo parcellation.
"""
from typing import Union

import nibabel as nib

from nilearn import image
from nilearn._utils import check_niimg_4d
from nilearn.input_data import NiftiMasker

niimg_like = Union[str, nib.nifti1.Nifti1Image]


def voxelwise_mean(img: niimg_like) -> nib.nifti1.Nifti1Image:
    """Compute the voxelwise mean of a Nifti 4D file.
    This is the numerator of the first term of the SFS expression."""
    img = check_niimg_4d(img)  # Application is idempotent.
    return image.mean_img(img)


def voxelwise_std(img: niimg_like) -> nib.nifti1.Nifti1Image:
    """Compute the standard deviation of a Nifti 4D file.
    This is the denominator of the first term of the SFS expression."""
    img = check_niimg_4d(img)
    return image.math_img("np.std(img, axis=-1)", img=img)


def global_mean_within_mni(img: niimg_like) -> float:
    """Compute the standard deviation of a Nifti 4D file.
    This is the numerator of the second term of the SFS expression."""
    masker = NiftiMasker(mask_strategy="template")
    masker.fit(img)
    masked_img = masker.transform(img)
    return masked_img.mean()


def confound_std(img: niimg_like) -> float:
    """Compute the standard deviation of a Nifti 4D file.
    This is the denominator of the second term of the SFS expression.
    In order to be completely independent of external sources, we will use
    nilearn to estimate noisy fluctuations."""
    masker = NiftiMasker(mask_strategy="template")
    masker.fit(img)
    cof = image.high_variance_confounds(img, n_confounds=1, mask_img=masker.mask_img_)
    return cof.std()


def signal_fluctuation_sensitivity(img: niimg_like) -> nib.nifti1.Nifti1Image:
    """Compute voxelwise SFS given an img in MNI space and an array containing
    a CSF confounding regressor"""
    # First term
    meanimg = voxelwise_mean(img)
    first_term = meanimg.get_data() / global_mean_within_mni(img)

    stdimg = voxelwise_std(img)
    second_term = stdimg.get_data() / confound_std(img)

    sfs = first_term * second_term
    return image.new_img_like(img, data=sfs, affine=meanimg.affine, copy_header=True)
