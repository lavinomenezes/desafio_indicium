import pickle
import numpy  as np
import pandas as pd

class indicium:
    
    def __init__( self ):
        self.home_path = 'C:/Users/Lavin/Documents/desafios/desafio_indicium/'
        self.rotational_speed_rpm_scaler =   pickle.load(open(self.home_path + 'src/features/rotational_speed_rpm_scaler.pkl','rb'))
        self.torque_nm_scaler =              pickle.load(open(self.home_path + 'src/features/torque_nm_scaler.pkl','rb'))
        self.air_temperature_k_scaler =      pickle.load(open(self.home_path + 'src/features/air_temperature_k_scaler.pkl','rb'))
        self.process_temperature_k_scaler =  pickle.load(open(self.home_path + 'src/features/process_temperature_k_scaler.pkl','rb'))
        self.tool_wear_min_scaler =          pickle.load(open(self.home_path + 'src/features/tool_wear_min_scaler.pkl','rb')) 
        self.power_w_scaler =                pickle.load(open(self.home_path + 'src/features/power_w_scaler.pkl','rb'))
        self.encoding_failure_type =         pickle.load(open(self.home_path + 'src/features/encoding_failure_type.pkl','rb')) 
                                           
    def data_cleaning(self,df1):
        # nenhum processo de limpeza nesse ciclo
                                           
        return df1
    
    def feature_engineering(self,df2):
           
        # Nova coluna power_w
        df2['power_w'] = df2['torque_nm'] * df2['rotational_speed_rpm'] * np.pi / 30                                    
                                           
        return df2
    
    def data_preparation(self,df3):
    
        #robustscaler
        #aplicando a escala previamente salva
        df3['rotational_speed_rpm'] = self.rotational_speed_rpm_scaler.transform(df3[['rotational_speed_rpm']].values)


        #aplicando a escala previamente salva
        df3['torque_nm'] =  self.torque_nm_scaler.transform(df3[['torque_nm']].values)

        #min-max scaler
        # aplicando a escala previamente salva
        df3['air_temperature_k'] = self.air_temperature_k_scaler.transform(df3[['air_temperature_k']].values)


        # aplicando a escala previamente salva
        df3['process_temperature_k'] = self.process_temperature_k_scaler.transform(df3[['process_temperature_k']].values)


        # aplicando a escala previamente salva
        df3['tool_wear_min'] = self.tool_wear_min_scaler.transform(df3[['tool_wear_min']].values)

        # aplicando a escala previamente salva
        df3['power_w'] = self.power_w_scaler.transform(df3[['power_w']].values)



        #frequêncy encoding
        freq = np.round_(df3['type'].value_counts(normalize=True),2).to_dict()
        df3['type'] = df3['type'].map(freq)
                                           
        #feature selection
        cols_select_final = ['air_temperature_k',
                             'process_temperature_k', 
                             'rotational_speed_rpm', 
                             'torque_nm','tool_wear_min', 
                             'power_w']
        
        return df3[cols_select_final]

    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict( test_data )
        
        # join prediction into original data
        original_data['predictedValues'] = pred
        original_data['predictedValues'] = self.encoding_failure_type.inverse_transform(original_data[['predictedValues']])
        
        return original_data
                                           