============================
Digital Image Focus Stacking
============================

A digital image processing technique which combines multiple images taken
at different focus distances to give a resulting image with a greater depth of
field (DOF) than any of the individual source images.


Problem To Solve
================

When macro photography, the short depth of field (DOF) makes clear image only
in a small area because of very short distance to subject. **To get a clear
(focused) image in a wide range**, the photographer can shrink and use small
aperture size. But shrinking aperture size has two side effects as follow:

1. Increase diffraction effect that causes image blurry
2. Decrease exposure energy that makes noise relatively increase

So there are limits to get a clear photo by just shrinking aperture with one
shot. Here are three photos to show the effect of aperture size.

+-------------------------------------+-------------------------------------+------------------------------------+
| .. image:: wiki/Dof_blocks_f1_4.jpg | .. image:: wiki/Dof_blocks_f4_0.jpg | .. image:: wiki/Dof_blocks_f22.jpg |
| Aperture=f/1.4, DOF=0.8cm           | Aperture=f/4.0, DOF=2.2cm           | Aperture=f/22, DOF=12.4cm          |
+-------------------------------------+-------------------------------------+------------------------------------+

\:information_source: Source: https://en.wikipedia.org/wiki/Depth_of_field

Definition of depth of field (DOF)
__________________________________

.. image:: ./img/DOF_equation.png

+--------+----------------------+--------------------------------+
| Symbol | Definition           | Example                        |
+========+======================+================================+
| c      | circle of confusion  | Canon APS-C camera CoC=0.018mm |
+--------+----------------------+--------------------------------+
| f      |  focal length        | EF100mm f/2.8L MACRO IS USM    |
+--------+----------------------+--------------------------------+
| N      |  f-number            | f/2.8, f/4, f/10, f/16         |
+--------+----------------------+--------------------------------+
| u      |  distance to subject | 5cm ~ 20cm for Camera          |
+--------+----------------------+--------------------------------+

For example: A Canon APS-C camera with conditions in previous table and assume 
N=10, u=20cm=200mm, this will result:

**DOF = 1.44mm**

The value of DOF=1.44mm is too small to get a clear image for object. Here is an
example:

+-------------------------------+-------------------------------+
| .. image:: ../images/fly1.jpg | .. image:: ../images/fly2.jpg |
+-------------------------------+-------------------------------+

\:information_source: Source: https://en.wikipedia.org/wiki/Focus_stacking


Algorithm
=========

Edge detection
______________

Pixel values change fast (sharp) in the focused area. Pixel values chage gentlely
(soft) in the defocused aread. The sharp aread consider as edge that pixel value
varies fast. Follow steps aim to find the edges in a photo.

1. Perform a **Gaussian blur** on image with following kernel:

   ::

      (sigma=1)
      0.0585 0.0965 0.0585
      0.0965 0.1591 0.0965
      0.0585 0.0965 0.0585

   Using ``skimage.filters.gaussian()`` to filter "fly.jpg" image. 
   `:eyes: View Python source :eyes: <https://github.com/TommyLin/focus-stacking/blob/master/src/gaussian_blur.py>`_

   +-------------------------------+-------------------------------------+-------------------------------------+
   | .. image:: ../images/fly1.jpg | .. image:: ../images/fly1_blur1.jpg | .. image:: ../images/fly1_blur2.jpg |
   | Original                      | sigma=1                             | sigma=2                             |
   +-------------------------------+-------------------------------------+-------------------------------------+

2. Perform a **Laplacian Edge Detection kernel** on Gaussian Blurred image:

   ::

      -1 -1 -1
      -1  8 -1
      -1 -1 -1

   Using ``skimage.filters.sobel()`` to filter "fly.jpg" image. 
   `:eyes: View Python source :eyes: <https://github.com/TommyLin/focus-stacking/blob/master/src/edge_detect.py>`_

   +------------------------------------+-------------------------------------+-------------------------------------+
   | .. image:: ../images/fly1_edge.jpg | .. image:: ../images/fly1_edge1.jpg | .. image:: ../images/fly1_edge2.jpg |
   +------------------------------------+-------------------------------------+-------------------------------------+

