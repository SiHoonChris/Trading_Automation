Before Starting
- Take a glance at the file in the link below and the others too
  ( "FX_automation.py" ; https://github.com/SiHoonChris/Mercenary_Chris )
- This TEXT will be edited whenever I work with my source code
- This TEXT will be uploaded as "README.md" file after all the works are done

0. Cautions (For someone intersted in my tool or willing to use it for their own purpose)
   0-1.  Be aware of imperfectness ; of codes, as an indicator
   0-2.  The charts and its indicators, using the "past" datas, merely show you the "present" state of one asset,
         not the "future" of it.
   0-3.  The charts and indicators are only effective for setting own criteria when to buy or sell. 
   0-4.  "Fundamental Analysis" must precede "Technical Analysis." 

----------------------------------------------------------------------------------------------------
SEQUENCE of DEVELOPMENT
   0. Cautions
   1. Design the New Technical Analysis Tool
   2. Think of the Proper Strategy with the Tool
   3. Back-Test
   4. Apply New Tool to trade (for real) 


1.  Design the New Technical Analysis Tool
   1-1.  Develop new tool using :  a) SMA_Band(SMA&ATR) ,  b) Bollinger Band ,  c) Ichimoku Cloud
      1-1-a.  SMA_Band
         a-1.
            SMA = (A1+A2+...+An) / n
            where :
            SMA = Simple Moving Average
            An = the price of an asset as period n
            n = the number of total periods
         a-2.
            TR = Max[(H - L), Abs(H - Cp), Abs(L - Cp)]
            TR1 = H - L
                        (n)
            ATR = (1/n)  ∑ TRi
                       (i=1)
            where :
            TR = True Range
            ATR = Average True Range
            H = Highest Price
            L = Lowest Price
            Cp = (Previous) Closing Price
            TRi = A particular true range
            n = The time period employed
            * Don't ever be messed with the calculation of J. Welles Wilder Jr., which is ; ATRi-1*((n-1)/n) + TRi*(1/n)
            * Every ATR values are calculated within the formula above stirctly. 
         a-3.
            SMA_ML = SMA_MidLine
            SMA_UL = SMA_UpperLine = SMA + ATR
            SMA_LL = SMA_LowerLine = SMA - ATR
            where :
            n in (1) = n in (2) =250
            * 250(days) = 365(days in a year) - 104(Weekends ; 2days * 52weeks) - 11(Assumption ; DayOffs such as Independence Day)
         a-4.  What SMA_Band tells you / How to use SMA_Band
            (1)  SMA-Band are made up of 3 lines ; SMA-ML, SMA-UL, SMA-LL.
                  If the Closing Price is higher than SMA-UL, it means the Closing Price is much more expensive than the price of 250-day average.
                  If the Closing Price is lower than SMA-LL, it means the Closing Price is much cheaper than the price of 250-day average.
            (2)  ATR means how volatile the price changing is.
                  So that the width of SMA-Band tells you its volatilities. 
                  It means the volatility become greater if its width has become wider. - Vice Versa. 
            (3)  So if you can find the chart of one asset with upward-sloping SMA_Band and SMA_Band is relatively narrow in the chart,
                  The tool(indicator) tells you its price has been steadly increased with less volatility for a longer period
      1-1-b.  Bollinger_Band
         b-1.
            BOLU=MA(TP,n)+m∗σ[TP,n]
            BOLD=MA(TP,n)−m∗σ[TP,n]
            where :
            BOLU = Upper Bollinger Band
            BOLD = Lower Bollinger Band
            MA = Moving Average
            TP (Typical Price) = (High+Low+Close)÷3
            n = Number of days in smoothing period (typically 20)
            m = Number of standard deviations (typically 2)
            σ[TP,n] = Population Standard Deviation over last n periods of TP
      1-1-c.  Ichimoku Cloud
         c-1.
            Conversion Line (tenkan sen) = (9_PH + 9_PL) / 2 
            Base Line (kijun sen) = (26_PH + 26_PL) / 2 
            Leading Span A (senkou span A) = (CL + BL) / 2 
            Leading Span B (senkou span B) = (52_PH + 52_PL) / 2
​            Lagging Span (chikou span) = Closing_Price plotted 26 periods in the past
            where:
            PH=Period High (Highest Price among the prices including opening, closing, highest, lowest of each days)
            PL=Period Low (Lowest Price among the prices including opening, closing, highest, lowest of each days)
            CL=Conversion Line
            BL=Base Line
​            * Leading Span A, B are plotted 26 periods into the future.
   1-2.  What does the "new technical analysis tool" look like?
      1-2-a.  This tool draws 2 vertical lines and fills the color between them ; which is red or blue.
               One is drawn when the candle has penetrated the Ichimoku Cloud by its closing price.
               The other is drawn when Bollinger Band show its peak or valley.
               And then, add 1 horizontal line more which indicate the highest/lowest price between 2 vertical lines
               Explaining it in detail ; 
         a-1.  When it comes to RED ;
                 The RED column is made up of 3 lines, which are start_line, end_line and horizontal_line.
                 Start_line is drawn when the candle penetrate the upper line of Ichimoku Cloud with its closing price
                 End_line is drawn on the peak of Upper Bollinger Band when it has shown its peak after 'start_line' has been drawn.
                 Horizontal_line is drawn to indicate the highest price in the period(between start_line and end_line, including its start and end)
                 (and the color of horizontal_line is green)
         a-2.  When it comes to BLUE ;
                 The BLUE column, also, is made up of 3 lines, which are start_line, end_line and horizontal_line.
                 Start_line is drawn when the candle penetrate the lower line of Ichimoku Cloud with its closing price
                 End_line is drawn on the valley of Lower Bollinger Band when it has shown its valley after 'start_line' has been drawn.
                 Horizontal_line is drawn to indicate the lowest price in the period(between start_line and end_line, including its start and end)
                 (and the color of horizontal_line is yellow) 
   1-3.  What THESE tells you / How to use THEM
      1-3-a.  Remember the colors of vertical lines in the columns.
         a-1.  When the closing price becomes higher than the recent green vertical line after the red column has been drawn, 
                it tells you that the trend of moving upward has been confirmed with higher probability
         a-2.  When the closing price becomes lower than the recent yellow vertical line after the blue column has been drawn, 
                it tells you that the trend of moving downward has been confirmed with higher probability
         a-3.  When new column has been drawn before the closing price pass the value of vertical line, then follow that new one. 
                Make your decision using the last one. 

2.  Think of the Proper Strategy with the Tool
   2-1.  When to BUY & SELL


3. Back-Test


4. Apply new tool to trade (for real) 


----------------------------------------------------------------------------------------------------
HISTORY
08-28-2022  START THE PROJECT
09-18-2022  CREATE EXCLUSIVE REPOSITORY FOR THIS PROJECT 
09-20-2022  EDITING ON PENETRATING SITUATION
09-21-2022  ADDITIONAL EDITING ON PENETRATING SITUATION
            REMOVING OVERLAPPED COLUMNS
09-22-2022  ADDITIONAL EDITING ON REMOVING OVERLAPPED COLUMNS
