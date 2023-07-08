#!/usr/bin/env python
# coding: utf-8

# In[50]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot


# In[55]:


df = pd.read_csv("filepath") #file path
df.head()


# In[56]:


df.describe()


# In[57]:


df.set_index(['MD'], inplace = True)
df.head()


# In[ ]:


df = df.dropna()


# In[58]:


# Your DataFrame and data variables

GR = df["GR"]
RES_MED = df["RES_MED"]
RES_SLW = df["RES_SLW"]
RES_DP = df["RES_DEP"]
NEU = df["NEU"]
DENS = df["DEN"]
DT = df["DT"]
SW = df["SW"]
POR = df["POR"]
PERM = df["PERM"]


# In[59]:


def plot_wireline(df, save_path=None):
    fig, ax = plt.subplots(figsize=(20, 15))
    
    # Set up the plot axes
    # Existing tracks
    ax1 = plt.subplot2grid((1,7), (0,0), rowspan=1, colspan=1)  # Gamma Ray track
    ax2 = plt.subplot2grid((1,7), (0,1), rowspan=1, colspan=1, sharey=ax1)  # Resistivity - Med track
    ax3 = plt.subplot2grid((1,7), (0,2), rowspan=1, colspan=1, sharey=ax1)  # Density track
    ax4 = plt.subplot2grid((1,7), (0,3), rowspan=1, colspan=1, sharey=ax1)  # Permeability track
    ax5 = ax3.twiny()  # Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,7), (0,4), rowspan=1, colspan=1, sharey=ax1)  # Porosity track
    ax7 = ax2.twiny()  # Resistivity - Curve 2 track
    ax8 = ax2.twiny()  # Resistivity - Curve 3 track
    ax9 = plt.subplot2grid((1,7), (0,5), rowspan=1, colspan=1, sharey=ax1) #Sonic plot
    ax10 = plt.subplot2grid((1,7), (0,6), rowspan=1, colspan=1, sharey=ax1)  # SW track

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines. If you add new tracks, adjust the numbers below too.
    ax11 = ax1.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax2.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = ax2.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax3.twiny()
    ax14.xaxis.set_visible(False)
    ax15 = ax4.twiny()
    ax15.xaxis.set_visible(False)
    ax16 = ax6.twiny()
    ax16.xaxis.set_visible(False)
    ax17 = ax9.twiny()
    ax17.xaxis.set_visible(False)


    # Gamma Ray track
    ax1.plot(GR, df.index, color="black", linewidth=1.5)
    ax1.fill_betweenx(df.index, np.median(GR), GR, where=GR < np.median(GR), color="yellow")
    ax1.fill_betweenx(df.index, GR, np.median(GR), where=GR >= np.median(GR), color="brown")
    ax1.set_xlabel("Gamma")
    ax1.xaxis.label.set_color("black")
    ax1.set_xlim(40, 220) ## Adjust the limit
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="black")
    ax1.spines["top"].set_edgecolor("black")
    ax1.title.set_color('black')
    ax1.set_xticks([40, 100, 160, 220])

    # Resistivity track
    ax2.plot(RES_MED, df.index, color="red", linewidth=1.5)
    ax2.set_xlabel("Resistivity - Med")
    ax2.set_xlim(0.1, 1000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    ax2.set_xticks([0.1, 1, 10, 100, 1000])
    ax2.semilogx()

    # Density track
    ax3.plot(DENS, df.index, color="red", linewidth=1.5)
    ax3.set_xlabel("Density")
    ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    ax3.set_xticks([1.95, 2.2, 2.45, 2.7, 2.95])

    # Permeability track
    ax4.plot(PERM, df.index, color="purple", linewidth=1.5)
    ax4.set_xlabel("Permeability")
    ax4.set_xlim(0.01, 2000)
    ax4.xaxis.label.set_color("purple")
    ax4.tick_params(axis='x', colors="purple")
    ax4.spines["top"].set_edgecolor("purple")
    ax4.set_xticks([ 0.01, 0.1, 1, 10, 100, 1000, 2000], minor=True)
    ax4.semilogx()

    # Neutron track placed on top of density track
    ax5.plot(NEU, df.index, color="blue", linewidth=1.5)
    ax5.set_xlabel('Neutron')
    ax5.xaxis.label.set_color("blue")
    ax5.set_xlim(0.45, -0.15)
    ax5.tick_params(axis='x', colors="blue")
    ax5.spines["top"].set_position(("axes", 1.08))
    ax5.spines["top"].set_visible(True)
    ax5.spines["top"].set_edgecolor("blue")
    ax5.set_xticks([0.45, 0.30, 0.15, 0.0, -0.15])

    # Porosity track
    ax6.plot(POR, df.index, color="black", linewidth=1.5)
    ax6.set_xlabel("Porosity")
    ax6.set_xlim(0, 0.25)
    ax6.xaxis.label.set_color("black")
    ax6.tick_params(axis='x', colors="black")
    ax6.spines["top"].set_edgecolor("black")
    ax6.set_xticks([0, 0.05, 0.1, 0.15, 0.2, 0.25])

    # Resistivity track - Curve 2
    ax7.plot(RES_SLW, df.index, color="green", linewidth=1.5)
    ax7.set_xlabel("Resistivity - Shallow")
    ax7.set_xlim(0.1, 100, 1000)
    ax7.xaxis.label.set_color("green")
    ax7.spines["top"].set_position(("axes", 1.08))
    ax7.spines["top"].set_visible(True)
    ax7.tick_params(axis='x', colors="green")
    ax7.spines["top"].set_edgecolor("green")
    ax7.set_xticks([0.1, 1, 10, 100, 1000])
    ax7.semilogx()

    # Resistivity track - Curve 3
    ax8.plot(RES_DP, df.index, color="blue", linewidth=1.5)
    ax8.set_xlabel("Resistivity - Deep")
    ax8.set_xlim(0.1, 1000)
    ax8.xaxis.label.set_color("blue")
    ax8.spines["top"].set_position(("axes", 1.14))
    ax8.spines["top"].set_visible(True)
    ax8.tick_params(axis='x', colors="blue")
    ax8.spines["top"].set_edgecolor("blue")
    ax8.set_xticks([0.1, 1, 10, 100, 1000])
    ax8.semilogx()
    
    # S-Sonic track
    ax9.plot(DT, df.index, color = "black", linewidth = 1.5)
    ax9.set_xlabel("DT")
    ax9.set_xlim(150, 350)
    ax9.xaxis.label.set_color("black")
    ax9.tick_params(axis='x', colors="black")
    ax9.spines["top"].set_edgecolor("black")
    ax9.set_xticks([150, 200, 250, 300, 350])
    
    # SW track
    ax10.plot(SW, df.index, color = "blue", linewidth = 1.5)
    ax10.fill_betweenx(df.index, 0.75, SW, where=SW < 0.75, color="green")
    ax10.fill_betweenx(df.index, SW, 0.75, where=SW >= 0.75, color="blue")
    ax10.set_xlabel("SW")
    ax10.set_xlim(0, 1)
    ax10.xaxis.label.set_color("blue")
    ax10.tick_params(axis='x', colors="black")
    ax10.spines["top"].set_edgecolor("black")
    ax10.set_xticks([0, 0.25, 0.5, 0.75, 1])

    # Common functions for setting up the plot can be extracted into a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6, ax9, ax10]:
        ax.set_ylim(3053, 3307.537200) ## Adjust the depth
        ax.grid(which='both', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))

    for ax in [ax2, ax3, ax4, ax6, ax9, ax10]:
        plt.setp(ax.get_yticklabels(), visible=False) 
    
    plt.tight_layout()
    fig.subplots_adjust(wspace=0.25) # Increase or decrease the value to adjust spacing
    
    
    if save_path:
        plt.savefig(save_path, format='jpeg', dpi=600, bbox_inches='tight')
    
    plt.show()


# In[ ]:


import os
print(os.path.isdir("save_path"))


# In[62]:


save_path = "save_path"
plot_wireline(df, save_path=save_path)


# In[ ]:




