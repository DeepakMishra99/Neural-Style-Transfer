 <h1 id="neural-style-transfer">Neural Style Transfer</h1>
    <h2 id="overview">Overview</h2>
    <p><em>Neural Style Transfer</em> is a technique that uses deep learning to blend the <em>content</em> of one image with the <em>artistic style</em> of another image. This process allows you to apply the visual style of famous artworks to your own photos or create unique artistic renditions.</p>
    <h2 id="how-it-works">How it Works</h2>
    <ol>
    <li><strong>Content and Style Images:</strong> The algorithm takes two images as input:</li>
    <ul>
    <li><strong>Content Image:</strong> The image whose content you want to preserve.</li>
    <li><strong>Style Image:</strong> The image whose artistic style you want to transfer.</li>
    </ul>
    <li><strong>Deep Convolutional Neural Networks (CNNs):</strong> Pre-trained CNNs (like VGG) are used to extract <em>feature representations</em> from both images.</li>
    <li><strong>Feature Extraction:</strong></li>
    <ul>
    <li><strong>Content Representation:</strong> Higher-level layers of the CNN capture the <em>content</em> of the image.</li>
    <li><strong>Style Representation:</strong> <em>Gram matrices</em>, calculated from the feature maps of lower-level layers, represent the <em>style</em> of the image.</li>
    </ul>
    <li><strong>Optimization:</strong> The algorithm generates a new image by iteratively modifying its pixel values to:</li>
    <ul>
    <li>Match the <em>content representation</em> of the content image.</li>
    <li>Match the <em>style representation</em> of the style image.</li>
    </ul>
    <li><strong>Loss Functions:</strong></li>
    <ul>
    <li><strong>Content Loss:</strong> Measures how much the generated image retains the <em>content</em> of the content image.</li>
    <li><strong>Style Loss:</strong> Measures how well the generated image matches the <em>style</em> of the style image.</li>
    <li><strong>Total Loss:</strong> A weighted combination of the <em>content loss</em> and <em>style loss</em>, which the algorithm minimizes during the optimization process.</li>
    </ul>
    </ol>

<h2>🚀 How to Run the Project</h2>

<ol>
  <li>🍴 <strong>Fork</strong> the repository</li>
  <li>📦 <strong>Install required libraries</strong><br>
      🛠️ Run Command: <code>pip install -r requirements.txt</code>
  </li>
  <li>🧠 <strong>Run Streamlit App</strong><br>
      💻 Command: <code>streamlit run app.py</code>
  </li>
  <li>🖼️ <strong>Upload</strong> the <code>Content</code> and <code>Style</code> Images</li>
  <li>⏳ <strong>Wait for 4 minutes</strong></li>
  <li>🎨 <strong>Output Image</strong> will show the final result</li>
</ol>

<h2>🗂️ Project Structure</h2>

<ul>
  <li><strong>📁 Images</strong> – Folder containing project images
    <ul>
      <li>🖼️ <code>content.jpg</code> – Content Image</li>
      <li>🖌️ <code>style.jpg</code> – Style Image</li>
    </ul>
  </li>
  <li><strong>📓 Notebook</strong>
    <ul>
      <li>📘 <code>neural-style-transfer-with-tensorflow.ipynb</code> – Jupyter Notebook</li>
    </ul>
  </li>
  <li>🌐 <strong>venv</strong> – Virtual Environment</li>
  <li>📄 <strong>app.py</strong> – Main module to run the project</li>
  <li>📉 <strong>losses.py</strong> – Functions to evaluate losses</li>
  <li>🧩 <strong>model.py</strong> – VGG19 model configuration</li>
  <li>🧼 <strong>preprocessing.py</strong> – Preprocesses both images</li>
  <li>🔁 <strong>style_transfer.py</strong> – All-in-one module for processing, modeling, evaluating, and outputting the stylized image</li>
  <li>🧾 <strong>requirements.txt</strong> – Dependency file<br>
      🛠️ Run: <code>pip install -r requirements.txt</code>
  </li>
  <li>🚫 <strong>.gitignore</strong> – Files and folders to ignore in GitHub</li>
  <li>📘 <strong>README.md</strong> – This documentation file</li>
</ul>