# importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Solution:
    def __init__(self) -> None:
        # TODO: 
        # Load data from data/chipotle.tsv file using Pandas library and 
        # assign the dataset to the 'chipo' variable.
        file = 'data/chipotle.tsv'
        self.chipo = pd.read_csv('data/chipotle.tsv', sep='\t')
    
    def top_x(self, count) -> None:
        # TODO
        # Top x number of entries from the dataset and display as markdown format.
        topx = self.chipo.head(count)
        print(topx.to_markdown())
        
    def count(self) -> int:
        # TODO
        # The number of observations/entries in the dataset.
        shape = self.chipo.shape
        return (shape[0])
    
    def info(self) -> None:
        # TODO
        # print data info.
        print(self.chipo.info())
    
    def num_column(self) -> int:
        # TODO return the number of columns in the dataset
        shape = self.chipo.shape
        return (shape[1])
    
    def print_columns(self) -> None:
        # TODO Print the name of all the columns.
        print(self.chipo.columns.values.tolist())
    
    def most_ordered_item(self):
        # TODO
        c = self.chipo.groupby('item_name')
        c = c.sum().sort_values(['quantity'], ascending=False).reset_index()
        c = c.head(1).to_dict()
        order_id = c["order_id"][0]
        quantity = c["quantity"][0]
        item_name = c["item_name"][0]
        return item_name, order_id, quantity

    def total_item_orders(self) -> int:
       # TODO How many items were orderd in total?
       return (self.chipo['quantity'].sum())
   
    def total_sales(self) -> float:
        # TODO 
        # 1. Create a lambda function to change all item prices to float.
        # 2. Calculate total sales.
        total_sales_per_order = self.chipo['item_price'].apply(lambda x:float(x.replace('$', '')))
        value = np.multiply(total_sales_per_order, self.chipo['quantity']).sum()
        return value
    
    def num_orders(self) -> int:
        # TODO
        # How many orders were made in the dataset?
        return (chipo['order_id'].nunique())
    
    def average_sales_amount_per_order(self) -> float:
        # TODO
        total_orders = Solution.num_orders(self)
        total_sales = Solution.total_sales(self)
        return round(total_sales/total_orders, 2)
        
    def num_different_items_sold(self) -> int:
        # TODO
        # How many different items are sold?
        return (chipo['item_name'].nunique())
    
    def plot_histogram_top_x_popular_items(self, x:int) -> None:
        from collections import Counter
        letter_counter = Counter(self.chipo.item_name)
        top5_df = pd.DataFrame.from_dict(letter_counter, orient='index')
        top5_df = top5_df[0].sort_values(ascending = False)[:x]
        top5_df.plot(kind='bar')
        plt.xlabel('Item_name ')
        plt.ylabel('No of Times Item was Ordered')
        plt.title('Five most ordered item names')
        plt.show()
        
    def scatter_plot_num_items_per_order_price(self) -> None:
        # TODO
        # 1. create a list of prices by removing dollar sign and trailing space.
        # 2. groupby the orders and sum it.
        # 3. create a scatter plot:
        #       x: orders' item price
        #       y: orders' quantity
        #       s: 50
        #       c: blue
        # 4. set the title and labels.
        #       title: Numer of items per order price
        #       x: Order Price
        #       y: Num Items
        # create a list of prices
        chipo["item_price"] = [float(value[1:-1]) for value in chipo["item_price"]] # strip the dollar sign and trailing space
        order_price = chipo.groupby('order_id').sum()
        plt.scatter(x = order_price.item_price, y = order_price.quantity, s = 50, c = 'blue')
        plt.xlabel('Order Price')
        plt.ylabel('Num Items')
        plt.title('Numer of items per order price')
        plt.ylim(0)



def test() -> None:
    solution = Solution()
    solution.top_x(10)
    count = solution.count()
    print(count)
    assert count == 4622
    solution.info()
    solution.print_columns()
    count = solution.num_column()
    assert count == 5
    item_name, order_id, quantity = solution.most_ordered_item()
    assert item_name == 'Chicken Bowl'
    assert order_id == 713926
    assert quantity == 761
    total = solution.total_item_orders()
    assert total == 4972
    assert 39237.02 == solution.total_sales()
    assert 1834 == solution.num_orders()
    assert 21.39 == solution.average_sales_amount_per_order()
    assert 50 == solution.num_different_items_sold()
    solution.plot_histogram_top_x_popular_items(5)
    solution.scatter_plot_num_items_per_order_price() 


if __name__ == "__main__":
# execute only if run as a script
    test()  