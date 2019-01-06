<h1>Image-Colorization</h1>
<h2>Automatic Image Colorization using a Convolutional Network (U-Net)</h2>
<ul>
  <li>Using the U-Net ConvNet Architecture for end-to-end image colorization.</li>
  <li>Takes as input a grayscale 32x32 image and returns a colorized 32x32 version</li>
  <li>The model has been trained on the CIFAR-10 32x32 images for 100 epochs.</li>
  <li>The model achieved an accuracy of <strong>55.14%</strong> and a mean absolute error(MAE) of <strong>0.0464</strong> on the test set.</li> 
 </ul>
<br/>
<h2>Model Achitecture</h2>
<p>The model uses U-Net architecture which uses skip connections to preserve the lower level details and structute of an image, that are lost due to contracting bottle-neck.</p>
<p align='center'>
  <img src='UNet.png' width='800vw'><br/><em>The U-Net Architecture</em>
</p>
<br/>
<h2>Demo</h2>
<p>A web interface has been implemented, where a user uploads a grayscale image as input and gets a colored image displayed as output</p>
<p align='center'>
  <kbd><img src='demo.png' width='800vw'></kbd><br/><em>Sample Run</em>
</p>
<br/>
<h2>Requirements</h2>
<ul>
  <li>NumPy</li>
  <li>Tensorflow</li>
  <li>Keras</li>
  <li>SciPy</li>
  <li>Flask</li>
</ul>
