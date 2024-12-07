# 1. Information
- Using AI Support doctor predict skin fungus (8 Categorical)
- Using skills about image data processing and Computer Vision
- Open-source (For free)
- Data about 9756 images (collect from book and google image)
- Release date: September 2019
- My role: AI Intern

# 2. Development Version 

## 2.1. About data


| Categories | Code | Number of image| Illustration |
|------------|------|:------------:|---------|
| Pityriasis versicolor | PVS | 488 | ![PVS]()|
| Folliculitis | PFL | 400 | ![PFL]()|
| Seborrhoeic dermatitis and dandruff | SBD | 430 | ![SBD]()|
| Tinea nigra | TIN | 257 | ![TIN]()|
| White piedra | WPD | 98 | ![WPD]()|
| Tinea | TIB, TIP, TIU, TIC | 3318 | ![TI]()|
| Candidiasis |	CAO, CAV, CAB, CAS, CAN | 4321 | ![CA]()|
| Subcutaneous | SUB | 444 | ![SUB]()|
| Total |  | 9756 | |

**Data Preprocessing**

- Using Data Augmentation by ImageDataGenerator:
- Split data: 0.1 validation data, 0.7 training data and 0.2 testing data
- Resize image: 150x150x3

## 2.2. Model Development

### 2.2.1. [Resnet50](https://keras.io/api/applications/resnet/)

- Pretrain model: [Resnet50](https://keras.io/api/applications/resnet/)
- Training weight: Imagenet
- Optimizer: RMS with learning rate $1\times10^-4$
- Epoch: 30
- Loss: Categorical crossentropy

![image_struct_resnet50](https://miro.medium.com/v2/resize:fit:4800/format:webp/0*tH9evuOFqk8F41FG.png)

## 2.2.2 [InceptionV3](https://keras.io/api/applications/inceptionv3/)

### Model Development

- Pretrain model: [InceptionV3](https://keras.io/api/applications/inceptionv3/)
- Training weight: Imagenet
- Optimizer: RMS with learning rate $1\times10^-4$
- Epoch: 30
- Loss: Categorical crossentropy

|![image_struct_inceptionv3](https://lh3.googleusercontent.com/bA_Rkj4a0sA3NZ1wjUYIO5_eq0hUmiBNbagOFb84C8Y9GxeedGUYNd-LIbhAlpW-1o8xSeNypMnbD6p-XsrAQvup3FeWXrAoZig7l7Y9WIK3uDHooEMEKiNNQ2qt0PfA4Zfsyltn)|
|:-----------------------:|
| *InceptionV3 Structure* |

## 2.3. Results

<html>
<table>
  <tr>
    <th>Pre-train Model</th>
    <th>Batchsize</th>
    <th>Optimizer Algorithm</th>
    <th>Initial Learning rate 1</th>
    <th>Learning rate decay method 1</th>
    <th>Momentum 1</th>
    <th>Epochs 1</th>
    <th>Last layer</th>
    <th>Initial Learning rate 2</th>
    <th>Learning rate decay method 2</th>
    <th>Momentum 2</th>
    <th>Epochs 2</th>
    <th>Train accuracy</th>
    <th>Validation accuracy</th>


  </tr>
  <tr>
    <td>InceptionV3</td>
    <td>100</td>
    <td>Stochastic Gradient Descent (SGD)</td>
    <td>5E-04</td>
    <td>None</td>
    <td>0.8</td>
    <td>10</td>
    <td>all</td>
    <td>0.01</td>
    <td>None</td>
    <td>0</td>
    <td>100</td>
    <td>0.62</td>
    <td>0.51</td>
  </tr>

  <caption><b>Summary Results</b></caption>
</table>
</html>