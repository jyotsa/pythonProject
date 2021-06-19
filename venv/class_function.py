import pandas as pd
import numpy as np
import os, sys
from time import sleep


class Products(object):

    def __init__(self):
        while True:
            try:
                user_input = input('Enter the name of the folder with product and purchase data files: ')
                os.chdir(user_input)
                arr = os.listdir()
                purchases = pd.read_csv(arr[0])
                product_details = pd.read_csv(arr[1])
                df = pd.merge(product_details, purchases, on='PRODUCT_ID')
                self.pur = pd.DataFrame(df)
                break
            except IOError:
                sleep(1)
                print('Error: Folder not found!')


    def fillPeopleProducts(self):   #Creating correlation between product_id and user_id

        pep_pur=self.pur.groupby(['USER_ID','PRODUCT_ID']).size().unstack().fillna(0)
        self.pep_pur = pd.DataFrame(pep_pur)
        return pep_pur


    def fillProductsCoPurchase(self):  #Creating co-purchasing matrix
        print('Preparing co-purchasing matrix...')
        sleep(1)
        copay = self.pep_pur.T.dot(self.pep_pur)
        np.fill_diagonal(copay.values,0)
        self.copay = pd.DataFrame(copay)
        return copay


    def findMostBought(self):  #Getting most bought products
        frequency = self.pur.groupby('PRODUCT_ID')['USER_ID'].count().sort_values(ascending=False).head(4)
        self.frequency = pd.DataFrame(frequency)
        return frequency


    def printRecProducts(self):   #Getting product recommendation
        while True:
            print('\n')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            product = input('Enter PRODUCT ID for product recommendation or press ENTER to quit:  ')
            sleep(1)
            if product == "":
                sys.exit(0)

            while product:
                if (self.pur.PRODUCT_ID == product).any():
                    self.product = product
                    recommendation = self.copay[self.product]
                    pd.set_option('display.max_columns', 1000)
                    pd.set_option('display.max_rows', 1000)
                    pd.set_option('display.width', 1000)
                    a = self.pur[['DESCRIPTION', 'PRICE', 'PRODUCT_ID']]

                    if all(i == 0 for i in recommendation.values):

                        print('[Co-purchasing value is 0]')
                        sleep(1)
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print('Some of our recommendation')

                        for i in self.frequency.index:
                            print(i)
                        sleep(1)
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print('Suggesting one of our most popular products: ')
                        for i in self.frequency.index:
                            b = a[a.PRODUCT_ID == i]
                            c = pd.DataFrame(b).drop_duplicates()

                            print(c[['DESCRIPTION']].to_string(header=False,index=False),',','$',c[['PRICE']].to_string(header=False,index=False))
                    else:
                        correlation = recommendation.loc[(recommendation != 0)].sort_values(ascending=False).head(6)

                        print('Recommended items with', self.product, ' :')
                        for i in correlation.index:
                             print(i)
                        sleep(1)
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print('People who bought it were most likely to buy: ')

                        for i in correlation.index:


                            b = a[a.PRODUCT_ID == i]
                        # if(a.PRODUCT_ID == i).any():
                        # b=a.where(a.PRODUCT_ID == i)
                            c = pd.DataFrame(b).drop_duplicates()

                            print(c[['DESCRIPTION']].to_string(header=False,index=False),',','$',c[['PRICE']].to_string(header=False,index=False))

                else:
                   print('Invalid PRODUCT ID')
                break


if __name__ == '__main__':

    products = Products()
    products.fillPeopleProducts()
    products.fillProductsCoPurchase()
    products.findMostBought()
    products.printRecProducts()















