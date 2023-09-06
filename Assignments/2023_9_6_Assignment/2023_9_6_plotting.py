import matplotlib.pyplot as plt

f = open("ecut_data.txt")
dat = f.readlines()

x = []
y = []
z = []
for i in range(len(dat)):
    x.append(float(dat[i].split()[0]))
    y.append(float(dat[i].split()[1]))
    z.append(float(dat[i].split()[2]))

fig, ax = plt.subplots(1,2)
ax[0].plot(x,y, color = 'r')
ax[1].plot(x,z, color = 'g')
ax[0].set_xlabel("ecut", size = 12)
ax[1].set_xlabel("ecut", size = 12)
ax[0].set_ylabel("total energy (Ry)", size = 12)
ax[1].set_ylabel("time (s)", size = 12)
for i in range(2):
    ax[i].tick_params(labelsize = 12)
    ax[i].tick_params(labelsize = 12)
    ax[i].grid()
plt.show()

f = open("k_no_offset_data.txt")
dat = f.readlines()
x = []
y = []
z = []
f1 = open("k_yes_offset_data.txt")
dat1 = f1.readlines()
x1 = []
y1 = []
z1 = []
for i in range(len(dat)):
    x.append(float(dat[i].split()[0]))
    y.append(float(dat[i].split()[1]))
    z.append(float(dat[i].split()[2]))
for i in range(len(dat1)):
    x1.append(float(dat1[i].split()[0]))
    y1.append(float(dat1[i].split()[1]))
    z1.append(float(dat1[i].split()[2]))

fig, ax = plt.subplots(1,2)
ax[0].plot(x,y, color = 'b', label = 'no offset')
ax[0].plot(x1,y1, color = 'orange', label = 'with offset')
ax[1].plot(x,z, color = 'b', label = 'no offset')
ax[1].plot(x1,z1, color = 'orange', label = 'with offset')
ax[0].set_xlabel("k", size = 12)
ax[1].set_xlabel("k", size = 12)
ax[0].set_ylabel("total energy (Ry)", size = 12)
ax[1].set_ylabel("time (s)", size = 12)
for i in range(2):
    ax[i].tick_params(labelsize = 12)
    ax[i].tick_params(labelsize = 12)
    ax[i].grid()
    ax[i].legend(loc = 'upper right')
plt.show()
