from sklearn import preprocessing
import pandas as pd


class CategoricalFeature:
    def __init__(self, df, categorical_features, encoding_type, handle_na=False):
        """
        :param df: pandas dataframe
        :param categorical_features: list of column names e.g. ['ord_1','ord_2'......]
        :param encoding_type: label,binary

        """
        self.df = df
        self.cat_features = categorical_features
        self.enc_type = encoding_type
        self.handle_na = handle_na
        self.label_encoders = dict()
        self.binary_encoders = dict()
        self.ohe = dict()

        if handle_na:
            for c in self.cat_features:
                self.df.loc[:, c] = self.df.loc[:, c].astype(str).fillna('-9999999999999999999')
            self.output_df = self.df.copy(deep=True)

    def _label_encoding_(self):

        for c in self.cat_features:
            lbl = preprocessing.LabelEncoder()
            lbl.fit(self.output_df[c].values)
            self.output_df.loc[:, c] = lbl.transform(self.output_df[c].values)

            self.label_encoders[c] = lbl

        if 'Unnamed: 0' in self.output_df.columns:
            self.output_df.drop(self.output_df.filter(regex="Unnamed"), axis=1, inplace=True)
        return self.output_df

    def _label_binarization(self):
        for c in self.cat_features:
            lbl = preprocessing.LabelBinarizer()
            lbl.fit(self.output_df[c].values)
            val = lbl.transform(self.output_df[c].values)  # Array
            self.output_df = self.output_df.drop(c, axis=1)
            for j in range(val.shape[1]):
                new_col_name = c + f"__bin_{j}"
                self.output_df[new_col_name] = val[:, j]
            self.binary_encoders[c] = lbl

        if 'Unnamed: 0' in self.output_df.columns:
            self.output_df.drop(self.output_df.filter(regex="Unnamed"), axis=1, inplace=True)
        return self.output_df

    def _one_hot(self):
        dummies = pd.get_dummies(self.output_df[self.cat_features], drop_first=True)
        dataframe = pd.concat([self.output_df, dummies], axis=1)
        dataframe.drop(self.cat_features, axis=1, inplace=True)
        if 'Unnamed: 0' in dataframe.columns:
            dataframe.drop(dataframe.filter(regex="Unnamed"), axis=1, inplace=True)
        return dataframe

    def fit_transform(self):
        if self.enc_type == 'label':
            return self._label_encoding_()
        elif self.enc_type == 'binary':
            return self._label_binarization()
        elif self.enc_type == 'ohe':
            return self._one_hot()
        else:
            raise Exception('Encoding type unknown')
    #
    # def transform(self, dataframe):
    #     if self.handle_na:
    #         for c in self.cat_features:
    #             dataframe.loc[:, c] = dataframe.loc[:, c].astype(str).fillna("-999999999")
    #     if self.enc_type == 'label':
    #         for c, lbl in self.label_encoders.items():
    #             dataframe.loc[:, c] = lbl.transform(dataframe[c].values)
    #         return dataframe
    #     elif self.enc_type == 'binary':
    #         print(self.binary_encoders.items())
    #         for c, lbl in self.binary_encoders.items():
    #             print(c)
    #             val = lbl.transform(dataframe[c].values)
    #             dataframe = dataframe.drop(c, axis=1)
    #             for j in range(val.shape[1]):
    #                 new_col_name = c + f"__bin_{j}"
    #                 self.dataframe[new_col_name] = val[:, j]
    #             print(dataframe)
    #         return dataframe
    #     else:
    #         raise Exception('Encoding type not understood')


