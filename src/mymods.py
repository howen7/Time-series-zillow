import pandas as pd

def get_datetimes(df):
    return pd.to_datetime(df.columns.values[1:], format='%Y-%m')


def melt_data(df):
    melted = pd.melt(df, id_vars=['RegionName', 'City', 'State', 'Metro', 'CountyName'], var_name='time')
    melted['time'] = pd.to_datetime(melted['time'], infer_datetime_format=True)
    melted = melted.dropna(subset=['value'])
    return melted.groupby('time').aggregate({'value':'mean'})

def plot_function(df, zipcode, params, size_test):

    data= df[df['RegionName']== zipcode]
    data = data[['time', 'value']]
    data.columns = ['ds','y']
    data.reset_index(inplace = True)

    eotindex = round(data.shape[0] * size_test)
    train = data[:eotindex]
    test = data[eotindex:]

    train_size = train.shape[0]
    test_size = test.shape[0]
    freq = 'MS'
    period = 60
    data_size = data.shape[0]

    model = Prophet(changepoint_prior_scale = params['changepoint_prior_scale'],
                             n_changepoints = params['n_changepoints'],
                             seasonality_mode = params['seasonality_mode'],
                             weekly_seasonality=False,
                             daily_seasonality = False,
                             yearly_seasonality = True,
                             interval_width=0.95)
    
    # Modeling for train set to test MOPE
    model.fit(train)
    validation = model.make_future_dataframe(periods = period + test_size, freq = freq)
    prediction = model.predict(validation)
    y_hat =  prediction.yhat[train_size:test_size+train_size]
    MAPE = np.mean(np.abs((np.array(test.y) -  
                               np.array(y_hat))/ np.array(test.y))) * 100 
    root_mse = np.sqrt(mean_squared_error(test.y,y_hat))
   
    # Modeling on entire data set to forcast
    model = Prophet(changepoint_prior_scale = params['changepoint_prior_scale'],
                         n_changepoints = params['n_changepoints'],
                         seasonality_mode = params['seasonality_mode'],
                         weekly_seasonality=False,
                         daily_seasonality = False,
                         yearly_seasonality = True,
                         interval_width=0.95)
    
    model.fit(data)
    future= model.make_future_dataframe(periods = period, freq = freq)
    forecast = model.predict(future)
    

    font = {'weight' : 'bold',
            'size'   : 22}
    pd.plotting.register_matplotlib_converters()
    f, ax = plt.subplots(figsize=(10,5))
    train.plot(kind='line', x='ds', y='y', color='blue', label='Train', ax=ax)
    test.plot(kind='line', x='ds', y='y', color='black', label='Test', ax=ax)
    prediction.loc[train_size:train_size+test_size -1].plot(kind='line', x='ds', y='yhat', color='red', label='Predicted', ax=ax)
    forecast.loc[data_size:].plot(kind='line', x='ds', y='yhat', color='orange', label='Forecast', ax=ax)
    
    plt.xlabel('Year', fontdict = font)
    plt.ylabel('Home Value',fontdict = font)
    plt.title(f'ZIP code {zipcode} Model Predictions', fontdict = font)
    plt.tight_layout()
    plt.savefig(f'../report/figures/{zipcode}_predictions', dpi = 300)
    plt.show()
    
    print(f'------------ZIP code: {zipcode} info-------------- ')
    print(f'Year 2018 forecasted home value is: ${int(test.y.tail(1))}')
    print(f'Year 2023 forecasted home value is: ${int(forecast.yhat.tail(1))}')
    
    print(f'The mean absolute percentage error of this model is: {round(MAPE,2)}%')
    
    
    return model, forecast