3. Take absolute value of Laplacian of Gaussian (LoG) result. This will quantify
   the strength of edges with respect to the size and strength of kernel.
4. Create a blank image, loop through each pixel and find the strongest edge in
   the LoG(i.e. the highest value in the image stack) and take the RGB value for
   that pixel from the corresponding image.

:star::star::star: Deep Learning :star::star::star:
___________________________________________________

The idea of filter image with **KERNEL** is basic of deep learning neural network.

Structural Similarity Index Measure (SSIM)
__________________________________________

The structural similarity index measure (SSIM) is a method for predicting the
perceived quality of digital television and cinematic pictures, as well as other
kinds of digital images and videos. SSIM is used for measuring the similarity
between two images.

.. image:: https://wikimedia.org/api/rest_v1/media/math/render/svg/1783c17346b8f4c822ed206798bb6769a845c417

The resultant SSIM index is a decimal value between -1 and 1, and value 1 is
only reachable in the case of two identical sets of data and therefore indicates
perfect structural similarity. A value of 0 indicates no structural similarity.

Prospective Users
=================

Macro photography or optical microscopy users who wants to take a clear image.
They must have equipment to take multiple digital photos. This project could
help to stack photos took with stepped focus distances.

1. [Service] firmware update - Install "Magic Lantern" plug-in to camera.
2. [Software] Automatic focus stacking software


System Architecture
===================

**Image capture** (hardware control)
____________________________

