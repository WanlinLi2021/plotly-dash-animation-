import pandas as pd
import plotly           
import plotly.express as px
import plotly.io as pio

df = pd.read_csv(r"/Users/wanlin/Documents/1visualization/code/1COVID_QC/cas_QC.csv", sep=",")

#print(df.columns)

time_lines =  ['4.25', '4.26', '4.27', '4.28', '4.29', '4.30', '5.01',
                '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08']

df1 = pd.melt(df,id_vars=['regions'],
    value_vars= time_lines,
    var_name='day',value_name='n_cas', ignore_index=False)

df1.sort_values(["day","regions"], inplace=True)

#print(df1)

# Build the dot plot (variation of scatter plot)
fig = px.scatter(df1, x="n_cas", y="regions", animation_frame="day", color="regions",
                 range_x=[0,330], 
                 range_y=[-0.5,18.5],
                 title="Number of confirmed cases by region",
                 labels={"n_cas":"number of cases"} # customize label
      )
fig.update_layout(title={'x':0.5,'xanchor':'center','font':{'size':20}},
                  xaxis=dict(title=dict(font=dict(size=20))),
                  yaxis = dict(title=dict(font=dict(size=20))),
                  #yaxis={'title':{'text':None}},
                  legend={'font':{'size':18},'title':{'font':{'size':18}}})

#print(fig.layout)
#print(fig.data)
#print(fig.frames)

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 800
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 800


pio.show(fig)
