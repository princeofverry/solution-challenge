# Inisialisasi kelas Solution
class Solution(object):
    
    # Metode untuk mencari keuntungan maksimum dari satu transaksi beli-jual saham
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Jika array prices kosong, langsung kembalikan 0 karena tidak bisa dilakukan transaksi
        if not prices:
            return 0
        
        # Inisialisasi min_price dengan nilai tak terhingga
        min_price = float('inf')
        # Inisialisasi max_profit dengan nilai 0
        max_profit = 0

        # Loop untuk mengiterasi setiap harga dalam array prices
        for price in prices:
            # Jika harga saat ini lebih kecil dari min_price, update min_price
            if price < min_price:
                min_price = price
            # Jika harga saat ini dikurangi min_price lebih besar dari max_profit yang tersimpan,
            # update max_profit dengan nilai tersebut
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        # Kembalikan nilai max_profit yang merupakan keuntungan maksimum yang bisa didapat
        return max_profit
