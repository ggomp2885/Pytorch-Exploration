"""This is my documentation file for all Pytorch commands and functions"""

                        # Generic Code Samples
                                 #Imports
# import torch
# import torch.nn as nn                 # prebuilt neural net layers
# import torch.nn.functional as F       # activations functions
# import torch.optim as optim           # optimizer functions
                                #Functions
                                  #many functions can be written explicitly, such as torch.func_name(tens_name) or implicitly as in tens_name.func_name()
                                    #Creating tensors
# torch.tensor(list_name)               # creates tensor with data type inferred from input (Copy) (Factory)
# torch.as_tensor(list_name)            # (Share) (Higher performance at scale because there's only one total instance of the tensor) (Factory)
# torch.eye(#)                          # creates a tensor with the “identity matrix” with # of rows (1’s along the diagonal)
# torch.diag(torch.ones(3))             # same as using the .eye(#) function
# torch.zeros(#,#)                      # creates a tensor of shape #,# with all zeros
# torch.ones(#,#)                       # creates tensor of shape #,# with all one's
# torch.rand(#,#)                       # creates tensor of shape #,# with all random values between 0 and 1
# torch.arange(start=#, end=#, step=#)  # creates a tensor starting with the first #, ending at the 2nd # (not inclusive), with a step size of the 3rd # - also, do not have to include these words
# torch.linspace(start=#, end=#, steps=#)   # creates a tensor starting with the first #, ending at the 2nd # (is inclusive), with the 3rd # of steps inbetween - also do not have to include these words
# torch.from_numpy(array_name)          # creates a tensor from a numpy array

                                    #Manipulating tensors
# sorted_tens_1, indices = torch.sort(tens_1, descending=False)
# torch.where(tens_>#, tens_, tens_*2)  # finds where values > #, sets value = to middle value, where this is not true, does 3rd operation
# tens_name.permute(#,#,#)              # switches the shape of the tensor around, using the orginal index values. IE, if you wanted a tensor of shape (50, 25, 30) to be (30, 25, 50) in this function you would input (2, 1, 0) # .t() is for ease of use, with only 2 dimensional tensors.
# tens_name.squeeze(#)                  # removes a dimension from a tensor, number here is the index of the dimension you want to remove.
# tens_name.unsqueeze(#)                # adds a dimension to a tensor, number here is the index where the new dimension should be placed, either infront or behind the indexes of the current dimensions.

                                #Methods
# tens_name.reshape(#,#)                # reshapes the tensor, (new shape must have same amount of elements) can put (1,-1) in here, as a keyword to flatten the tensor
# tens_name.view(#,#)                   # reshapes the tensor, only works on tensors in the same contigious memory block, and therefore can be more efficient at times, I probably wont use this for now.
# tens_name.short()                     # converts to int 16 (default is int 32)
# tens_name.half()                      # converts to float 16
# tens_name.float()                     # converts to float 32
# tens_name.long()                      # converts to int 64
# tens_name.double()                    # converts to float 64
# tens_name.bool()                      # converts to boolean
# tens_name.numpy()                     # converts to numpy array

                                #Attributes
# tens_name.shape()                     # returns shape of tensor (.size is the exact same thing)
# tens_name.numel()                     # returns the number of elements in the tensor
# tens_name.dtype                       # returns data type
# tens_name.device                      # returns gpu/cpu
# tens_name.layout                      #
# tens_name.ndimension()                # returns # of dimensions of the tensor

                                # Indexing tensors
# tens_name[#]                          # returns entire row
# tens_name[:,#]                        # returns entire column
# tens_name[(tens_name ># | tens_name <#    # returns elements above OR below these #s, can also use the & sign here
                                # Basic Tensor Math Operations
                                    # I can add a _ after any of these functions to do these operations, "in place," which takes less time and memory
                                    # broadcasting is a built-in feature for ease of use which allows you to do operations between tensors of different sizes
                                    # in each of these parenthesis, you can also specify dim=#, to just do the operation on a specific row. When specifying an axis, the index returned is relative to that axis.