1. Control from host (PC)

   [Camera] --- PTP ---- [Host] [#]_

   Host "**command**" [#]_ camera to shoot photos with fixed focal distances.

   (NOT included in this project)

   .. [#] Host could be a PC or an embedded system such as Raspberry PI board.
   .. [#] This can be achived by using `Canon's EOS Digital Camera SDK(EDSDK) <https://www.codeproject.com/articles/688276/canon-edsdk-tutorial-in-csharp>`_ or `Canon’s Camera Control API(CCAPI) <https://www.canonbody.com/canon-usa-introduction-to-canons-camera-control-api-with-canon-developer-community/>`_.

       .. image:: ./img/Canon-EDSDK.jpg
       .. image:: ./img/Canon-CCAPI.png

2. Control from camera itself

   * `Magic lantern <https://magiclantern.fm/>`_
      .. image:: ./img/MagicLantern.png

**Focus stacking** (software)
_____________________________

[**Scan for images**] ==> [**Grouping**] ==> [**Edge detect**] ==> [*Alignment* [#]_] ==> [*White Balance*] ==> [**Focus stacking**]

.. [#] Alignment and white balance are not included in this project. Tested images are created and always aligned and white balanced.

Engineering Infrastructure
==========================

Algorism Performance Evaluation
_______________________________

To evaluate the algorism performance in this project, testing images are created 
from a source image(focused). This also prevent alignment procedure to do focus
stacking. Here is the steps to evaluate algorism performance.

1. Get a clear and focused source image (image1)
2. Smooth souce image with a set of mask by Gaussian blur kernel
3. Through the focus stacking to combine these blurred images into image2
4. Calculate SSIM of image1 and image2 to tell the performance of focus stacking algorism.

Coding Style Check
__________________

checkpatch.pl

::

    $ $(kernel)/scripts/checkpatch.pl -f source.cpp

Static Analysis Tool
____________________

`cppcheck -- A static analysis tool for C/C++ code <http://cppcheck.sourceforge.net/>`_



::

    $ cppcheck .

Source Code Coverage Analysis
_____________________________

Source code coverage analysis here is used to check unit test coverage of whole source code. There are two cases concerned as follow:

* Improve testing procedure coverage, if there was source code not covered by testing.
* Remove redundant code, if there was no condition could cover or test it.

`gcov -- a Test Coverage Program <https://gcc.gnu.org/onlinedocs/gcc/Gcov.html>`_

`LCOV - the LTP GCOV extension <http://ltp.sourceforge.net/coverage/lcov.php>`_

Steps to create code coverage information:

1. Enable coverage testing the program and compiled with the following options:

   ``$ gcc -Wall -fprofile-arcs -ftest-coverage cov.c``

2. Running test

   ``$ python3 -m pytest -v``
   (This will create \*.gcov)

3. Generate html formate report from \*.gcov

   ``$ make lcov``

   Makefile

   ::

      TARGET = _vector
      lcov:
           lcov --capture --directory . --output-file $(TARGET).info --test-name $(TARGET)
           genhtml $(TARGET).info --output-directory output --title "$(TARGET)" --show-details --legend

4. Browse result at ``./output/index.html`` with browser.

 `Example: CPP source code coverage of HW2 <https://github.com/TommyLin/focus-stacking/blob/master/doc/lcov/index.html>`_

Estimated Computations
======================

Conditions:

* Image size: 5184x3456 (RGB)
* Kernel size: 3x3
* Gaussian / Laplacian filtering => x2

For the focus stacking part:

5184 x 3456 x 3 x (3 x 3) x 2 multiplications and additions per image

Then multiply with how many photos in the directory to stack.

For the SSIM part:

5184 x 3456 x 3 x (9 multiplication , 1 division, 6 addition)

Assume there are 4 photos in directory. To determinate the relationship of each other, above SSIM calculation needs to multiply with (4 x 3 / 2) = 6.



Schedule
========

Original

* Week 1: [Python] Generate defocused photos (Gaussian blur)
* Week 2: [C++] Evaluate SSIM of two photos
* Week 3: Github CI
* Week 4: [Python] Setup testing environment
* Week 5: [Python] Browse directory and read image
* Week 6: [C++] Gaussian blur & Laplacian edge detection
* Week 7: [C++] Image stacking
* Week 8: [Python/C++] Debug and optimization


Then become

* Week 1: |50%| 11/02 [Python] Generate defocused photos (Gaussian blur)
* Week 2: |100%| 11/09 [C++] Evaluate SSIM of two photos  => :dart: `[Performance Index] <https://github.com/TommyLin/focus-stacking/milestone/5>`_
* Week 3: |100%| 11/16 Github CI => :dart: `[Github Actions implementation] <https://github.com/TommyLin/focus-stacking/milestone/2>`_ / :dart: `[Try Github functions] <https://github.com/TommyLin/focus-stacking/milestone/3>`_
* Week 4: |100%| 11/23 [Python] Setup testing environment
* Week 5: |50%| 11/30 [Python] Browse directory and read image
* Week 6: |30%| 12/07 [C++] Gaussian blur & Laplacian edge detection => :dart: `[C++ implementation and acceleration] <https://github.com/TommyLin/focus-stacking/milestone/4>`_
* Week 7: |0%| 12/14 [C++] Image stacking => :dart: `[Functions implemented by Python] <https://github.com/TommyLin/focus-stacking/milestone/1>`_
* Week 8: |0%| 12/21 [Python/C++] Debug and optimization
* |0%| 12/28 Term project presentation 1
* |0%| 01/04 **Term project presentation 2** (V)
* |0%| 01/11 No meeting (optional lecture is not planned)

.. |0%| image:: https://progress-bar.dev/0
.. |10%| image:: https://progress-bar.dev/10
.. |20%| image:: https://progress-bar.dev/20
.. |30%| image:: https://progress-bar.dev/30
.. |40%| image:: https://progress-bar.dev/40
.. |50%| image:: https://progress-bar.dev/50
.. |60%| image:: https://progress-bar.dev/60
.. |70%| image:: https://progress-bar.dev/70
.. |80%| image:: https://progress-bar.dev/80
.. |90%| image:: https://progress-bar.dev/90
.. |100%| image:: https://progress-bar.dev/100


Scrum
=====

The Scrum Team consists of three roles:

.. image:: ./img/scrum_team.png

Source: `Equality - The Roles in Scrum <https://www.scrum.org/resources/blog/equality-roles-scrum>`_

Target: (for Product Owner)

1. Automatic photo system with super DOF.
2. This term project.


References
==========

1. https://en.wikipedia.org/wiki/Focus_stacking
2. https://en.wikipedia.org/wiki/Depth_of_field
3. https://en.wikipedia.org/wiki/Circle_of_confusion
4. https://en.wikipedia.org/wiki/Structural_similarity
5. `Scrum的三大主要角色 <https://www.projectup.net/article/view/id/7032>`_