def optimized_params(df, zipcode, size_train):

    model_parameters = pd.DataFrame(columns = ['RMSE','MAPE','Parameters'])
    
    params_grid = {'seasonality_mode':('multiplicative','additive'),
                   'changepoint_prior_scale':[0.1,0.2,0.3,0.4,0.5],
                   'n_changepoints' : [5,10,20,30]}
    grid = ParameterGrid(params_grid)
    
    data= df[df['RegionName']== zipcode]
    data = data[['time', 'value']]
    data.columns = ['ds','y']

    eotindex = round(data.shape[0] * size_train)
    train = data[:eotindex]
    test = data[eotindex:]

    train_size = train.shape[0]
    test_size = test.shape[0]
    freq = 'MS'
    period = 60

    for p in grid:
    
        # Prophet Func
        model = Prophet(changepoint_prior_scale = p['changepoint_prior_scale'],
                             n_changepoints = p['n_changepoints'],
                             seasonality_mode = p['seasonality_mode'],
                             weekly_seasonality=False,
                             daily_seasonality = False,
                             yearly_seasonality = True,
                             interval_width=0.95)
        model.fit(train)
        future = model.make_future_dataframe(periods = period + test_size, freq = freq)
        forecast = model.predict(future)
        
        y_hat =  forecast.yhat[train_size:test_size+train_size]
        mean_ape = np.mean(np.abs((np.array(test.y) -  
                           np.array(y_hat))/ np.array(test.y))) * 100 #mean absolute percentage error 
        root_mse = np.sqrt(mean_squared_error(test.y,y_hat))


        model_parameters = model_parameters.append({'RMSE':root_mse,'Parameters':p, 'MAPE':mean_ape},ignore_index=True)
        
    param_dic = model_parameters.sort_values(by=['RMSE']).reset_index(drop=True)['Parameters'][0]
    return param_dic, model_parameters

def Prophet_func2(df, zipcodes, period, size_train):
    '''
    Used to determine how well a list of zipcodes will perform and forecast on a basic prophet model
    
    Parameters:
    df - Dataframe with time and value column in long format
    zipcodes - list of zipcodes that are in the dataframe. 
    period - how long into the future you want the to forecast in monthes ex: 60
    size_train - how large the train will be. ex: .8
    
    _____________________________Out Put ________________________________________
    Output:
    a dataframe with columns: Zipcode,Future_Home_Value, Percent_Increase, RMSE ,MAPE 
    
    RMSE = Root mean square error
    MAPE = mean absolute percentage error 
    '''
    
    df_info = pd.DataFrame(dict(Zipcode=[], 
                                 Home_Value=[], 
                                 Future_Home_Value=[], 
                                 Percent_Increase=[],
                                 RMSE = [],
                                 MAPE =[])) 
    for zipcode in zipcodes:
        
       # selecting zipcode from df and changing time and value to ds and y
        data= df[df['RegionName']== zipcode]
        data = data[['time', 'value']]
        data.columns = ['ds','y']
        
        # creating stop index and measuring size of train/test
        eotindex = round(data.shape[0] * size_train)
        train = data[:eotindex]
        test = data[eotindex:]
        train_size = train.shape[0]
        test_size = test.shape[0]
        freq = 'MS'
        
        value_now = int(data.y.tail(1))

        # Prophet Func
        model = Prophet(daily_seasonality= False, weekly_seasonality= False, interval_width=0.95)
        model.fit(train)
        future = model.make_future_dataframe(periods = period + test_size, freq = freq)
        forecast = model.predict(future)

        value_future = round(list(forecast.yhat)[-1],-2)
        diff= value_future - value_now
        rate_5_yrs = 100*(diff / value_now)
        
        y_hat = forecast.yhat[train_size:test_size+train_size]
        root_mse = round(np.sqrt(mean_squared_error(test.y,y_hat)),2)
        mean_ape = round(np.mean(np.abs((np.array(test.y) -  
                           np.array(y_hat))/ np.array(test.y))) * 100, 2) #mean absolute percentage error 
        df_info = df_info.append({'Percent_Increase': rate_5_yrs,
                                  'Home_Value': value_now, 
                                  'Future_Home_Value': value_future,
                                  'Zipcode': zipcode,
                                  'RMSE': root_mse,
                                  'MAPE':mean_ape}, ignore_index = True)
                                    
        
        df_info.Zipcode = df_info.Zipcode.astype('int64')
    return df_info