import matplotlib.pyplot as plt

def figplot(state_space_coverage, action_space_coverage):
    fig = plt.figure(figsize=(5,5))
    cmap = plt.get_cmap("tab10")
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]
    rect_hist_action = [left+1, bottom, width, height]

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)
    axHist_action = plt.axes(rect_hist_action)

    axScatter.scatter(state_space_coverage[:,0],state_space_coverage[:,1],marker='.',alpha=0.3, color=cmap(0));
    axScatter.set_xlabel("Battery")
    axScatter.set_ylabel("Harvested Energy")


    axHistx.hist(state_space_coverage[:,0],rwidth=1.0,bins=100,color=cmap(1),log=not False,histtype='step');
    axHistx.tick_params(labelbottom=False)

    axHisty.hist(state_space_coverage[:,1],bins=100,rwidth=1.0,orientation='horizontal',color=cmap(2),log=not False,histtype='step');        axHisty.tick_params(labelleft=False)

    axHist_action.hist(action_space_coverage,bins = 10,rwidth=0.95,color=cmap(3))
    axHist_action.set_xlabel("Duty Cycle")
    axHist_action.yaxis.set_label_position("right")
    axHist_action.yaxis.tick_right()
    plt.show()
    
    return 0