# tens_name.sum()                       # adds all the elements of a tensor into one scalar value.
# tens_name.prod()                      # multiples all elements
# tens_name.std()                       # std all elements
# tens_name.max()                       # returns the max value of all the elements in the array.
# tens_name.mean()                      # returns a single value tensor of the avg of all elements
# tens_name.mean().item()               # returns a single scalar value
# tens_name.argmax()                    # returns index of max value of the elements. index value returned is as if the function was flattened to a 1D array.
# tens_name.argmin()                    # returns index of min value of the elements. index value returned is as if the function was flattened to a 1D array.
# tens_name.unique()                    # returns the unique values of the tensor
# tens_name_1 += tens_name_2            # Easiest way to write ASDM functions in place
# tens_name < #                         # returns a tensor containing all elements less than this #
# tens_name ** #                        # raises all elements by this power
# tens_name.mm(tens_name_2)             # raises all elements by the element wise numbers in another matrix
# tens_name.cat(tens_name_2, dim=#)     # this adds tensors together similar to a "union" in SQL, the dim specifies whether you want to add the columns together or the rows, left blank it will do both.
# tens_name.clamp(max=#)                # sets all elements above this #, to this #, can also use min=# here
# tens_name.abs()                       # returns the absolute value of each element
# tens_name.any()                       # returns true if any values are true
# tens_name.all(tens_name)              # returns true if all values are true
# tens_name_1.dot(tens_name_2)          # dot product (multiples matrices together and adds all elements to return one single value).
# torch.eq(tens_name_1, tens_name_2)    # (explicit example) returns a boolean tensor where elements of two tensors are equal
# longer setup                          # can also do "batch multiplication" which is like "multiple" multiplication in one, not sure where Id end up using this though

	                                #Functions for creating NNs
# class Net(nn.Module):                 # Creates a class of functions
# 	  super().func_name()                 # initiates the nn.module part of the class function
#     self.lay_name_1 = nn.Linear(input #, output #)        # creates a fully connected layer - For 3 hidden layers, repeat this 4 times, because the first is the input layer, and the last line contains the hidden layer, and the output layer.
#     self.lay_name_2 = nn.Linear(input #, output #)        # creates a fully connected layer
#     self.lay_name_3 = nn.Linear(input #, output #)        # creates a fully connected layer
#     self.lay_name_4 = nn.Linear(input #, output #)        # creates a fully connected layer

                                            #EXAMPLE CODE
                                    #Example code to create simple FF NN with 3 hidden layers


# def forward(self, var_name1):
#     var_name = F.act_func(self.lay_name1(var_name1))
#     var_name = F.act_func(self.lay_name2(var_name1))
#     var_name = F.act_func(self.lay_name3(var_name1))
#     var_name = self.lay_name4(var_name1)  ## this may be unnecessary
#     return F.loss_func(var_name1, dim=1)
# 
# opt_var_name = optim.Adam(net.parameters(), lr=0.001)
# 
# EPOCHS = 3
# for epoch in range(EPOCHS):
#     for data in trainset:
#         X, y = data
#         net.zero_grad()
#         output = net(X.view(-1, input  # )
#         loss_var_name = F.loss_func_name(output, y)
#         loss_var_name.backward()
#         opt_var_name.step()
# 
                    # measuring accuracy
# Correct = 0
# Total = 0
# with torch.no_grad()
#    for data in trainset:
#        X, y = data
#        Output = net(X.view(-1, 784)
#             for idx, i in enumerate(output):
#                 if torch.argmax(i) == y[idx]:
#                     correct += 1
#                     total += 1
#        print(“Accuracy “, round(correct / total, 3))


                                            # EXAMPLE CODE OF BASIC FUNCTIONS -- All confirmed working 11/11/20

# import numpy as np
# import torch
# device = "cuda" if torch.cuda.is_available() else "cpu"
#
# my_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32, device=device, requires_grad=True)
# print(my_tensor)
# print(my_tensor.dtype)
# print(my_tensor.device)
# print(my_tensor.shape)
# print("requires grad? {}".format(my_tensor.requires_grad))
# print()

# x = torch.empty(size=(3,3))
# print(x)
# x = torch.zeros(3,3)
# print(x)
# x = torch.ones(3,3)
# print(x)
# x = torch.rand(3,3)
# print(x)
# x = torch.eye(3,3)
# print(x)
# x = torch.arange(0, 5, 1)
# print(x)
# x = torch.linspace(.1,1,10)
# print(x)
# x = torch.empty(size=(1,5)).normal_(mean=0, std=1)
# print (x)
# x = torch.empty(size=(1,5)).uniform_(0,1)
# print(x)
# x = torch.diag(torch.ones(3))    # same as using the .eye function
# print(x)

# print(x.bool())
# print(x.short())
# print(x.long())

# np_array = np.zeros((5, 5))
# print(np_array.)
# tensor = torch.from_numpy(np_array)
# print(tensor.type)
# np_back = tensor.numpy()
# print(np_back.type)


                                                # EXAMPLE CODE OF 3 Layer NN for MNIST CV
                                                    # Contains: Imports, create NN, hyperparams, loading data, initalize NN, Loss and Optimizer, training, accuracy check
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from timeit import default_timer as timer
from torch.utils.data import DataLoader

start = timer()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


#Loading in MNIST Train and Test datasets from torchvision.datasets
batch_size = 64
train_dataset = datasets.MNIST(root='dataset/', train=True, transform=transforms.ToTensor(), download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = datasets.MNIST(root='dataset/', train=False, transform=transforms.ToTensor(), download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)



                                    # Create simple fully connected NN
# class NN(nn.Module):
#     def __init__(self, input_size, num_classes):
#         super(NN, self).__init__()
#         self.fc1 = nn.Linear(input_size, 50)
#         self.fc2 = nn.Linear(50, num_classes)
#
#     def forward(self, x):
#         x = F.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x

                                    # Create simple Convolutional NN
class CNN(nn.Module):
    def __init__(self, in_channels = 1, num_classes=10):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=(3,3), stride=(1,1), padding=(1,1)) # these last 3 arguments are chosen based on a simple formula which feeds the output of this layer into the next layer with the same dimensions
        self.pool = nn.MaxPool2d(kernel_size=(2,2), stride = (2,2))
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3,3), stride=(1,1), padding=(1,1))
        self.fc1 = nn.Linear(16*7*7, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = x.reshape(x.shape[0],-1)
        x = self.fc1(x)
        return x

                                    # shape tests of model output with mock data
                                        #FC NN
# model = NN(784,10)
# x = torch.random(64, 784)             # first # is the # of rows, 2nd is the # of features
# print(model(x).shape)                 # checks that the output is correct
                                        #CNN
# model = CNN()
# x = torch.randn(64, 1, 28, 28)
# print(model(x).shape)



                                    # Hyperparameters
                                        # General HyperPs
num_epochs = 5                              # value represents how many times the loop runs to train the model on the same dataset)
num_classes = 10
learning_rate = .001
                                        # FC HyperPs
# input_size = 784
                                        # CNN HyperPs
in_channels = 1                             # value represents amount of colors in image


                                    # Model build, Optimizer, and Loss function
                                        # FC NN
# model = NN(input_size=input_size, num_classes=num_classes).to(device)
                                        # CNN
model = CNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

                                    # NN Training loop
for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(train_loader):      # this fancier for loop just gives the index for each epoch your in
        # Put data in Cuda if possible
        data = data.to(device=device)
        targets = targets.to(device=device)
                                        # FC NN specific
#        data = data.reshape(data.shape[0],-1)                       # reshapes the 28,28 into a 784, by "squeezing" the input to a flat tensor
        # forward function
        scores = model(data)
        loss = criterion(scores, targets)
        # backward function
        optimizer.zero_grad()
        loss.backward()
        # gradient descent function
        optimizer.step()

# Check Accuracy
def check_accuracy(loader, model):
    if loader.dataset.train:
        print('Checking accuracy on train set')
    else:
        print('Checking accuracy on test set')
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)
                                        # FC NN specific
#            x = x.reshape(x.shape[0], -1)

            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
        print(f'Got {num_correct} / {num_samples} with accuracy of {float(num_correct)/float(num_samples)*100:.2f}')
    model.train(x)

check_accuracy(train_loader, model)
check_accuracy(test_loader, model)

end = timer()
print(f'Time taken: {end-start:.1f} Seconds')
# test Acc with  epochs and batch size of 128 = 94.88
# test Acc with 3 epochs and batch size of 32 = 96.19
