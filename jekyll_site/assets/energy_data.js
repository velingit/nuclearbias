// This file contains time series data for all analyzed countries
// Format: { country: 'CountryName', data: [{Period, Nuclear_Generation_GWh, Household_Price_EUR_per_KWH, Industrial_Price_EUR_per_KWH}, ...] }
const energyData = [
  {
    "country": "Belgium",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 42720.0,
        "Household_Price_EUR_per_KWH": 0.11799999999999998,
        "Industrial_Price_EUR_per_KWH": 0.0581
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 42860.0,
        "Household_Price_EUR_per_KWH": 0.1155,
        "Industrial_Price_EUR_per_KWH": 0.0568
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 43460.0,
        "Household_Price_EUR_per_KWH": 0.1159,
        "Industrial_Price_EUR_per_KWH": 0.0563
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 41930.0,
        "Household_Price_EUR_per_KWH": 0.1169,
        "Industrial_Price_EUR_per_KWH": 0.057200000000000015
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 40620.0,
        "Household_Price_EUR_per_KWH": 0.11709999999999998,
        "Industrial_Price_EUR_per_KWH": 0.05539999999999999
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 41360.0,
        "Household_Price_EUR_per_KWH": 0.11879999999999999,
        "Industrial_Price_EUR_per_KWH": 0.055999999999999994
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 43340.0,
        "Household_Price_EUR_per_KWH": 0.1173,
        "Industrial_Price_EUR_per_KWH": 0.0559
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 47410.0,
        "Household_Price_EUR_per_KWH": 0.11900000000000001,
        "Industrial_Price_EUR_per_KWH": 0.0553
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 46170.0,
        "Household_Price_EUR_per_KWH": 0.12009999999999998,
        "Industrial_Price_EUR_per_KWH": 0.0552
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 49020.0,
        "Household_Price_EUR_per_KWH": 0.1166,
        "Industrial_Price_EUR_per_KWH": 0.052099999999999994
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 48160.0,
        "Household_Price_EUR_per_KWH": 0.1172,
        "Industrial_Price_EUR_per_KWH": 0.0518
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 45570.0,
        "Household_Price_EUR_per_KWH": 0.1366,
        "Industrial_Price_EUR_per_KWH": 0.08469999999999998
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 47220.0,
        "Household_Price_EUR_per_KWH": 0.1232,
        "Industrial_Price_EUR_per_KWH": 0.0915
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 47940.0,
        "Household_Price_EUR_per_KWH": 0.12739999999999999,
        "Industrial_Price_EUR_per_KWH": 0.08360000000000001
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 48230.0,
        "Household_Price_EUR_per_KWH": 0.1393,
        "Industrial_Price_EUR_per_KWH": 0.08795
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 40290.0,
        "Household_Price_EUR_per_KWH": 0.14425000000000002,
        "Industrial_Price_EUR_per_KWH": 0.08635
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 42640.0,
        "Household_Price_EUR_per_KWH": 0.14395,
        "Industrial_Price_EUR_per_KWH": 0.08074999999999999
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 33700.0,
        "Household_Price_EUR_per_KWH": 0.16146,
        "Industrial_Price_EUR_per_KWH": 0.09744
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 26100.0,
        "Household_Price_EUR_per_KWH": 0.17565999999999998,
        "Industrial_Price_EUR_per_KWH": 0.09494
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 43520.0,
        "Household_Price_EUR_per_KWH": 0.16913999999999998,
        "Industrial_Price_EUR_per_KWH": 0.09403
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 42230.0,
        "Household_Price_EUR_per_KWH": 0.18165818600000003,
        "Industrial_Price_EUR_per_KWH": 0.09006948
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 28600.0,
        "Household_Price_EUR_per_KWH": 0.19111762200000001,
        "Industrial_Price_EUR_per_KWH": 0.08638371399999999
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 43520.0,
        "Household_Price_EUR_per_KWH": 0.19292828000000004,
        "Industrial_Price_EUR_per_KWH": 0.090292432
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 34430.0,
        "Household_Price_EUR_per_KWH": 0.183790604,
        "Industrial_Price_EUR_per_KWH": 0.088890266
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 50330.0,
        "Household_Price_EUR_per_KWH": 0.19007074399999999,
        "Industrial_Price_EUR_per_KWH": 0.10052918500000001
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 43880.0,
        "Household_Price_EUR_per_KWH": 0.32373609099999995,
        "Industrial_Price_EUR_per_KWH": 0.180550046
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 32930.0,
        "Household_Price_EUR_per_KWH": 0.31683679800000003,
        "Industrial_Price_EUR_per_KWH": 0.189995317
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 31250.0,
        "Household_Price_EUR_per_KWH": 0.24359999999999998,
        "Industrial_Price_EUR_per_KWH": 0.14462
      }
    ]
  },
  {
    "country": "Finland",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 19220.0,
        "Household_Price_EUR_per_KWH": 0.0549,
        "Industrial_Price_EUR_per_KWH": 0.0406
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 19510.0,
        "Household_Price_EUR_per_KWH": 0.05629999999999999,
        "Industrial_Price_EUR_per_KWH": 0.0409
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 19260.0,
        "Household_Price_EUR_per_KWH": 0.0581,
        "Industrial_Price_EUR_per_KWH": 0.041499999999999995
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 19930.0,
        "Household_Price_EUR_per_KWH": 0.060899999999999996,
        "Industrial_Price_EUR_per_KWH": 0.04190000000000001
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 19430.0,
        "Household_Price_EUR_per_KWH": 0.0636,
        "Industrial_Price_EUR_per_KWH": 0.043500000000000004
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 19220.0,
        "Household_Price_EUR_per_KWH": 0.0655,
        "Industrial_Price_EUR_per_KWH": 0.0442
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 19480.0,
        "Household_Price_EUR_per_KWH": 0.0701,
        "Industrial_Price_EUR_per_KWH": 0.047799999999999995
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 20890.0,
        "Household_Price_EUR_per_KWH": 0.0665,
        "Industrial_Price_EUR_per_KWH": 0.0422
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 21850.0,
        "Household_Price_EUR_per_KWH": 0.06599999999999999,
        "Industrial_Price_EUR_per_KWH": 0.041299999999999996
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 22970.0,
        "Household_Price_EUR_per_KWH": 0.06330000000000001,
        "Industrial_Price_EUR_per_KWH": 0.0387
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 22480.0,
        "Household_Price_EUR_per_KWH": 0.0622,
        "Industrial_Price_EUR_per_KWH": 0.0376
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 22770.0,
        "Household_Price_EUR_per_KWH": 0.0634,
        "Industrial_Price_EUR_per_KWH": 0.0383
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 22300.0,
        "Household_Price_EUR_per_KWH": 0.06659999999999999,
        "Industrial_Price_EUR_per_KWH": 0.040999999999999995
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 22730.0,
        "Household_Price_EUR_per_KWH": 0.0737,
        "Industrial_Price_EUR_per_KWH": 0.0534
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 22720.0,
        "Household_Price_EUR_per_KWH": 0.074,
        "Industrial_Price_EUR_per_KWH": 0.05299999999999999
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 23270.0,
        "Household_Price_EUR_per_KWH": 0.072324,
        "Industrial_Price_EUR_per_KWH": 0.052107999999999995
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 23420.0,
        "Household_Price_EUR_per_KWH": 0.079558,
        "Industrial_Price_EUR_per_KWH": 0.057100000000000005
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 22960.0,
        "Household_Price_EUR_per_KWH": 0.08783000000000002,
        "Industrial_Price_EUR_per_KWH": 0.063639
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 23530.0,
        "Household_Price_EUR_per_KWH": 0.09366999999999999,
        "Industrial_Price_EUR_per_KWH": 0.067504
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 22800.0,
        "Household_Price_EUR_per_KWH": 0.09927000000000001,
        "Industrial_Price_EUR_per_KWH": 0.06898000000000001
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 23190.0,
        "Household_Price_EUR_per_KWH": 0.10778707300000001,
        "Industrial_Price_EUR_per_KWH": 0.07464434
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 22990.0,
        "Household_Price_EUR_per_KWH": 0.106227276,
        "Industrial_Price_EUR_per_KWH": 0.07379749700000002
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 23610.0,
        "Household_Price_EUR_per_KWH": 0.10585183499999999,
        "Industrial_Price_EUR_per_KWH": 0.073280675
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 23580.0,
        "Household_Price_EUR_per_KWH": 0.10335770200000001,
        "Industrial_Price_EUR_per_KWH": 0.06293460399999999
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 23250.0,
        "Household_Price_EUR_per_KWH": 0.100273085,
        "Industrial_Price_EUR_per_KWH": 0.060299928
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 23200.0,
        "Household_Price_EUR_per_KWH": 0.100993932,
        "Industrial_Price_EUR_per_KWH": 0.05888246400000001
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 22480.0,
        "Household_Price_EUR_per_KWH": 0.108096411,
        "Industrial_Price_EUR_per_KWH": 0.057538075999999994
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 22790.0,
        "Household_Price_EUR_per_KWH": 0.11357129,
        "Industrial_Price_EUR_per_KWH": 0.059464556
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 23870.0,
        "Household_Price_EUR_per_KWH": 0.125596694,
        "Industrial_Price_EUR_per_KWH": 0.06038422100000001
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 23290.0,
        "Household_Price_EUR_per_KWH": 0.12428600800000002,
        "Industrial_Price_EUR_per_KWH": 0.061395012
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 23600.0,
        "Household_Price_EUR_per_KWH": 0.131518811,
        "Industrial_Price_EUR_per_KWH": 0.070029912
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 25340.0,
        "Household_Price_EUR_per_KWH": 0.16278881199999998,
        "Industrial_Price_EUR_per_KWH": 0.10733275500000002
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 34310.0,
        "Household_Price_EUR_per_KWH": 0.178163214,
        "Industrial_Price_EUR_per_KWH": 0.08917244700000002
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 32600.0,
        "Household_Price_EUR_per_KWH": 0.1612,
        "Industrial_Price_EUR_per_KWH": 0.0765
      }
    ]
  },
  {
    "country": "France",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 314080.0,
        "Household_Price_EUR_per_KWH": 0.10149999999999999,
        "Industrial_Price_EUR_per_KWH": 0.046799999999999994
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 331340.0,
        "Household_Price_EUR_per_KWH": 0.09790000000000001,
        "Industrial_Price_EUR_per_KWH": 0.0463
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 338450.0,
        "Household_Price_EUR_per_KWH": 0.09929999999999999,
        "Industrial_Price_EUR_per_KWH": 0.046099999999999995
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 368190.0,
        "Household_Price_EUR_per_KWH": 0.1011,
        "Industrial_Price_EUR_per_KWH": 0.04719999999999999
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 359980.0,
        "Household_Price_EUR_per_KWH": 0.10149999999999999,
        "Industrial_Price_EUR_per_KWH": 0.045000000000000005
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 377230.0,
        "Household_Price_EUR_per_KWH": 0.0995,
        "Industrial_Price_EUR_per_KWH": 0.045799999999999993
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 397340.0,
        "Household_Price_EUR_per_KWH": 0.09790000000000003,
        "Industrial_Price_EUR_per_KWH": 0.0442
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 395480.0,
        "Household_Price_EUR_per_KWH": 0.0912,
        "Industrial_Price_EUR_per_KWH": 0.0434
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 387990.0,
        "Household_Price_EUR_per_KWH": 0.0888,
        "Industrial_Price_EUR_per_KWH": 0.042
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 394240.0,
        "Household_Price_EUR_per_KWH": 0.0889,
        "Industrial_Price_EUR_per_KWH": 0.0409
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 415160.0,
        "Household_Price_EUR_per_KWH": 0.087,
        "Industrial_Price_EUR_per_KWH": 0.0388
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 421080.0,
        "Household_Price_EUR_per_KWH": 0.0867,
        "Industrial_Price_EUR_per_KWH": 0.038799999999999994
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 436760.0,
        "Household_Price_EUR_per_KWH": 0.0875,
        "Industrial_Price_EUR_per_KWH": 0.038799999999999994
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 441070.0,
        "Household_Price_EUR_per_KWH": 0.08545,
        "Industrial_Price_EUR_per_KWH": 0.03625
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 448240.0,
        "Household_Price_EUR_per_KWH": 0.08549999999999999,
        "Industrial_Price_EUR_per_KWH": 0.0356
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 451530.0,
        "Household_Price_EUR_per_KWH": 0.0855,
        "Industrial_Price_EUR_per_KWH": 0.0356
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 450190.0,
        "Household_Price_EUR_per_KWH": 0.08609999999999998,
        "Industrial_Price_EUR_per_KWH": 0.035899999999999994
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 439730.0,
        "Household_Price_EUR_per_KWH": 0.08590000000000002,
        "Industrial_Price_EUR_per_KWH": 0.0602
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 439450.0,
        "Household_Price_EUR_per_KWH": 0.08449999999999999,
        "Industrial_Price_EUR_per_KWH": 0.06440000000000001
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 409740.0,
        "Household_Price_EUR_per_KWH": 0.086,
        "Industrial_Price_EUR_per_KWH": 0.069
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 428520.0,
        "Household_Price_EUR_per_KWH": 0.091007946,
        "Industrial_Price_EUR_per_KWH": 0.072103135
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 442390.0,
        "Household_Price_EUR_per_KWH": 0.094989709,
        "Industrial_Price_EUR_per_KWH": 0.07521696
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 425410.0,
        "Household_Price_EUR_per_KWH": 0.095084784,
        "Industrial_Price_EUR_per_KWH": 0.076602849
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 423680.0,
        "Household_Price_EUR_per_KWH": 0.09900610500000001,
        "Industrial_Price_EUR_per_KWH": 0.077721978
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 436480.0,
        "Household_Price_EUR_per_KWH": 0.10164519600000001,
        "Industrial_Price_EUR_per_KWH": 0.07870377499999999
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 437430.0,
        "Household_Price_EUR_per_KWH": 0.10617764099999999,
        "Industrial_Price_EUR_per_KWH": 0.079946912
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 403200.0,
        "Household_Price_EUR_per_KWH": 0.10504216499999999,
        "Industrial_Price_EUR_per_KWH": 0.074438789
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 398360.0,
        "Household_Price_EUR_per_KWH": 0.10596100699999998,
        "Industrial_Price_EUR_per_KWH": 0.07450223400000001
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 412940.0,
        "Household_Price_EUR_per_KWH": 0.10996296,
        "Industrial_Price_EUR_per_KWH": 0.076823103
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 399010.0,
        "Household_Price_EUR_per_KWH": 0.11514757199999999,
        "Industrial_Price_EUR_per_KWH": 0.083586946
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 353830.0,
        "Household_Price_EUR_per_KWH": 0.12376416600000002,
        "Industrial_Price_EUR_per_KWH": 0.08765686700000001
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 379360.0,
        "Household_Price_EUR_per_KWH": 0.128478965,
        "Industrial_Price_EUR_per_KWH": 0.093417858
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 294730.0,
        "Household_Price_EUR_per_KWH": 0.15899054799999998,
        "Industrial_Price_EUR_per_KWH": 0.124216566
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 338200.0,
        "Household_Price_EUR_per_KWH": 0.195929372,
        "Industrial_Price_EUR_per_KWH": 0.202213495
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 380450.0,
        "Household_Price_EUR_per_KWH": 0.21521,
        "Industrial_Price_EUR_per_KWH": 0.15122999999999998
      }
    ]
  },
  {
    "country": "Germany",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 152470.0,
        "Household_Price_EUR_per_KWH": 0.1097,
        "Industrial_Price_EUR_per_KWH": 0.0696
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 147230.0,
        "Household_Price_EUR_per_KWH": 0.1095,
        "Industrial_Price_EUR_per_KWH": 0.06870000000000001
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 158800.0,
        "Household_Price_EUR_per_KWH": 0.11179999999999998,
        "Industrial_Price_EUR_per_KWH": 0.06890000000000002
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 153280.0,
        "Household_Price_EUR_per_KWH": 0.11560000000000001,
        "Industrial_Price_EUR_per_KWH": 0.07029999999999999
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 150700.0,
        "Household_Price_EUR_per_KWH": 0.11870000000000001,
        "Industrial_Price_EUR_per_KWH": 0.0682
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 153090.0,
        "Household_Price_EUR_per_KWH": 0.11919999999999999,
        "Industrial_Price_EUR_per_KWH": 0.0674
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 160020.0,
        "Household_Price_EUR_per_KWH": 0.1206,
        "Industrial_Price_EUR_per_KWH": 0.06620000000000001
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 170330.0,
        "Household_Price_EUR_per_KWH": 0.12290000000000002,
        "Industrial_Price_EUR_per_KWH": 0.0637
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 161640.0,
        "Household_Price_EUR_per_KWH": 0.12340000000000001,
        "Industrial_Price_EUR_per_KWH": 0.06049999999999999
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 170000.0,
        "Household_Price_EUR_per_KWH": 0.1228,
        "Industrial_Price_EUR_per_KWH": 0.053399999999999996
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 169610.0,
        "Household_Price_EUR_per_KWH": 0.1129,
        "Industrial_Price_EUR_per_KWH": 0.044
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 171300.0,
        "Household_Price_EUR_per_KWH": 0.1191,
        "Industrial_Price_EUR_per_KWH": 0.049
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 164840.0,
        "Household_Price_EUR_per_KWH": 0.12400000000000001,
        "Industrial_Price_EUR_per_KWH": 0.0515
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 165060.0,
        "Household_Price_EUR_per_KWH": 0.13399999999999998,
        "Industrial_Price_EUR_per_KWH": 0.0579
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 167070.0,
        "Household_Price_EUR_per_KWH": 0.1372,
        "Industrial_Price_EUR_per_KWH": 0.0619
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 163050.0,
        "Household_Price_EUR_per_KWH": 0.14739999999999998,
        "Industrial_Price_EUR_per_KWH": 0.06760000000000001
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 167270.0,
        "Household_Price_EUR_per_KWH": 0.15230000000000002,
        "Industrial_Price_EUR_per_KWH": 0.0751
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 140530.0,
        "Household_Price_EUR_per_KWH": 0.16140000000000002,
        "Industrial_Price_EUR_per_KWH": 0.0795
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 134930.0,
        "Household_Price_EUR_per_KWH": 0.138,
        "Industrial_Price_EUR_per_KWH": 0.0838
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 140560.0,
        "Household_Price_EUR_per_KWH": 0.13755,
        "Industrial_Price_EUR_per_KWH": 0.0795
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 107970.0,
        "Household_Price_EUR_per_KWH": 0.14005,
        "Industrial_Price_EUR_per_KWH": 0.07974999999999999
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 99460.0,
        "Household_Price_EUR_per_KWH": 0.14365,
        "Industrial_Price_EUR_per_KWH": 0.0778
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 97290.0,
        "Household_Price_EUR_per_KWH": 0.1491,
        "Industrial_Price_EUR_per_KWH": 0.07749999999999999
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 97130.0,
        "Household_Price_EUR_per_KWH": 0.14375,
        "Industrial_Price_EUR_per_KWH": 0.06999999999999999
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 91790.0,
        "Household_Price_EUR_per_KWH": 0.1429,
        "Industrial_Price_EUR_per_KWH": 0.06955
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 84630.0,
        "Household_Price_EUR_per_KWH": 0.13849999999999998,
        "Industrial_Price_EUR_per_KWH": 0.0674
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 76320.0,
        "Household_Price_EUR_per_KWH": 0.1386,
        "Industrial_Price_EUR_per_KWH": 0.06365
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 76000.0,
        "Household_Price_EUR_per_KWH": 0.13785,
        "Industrial_Price_EUR_per_KWH": 0.06355
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 75070.0,
        "Household_Price_EUR_per_KWH": 0.13969999999999996,
        "Industrial_Price_EUR_per_KWH": 0.067
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 64379.99999999999,
        "Household_Price_EUR_per_KWH": 0.14404999999999998,
        "Industrial_Price_EUR_per_KWH": 0.07185
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 69130.0,
        "Household_Price_EUR_per_KWH": 0.15790000000000004,
        "Industrial_Price_EUR_per_KWH": 0.08154999999999998
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 34710.0,
        "Household_Price_EUR_per_KWH": 0.21159999999999998,
        "Industrial_Price_EUR_per_KWH": 0.1585
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 7220.0,
        "Household_Price_EUR_per_KWH": 0.29275,
        "Industrial_Price_EUR_per_KWH": 0.17975
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 0.0,
        "Household_Price_EUR_per_KWH": 0.28011,
        "Industrial_Price_EUR_per_KWH": 0.17786000000000002
      }
    ]
  },
  {
    "country": "Hungary",
    "data": [
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 13730.0,
        "Household_Price_EUR_per_KWH": 0.03895223585839476,
        "Industrial_Price_EUR_per_KWH": 0.050854307926237595
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 13960.0,
        "Household_Price_EUR_per_KWH": 0.03619146981962901,
        "Industrial_Price_EUR_per_KWH": 0.046364207282443656
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 13800.0,
        "Household_Price_EUR_per_KWH": 0.03529563681756218,
        "Industrial_Price_EUR_per_KWH": 0.04514126182456638
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 14050.0,
        "Household_Price_EUR_per_KWH": 0.03055606517251548,
        "Industrial_Price_EUR_per_KWH": 0.03897702801533471
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 14030.0,
        "Household_Price_EUR_per_KWH": 0.039914812293639135,
        "Industrial_Price_EUR_per_KWH": 0.03443869475335328
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 14180.0,
        "Household_Price_EUR_per_KWH": 0.04191662877025601,
        "Industrial_Price_EUR_per_KWH": 0.037941776042042075
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 13970.0,
        "Household_Price_EUR_per_KWH": 0.05323730287855131,
        "Industrial_Price_EUR_per_KWH": 0.04798922062320566
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 13950.0,
        "Household_Price_EUR_per_KWH": 0.05566851294051978,
        "Industrial_Price_EUR_per_KWH": 0.04995143177646339
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 14100.0,
        "Household_Price_EUR_per_KWH": 0.0608514567887382,
        "Industrial_Price_EUR_per_KWH": 0.05162674017730293
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 14180.0,
        "Household_Price_EUR_per_KWH": 0.0632707733498839,
        "Industrial_Price_EUR_per_KWH": 0.05286338459868035
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 14130.0,
        "Household_Price_EUR_per_KWH": 0.06812981122644518,
        "Industrial_Price_EUR_per_KWH": 0.05665141911764192
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 13950.0,
        "Household_Price_EUR_per_KWH": 0.07550127925684445,
        "Industrial_Price_EUR_per_KWH": 0.062324557359294354
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 11010.0,
        "Household_Price_EUR_per_KWH": 0.08063408285078903,
        "Industrial_Price_EUR_per_KWH": 0.06937707948204436
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 11910.0,
        "Household_Price_EUR_per_KWH": 0.08620244228550107,
        "Industrial_Price_EUR_per_KWH": 0.07368918453437995
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 13830.0,
        "Household_Price_EUR_per_KWH": 0.09499364436444126,
        "Industrial_Price_EUR_per_KWH": 0.07613856229088022
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 13460.0,
        "Household_Price_EUR_per_KWH": 0.09568162086077293,
        "Industrial_Price_EUR_per_KWH": 0.0826543306856982
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 14680.0,
        "Household_Price_EUR_per_KWH": 0.11463398865603637,
        "Industrial_Price_EUR_per_KWH": 0.09736633186661055
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 14820.0,
        "Household_Price_EUR_per_KWH": 0.12777284528105787,
        "Industrial_Price_EUR_per_KWH": 0.11503138898744382
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 15430.0,
        "Household_Price_EUR_per_KWH": 0.1211777346553665,
        "Industrial_Price_EUR_per_KWH": 0.11408269861167056
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 15760.0,
        "Household_Price_EUR_per_KWH": 0.1311240811463958,
        "Industrial_Price_EUR_per_KWH": 0.09793387597958547
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 15690.0,
        "Household_Price_EUR_per_KWH": 0.12326674260890526,
        "Industrial_Price_EUR_per_KWH": 0.09448997722733815
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 15790.0,
        "Household_Price_EUR_per_KWH": 0.12108838203229583,
        "Industrial_Price_EUR_per_KWH": 0.09628530744605537
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 15370.0,
        "Household_Price_EUR_per_KWH": 0.1046865289567586,
        "Industrial_Price_EUR_per_KWH": 0.09367276422847097
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 15650.0,
        "Household_Price_EUR_per_KWH": 0.0939322911949583,
        "Industrial_Price_EUR_per_KWH": 0.08525994622846801
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 15830.0,
        "Household_Price_EUR_per_KWH": 0.09090638364044357,
        "Industrial_Price_EUR_per_KWH": 0.08103829517167274
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 16050.0,
        "Household_Price_EUR_per_KWH": 0.08947379411781002,
        "Industrial_Price_EUR_per_KWH": 0.07354378815761524
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 16100.000000000002,
        "Household_Price_EUR_per_KWH": 0.09000935428454643,
        "Industrial_Price_EUR_per_KWH": 0.07122815770787516
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 15730.0,
        "Household_Price_EUR_per_KWH": 0.08769644842857251,
        "Industrial_Price_EUR_per_KWH": 0.07598849389499747
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 16290.0,
        "Household_Price_EUR_per_KWH": 0.08597516699485394,
        "Industrial_Price_EUR_per_KWH": 0.0744970129278494
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 16059.999999999998,
        "Household_Price_EUR_per_KWH": 0.07977657763923238,
        "Industrial_Price_EUR_per_KWH": 0.06526247460451678
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 15990.0,
        "Household_Price_EUR_per_KWH": 0.07862114823171687,
        "Industrial_Price_EUR_per_KWH": 0.07611240113713193
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 15810.0,
        "Household_Price_EUR_per_KWH": 0.0777045459363549,
        "Industrial_Price_EUR_per_KWH": 0.1877049965785572
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 15920.0,
        "Household_Price_EUR_per_KWH": 0.08801987241306838,
        "Industrial_Price_EUR_per_KWH": 0.20931135093843692
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 16020.0,
        "Household_Price_EUR_per_KWH": 0.08473510129316239,
        "Industrial_Price_EUR_per_KWH": 0.16488245181398148
      }
    ]
  },
  {
    "country": "Netherlands",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 3500.0,
        "Household_Price_EUR_per_KWH": 0.0817,
        "Industrial_Price_EUR_per_KWH": 0.0432
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 3330.0,
        "Household_Price_EUR_per_KWH": 0.08170000000000001,
        "Industrial_Price_EUR_per_KWH": 0.044899999999999995
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 3800.0,
        "Household_Price_EUR_per_KWH": 0.0803,
        "Industrial_Price_EUR_per_KWH": 0.0408
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 3950.0,
        "Household_Price_EUR_per_KWH": 0.081,
        "Industrial_Price_EUR_per_KWH": 0.05360000000000001
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 3970.0,
        "Household_Price_EUR_per_KWH": 0.081,
        "Industrial_Price_EUR_per_KWH": 0.0533
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 4019.9999999999995,
        "Household_Price_EUR_per_KWH": 0.0836,
        "Industrial_Price_EUR_per_KWH": 0.0543
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 4160.0,
        "Household_Price_EUR_per_KWH": 0.086,
        "Industrial_Price_EUR_per_KWH": 0.054700000000000006
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 2410.0,
        "Household_Price_EUR_per_KWH": 0.0873,
        "Industrial_Price_EUR_per_KWH": 0.0557
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 3810.0,
        "Household_Price_EUR_per_KWH": 0.08769999999999999,
        "Industrial_Price_EUR_per_KWH": 0.056100000000000004
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 3830.0,
        "Household_Price_EUR_per_KWH": 0.0884,
        "Industrial_Price_EUR_per_KWH": 0.0561
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 3930.0,
        "Household_Price_EUR_per_KWH": 0.0938,
        "Industrial_Price_EUR_per_KWH": 0.0596
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 3980.0,
        "Household_Price_EUR_per_KWH": 0.0927,
        "Industrial_Price_EUR_per_KWH": 0.059300000000000005
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 4200.0,
        "Household_Price_EUR_per_KWH": 0.13681200000000004,
        "Industrial_Price_EUR_per_KWH": 0.07830000000000001
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 4170.0,
        "Household_Price_EUR_per_KWH": 0.131851,
        "Industrial_Price_EUR_per_KWH": 0.08015
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 4250.0,
        "Household_Price_EUR_per_KWH": 0.153779,
        "Industrial_Price_EUR_per_KWH": 0.0889
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 3970.0,
        "Household_Price_EUR_per_KWH": 0.13511800000000002,
        "Industrial_Price_EUR_per_KWH": 0.07675
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 4140.0,
        "Household_Price_EUR_per_KWH": 0.137784615,
        "Industrial_Price_EUR_per_KWH": 0.07434999999999999
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 3910.0,
        "Household_Price_EUR_per_KWH": 0.14731009,
        "Industrial_Price_EUR_per_KWH": 0.0741
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 2890.0,
        "Household_Price_EUR_per_KWH": 0.14873010500000003,
        "Industrial_Price_EUR_per_KWH": 0.07395
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 4090.0,
        "Household_Price_EUR_per_KWH": 0.1438418,
        "Industrial_Price_EUR_per_KWH": 0.0719
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 4080.0,
        "Household_Price_EUR_per_KWH": 0.137296807,
        "Industrial_Price_EUR_per_KWH": 0.06655
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 3960.0,
        "Household_Price_EUR_per_KWH": 0.13228181,
        "Industrial_Price_EUR_per_KWH": 0.06135
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 3400.0,
        "Household_Price_EUR_per_KWH": 0.124346169,
        "Industrial_Price_EUR_per_KWH": 0.059750000000000004
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 3510.0,
        "Household_Price_EUR_per_KWH": 0.13274288599999998,
        "Industrial_Price_EUR_per_KWH": 0.059550000000000006
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 3910.0,
        "Household_Price_EUR_per_KWH": 0.152763616,
        "Industrial_Price_EUR_per_KWH": 0.0643
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 4090.0,
        "Household_Price_EUR_per_KWH": 0.146998922,
        "Industrial_Price_EUR_per_KWH": 0.06355
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 3830.0,
        "Household_Price_EUR_per_KWH": 0.162624433,
        "Industrial_Price_EUR_per_KWH": 0.07995000000000001
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 4160.0,
        "Household_Price_EUR_per_KWH": 0.29138000000000003,
        "Industrial_Price_EUR_per_KWH": 0.15569999999999998
      }
    ]
  },
  {
    "country": "Slovakia",
    "data": [
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 11490.0,
        "Household_Price_EUR_per_KWH": 0.029410000000000002,
        "Industrial_Price_EUR_per_KWH": 0.04822999999999999
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 12600.0,
        "Household_Price_EUR_per_KWH": 0.02928,
        "Industrial_Price_EUR_per_KWH": 0.04800000000000001
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 11440.0,
        "Household_Price_EUR_per_KWH": 0.029280000000000004,
        "Industrial_Price_EUR_per_KWH": 0.048
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 11250.0,
        "Household_Price_EUR_per_KWH": 0.030209999999999997,
        "Industrial_Price_EUR_per_KWH": 0.05018999999999999
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 11070.0,
        "Household_Price_EUR_per_KWH": 0.030900000000000004,
        "Industrial_Price_EUR_per_KWH": 0.0544
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 11390.0,
        "Household_Price_EUR_per_KWH": 0.0309,
        "Industrial_Price_EUR_per_KWH": 0.05679000000000001
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 13120.0,
        "Household_Price_EUR_per_KWH": 0.04392,
        "Industrial_Price_EUR_per_KWH": 0.05636000000000001
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 16490.0,
        "Household_Price_EUR_per_KWH": 0.06921,
        "Industrial_Price_EUR_per_KWH": 0.06420000000000002
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 17100.0,
        "Household_Price_EUR_per_KWH": 0.09079000000000001,
        "Industrial_Price_EUR_per_KWH": 0.06848
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 17950.0,
        "Household_Price_EUR_per_KWH": 0.09062,
        "Industrial_Price_EUR_per_KWH": 0.07094
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 17860.0,
        "Household_Price_EUR_per_KWH": 0.1112,
        "Industrial_Price_EUR_per_KWH": 0.08531000000000001
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 17030.0,
        "Household_Price_EUR_per_KWH": 0.12048999999999997,
        "Industrial_Price_EUR_per_KWH": 0.08863
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 17730.0,
        "Household_Price_EUR_per_KWH": 0.12181999999999998,
        "Industrial_Price_EUR_per_KWH": 0.08896
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 18010.0,
        "Household_Price_EUR_per_KWH": 0.12879000000000002,
        "Industrial_Price_EUR_per_KWH": 0.09659000000000001
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 15330.0,
        "Household_Price_EUR_per_KWH": 0.12921999999999997,
        "Industrial_Price_EUR_per_KWH": 0.11220000000000001
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 16700.0,
        "Household_Price_EUR_per_KWH": 0.131,
        "Industrial_Price_EUR_per_KWH": 0.12329999999999999
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 14080.0,
        "Household_Price_EUR_per_KWH": 0.13959999999999997,
        "Industrial_Price_EUR_per_KWH": 0.1402
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 14570.0,
        "Household_Price_EUR_per_KWH": 0.1351,
        "Industrial_Price_EUR_per_KWH": 0.12769999999999998
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 15410.0,
        "Household_Price_EUR_per_KWH": 0.144775,
        "Industrial_Price_EUR_per_KWH": 0.128275
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 15490.0,
        "Household_Price_EUR_per_KWH": 0.14887999999999998,
        "Industrial_Price_EUR_per_KWH": 0.13206
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 15720.0,
        "Household_Price_EUR_per_KWH": 0.149436075,
        "Industrial_Price_EUR_per_KWH": 0.134889975
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 15500.0,
        "Household_Price_EUR_per_KWH": 0.13439715000000002,
        "Industrial_Price_EUR_per_KWH": 0.11830062499999998
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 15150.0,
        "Household_Price_EUR_per_KWH": 0.12860800000000003,
        "Industrial_Price_EUR_per_KWH": 0.11636819999999999
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 14770.0,
        "Household_Price_EUR_per_KWH": 0.12797165,
        "Industrial_Price_EUR_per_KWH": 0.11171227500000001
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 15080.0,
        "Household_Price_EUR_per_KWH": 0.123042763,
        "Industrial_Price_EUR_per_KWH": 0.1129782
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 14840.0,
        "Household_Price_EUR_per_KWH": 0.12714775,
        "Industrial_Price_EUR_per_KWH": 0.11833999999999999
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 15280.0,
        "Household_Price_EUR_per_KWH": 0.13565899999999997,
        "Industrial_Price_EUR_per_KWH": 0.129855
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 15440.0,
        "Household_Price_EUR_per_KWH": 0.14458601300000004,
        "Industrial_Price_EUR_per_KWH": 0.12815871799999998
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 15730.0,
        "Household_Price_EUR_per_KWH": 0.139879268,
        "Industrial_Price_EUR_per_KWH": 0.13267986099999998
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 15920.0,
        "Household_Price_EUR_per_KWH": 0.160286368,
        "Industrial_Price_EUR_per_KWH": 0.24406882500000004
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 18330.0,
        "Household_Price_EUR_per_KWH": 0.16409758800000002,
        "Industrial_Price_EUR_per_KWH": 0.272778548
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 18230.0,
        "Household_Price_EUR_per_KWH": 0.18341999999999997,
        "Industrial_Price_EUR_per_KWH": 0.19225
      }
    ]
  },
  {
    "country": "Spain",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 54270.0,
        "Household_Price_EUR_per_KWH": 0.10389999999999999,
        "Industrial_Price_EUR_per_KWH": 0.05969999999999999
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 55580.0,
        "Household_Price_EUR_per_KWH": 0.1106,
        "Industrial_Price_EUR_per_KWH": 0.06409999999999999
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 55780.0,
        "Household_Price_EUR_per_KWH": 0.11389999999999999,
        "Industrial_Price_EUR_per_KWH": 0.0645
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 56060.0,
        "Household_Price_EUR_per_KWH": 0.1176,
        "Industrial_Price_EUR_per_KWH": 0.06470000000000001
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 55310.0,
        "Household_Price_EUR_per_KWH": 0.12209999999999999,
        "Industrial_Price_EUR_per_KWH": 0.0631
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 55460.0,
        "Household_Price_EUR_per_KWH": 0.1256,
        "Industrial_Price_EUR_per_KWH": 0.0567
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 56330.0,
        "Household_Price_EUR_per_KWH": 0.1251,
        "Industrial_Price_EUR_per_KWH": 0.05650000000000001
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 55300.0,
        "Household_Price_EUR_per_KWH": 0.12399999999999999,
        "Industrial_Price_EUR_per_KWH": 0.0533
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 58990.0,
        "Household_Price_EUR_per_KWH": 0.11390000000000002,
        "Industrial_Price_EUR_per_KWH": 0.0484
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 58850.0,
        "Household_Price_EUR_per_KWH": 0.1084,
        "Industrial_Price_EUR_per_KWH": 0.0437
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 62210.0,
        "Household_Price_EUR_per_KWH": 0.10429999999999999,
        "Industrial_Price_EUR_per_KWH": 0.044
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 63710.0,
        "Household_Price_EUR_per_KWH": 0.09949999999999999,
        "Industrial_Price_EUR_per_KWH": 0.043699999999999996
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 63020.0,
        "Household_Price_EUR_per_KWH": 0.0991,
        "Industrial_Price_EUR_per_KWH": 0.0489
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 61880.0,
        "Household_Price_EUR_per_KWH": 0.09960000000000001,
        "Industrial_Price_EUR_per_KWH": 0.0453
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 63610.0,
        "Household_Price_EUR_per_KWH": 0.100053,
        "Industrial_Price_EUR_per_KWH": 0.045863
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 57540.0,
        "Household_Price_EUR_per_KWH": 0.10137499999999999,
        "Industrial_Price_EUR_per_KWH": 0.063814
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 60130.0,
        "Household_Price_EUR_per_KWH": 0.10768200000000001,
        "Industrial_Price_EUR_per_KWH": 0.06924
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 55100.0,
        "Household_Price_EUR_per_KWH": 0.11194,
        "Industrial_Price_EUR_per_KWH": 0.06222
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 58970.0,
        "Household_Price_EUR_per_KWH": 0.1223,
        "Industrial_Price_EUR_per_KWH": 0.08143999999999998
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 52760.0,
        "Household_Price_EUR_per_KWH": 0.12535,
        "Industrial_Price_EUR_per_KWH": 0.07064000000000001
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 61990.0,
        "Household_Price_EUR_per_KWH": 0.15016999999999997,
        "Industrial_Price_EUR_per_KWH": 0.09473000000000002
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 57720.0,
        "Household_Price_EUR_per_KWH": 0.17111,
        "Industrial_Price_EUR_per_KWH": 0.10171999999999998
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 61470.0,
        "Household_Price_EUR_per_KWH": 0.17128126363920118,
        "Industrial_Price_EUR_per_KWH": 0.10359421333007873
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 56730.0,
        "Household_Price_EUR_per_KWH": 0.17834494709895363,
        "Industrial_Price_EUR_per_KWH": 0.10510767255363682
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 57310.0,
        "Household_Price_EUR_per_KWH": 0.19480713999999996,
        "Industrial_Price_EUR_per_KWH": 0.11172990799999999
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 57200.0,
        "Household_Price_EUR_per_KWH": 0.150929,
        "Industrial_Price_EUR_per_KWH": 0.10939322500000001
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 58630.0,
        "Household_Price_EUR_per_KWH": 0.19116646499999998,
        "Industrial_Price_EUR_per_KWH": 0.09961002
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 58040.0,
        "Household_Price_EUR_per_KWH": 0.202820066,
        "Industrial_Price_EUR_per_KWH": 0.09748504100000001
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 55770.0,
        "Household_Price_EUR_per_KWH": 0.20750102000000004,
        "Industrial_Price_EUR_per_KWH": 0.102740014
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 58350.0,
        "Household_Price_EUR_per_KWH": 0.202052826,
        "Industrial_Price_EUR_per_KWH": 0.104250348
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 58300.0,
        "Household_Price_EUR_per_KWH": 0.189599635,
        "Industrial_Price_EUR_per_KWH": 0.097766654
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 56560.0,
        "Household_Price_EUR_per_KWH": 0.21530189100000002,
        "Industrial_Price_EUR_per_KWH": 0.119129927
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 58590.0,
        "Household_Price_EUR_per_KWH": 0.30772356999999995,
        "Industrial_Price_EUR_per_KWH": 0.21690848099999996
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 56870.0,
        "Household_Price_EUR_per_KWH": 0.2437612,
        "Industrial_Price_EUR_per_KWH": 0.15299400900000001
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 54530.0,
        "Household_Price_EUR_per_KWH": 0.22742,
        "Industrial_Price_EUR_per_KWH": 0.1343
      }
    ]
  },
  {
    "country": "Switzerland",
    "data": [
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 26450.0,
        "Household_Price_EUR_per_KWH": 0.1123696902661421,
        "Industrial_Price_EUR_per_KWH": 0.07495598332398265
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 26810.0,
        "Household_Price_EUR_per_KWH": 0.11305530428143443,
        "Industrial_Price_EUR_per_KWH": 0.07539226673100338
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 27230.0,
        "Household_Price_EUR_per_KWH": 0.11573358004262704,
        "Industrial_Price_EUR_per_KWH": 0.07477016331375848
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 27490.0,
        "Household_Price_EUR_per_KWH": 0.10965683535493542,
        "Industrial_Price_EUR_per_KWH": 0.06970383471841335
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 26960.0,
        "Household_Price_EUR_per_KWH": 0.10660271897143575,
        "Industrial_Price_EUR_per_KWH": 0.06722577296011563
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 23340.0,
        "Household_Price_EUR_per_KWH": 0.1039732387221877,
        "Industrial_Price_EUR_per_KWH": 0.06483796998576177
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 27820.0,
        "Household_Price_EUR_per_KWH": 0.09790343379147011,
        "Industrial_Price_EUR_per_KWH": 0.06395510025598632
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 27920.0,
        "Household_Price_EUR_per_KWH": 0.09255510692931997,
        "Industrial_Price_EUR_per_KWH": 0.061125030328588875
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 27700.0,
        "Household_Price_EUR_per_KWH": 0.09808563621565056,
        "Industrial_Price_EUR_per_KWH": 0.06412806074330821
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 27690.0,
        "Household_Price_EUR_per_KWH": 0.10670208664027252,
        "Industrial_Price_EUR_per_KWH": 0.06435262492404013
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 26340.0,
        "Household_Price_EUR_per_KWH": 0.12306448347079697,
        "Industrial_Price_EUR_per_KWH": 0.08146369161791503
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 26710.0,
        "Household_Price_EUR_per_KWH": 0.1445899008299404,
        "Industrial_Price_EUR_per_KWH": 0.09119194866639549
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 25440.0,
        "Household_Price_EUR_per_KWH": 0.143321049696,
        "Industrial_Price_EUR_per_KWH": 0.097594414848
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 25990.0,
        "Household_Price_EUR_per_KWH": 0.1383546116504854,
        "Industrial_Price_EUR_per_KWH": 0.09615574433656958
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 27560.0,
        "Household_Price_EUR_per_KWH": 0.14115868852459015,
        "Industrial_Price_EUR_per_KWH": 0.09212808743169398
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 23090.0,
        "Household_Price_EUR_per_KWH": 0.16153843555093556,
        "Industrial_Price_EUR_per_KWH": 0.10002785862785864
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 21150.0,
        "Household_Price_EUR_per_KWH": 0.15826883248730964,
        "Industrial_Price_EUR_per_KWH": 0.10877827411167512
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 20380.0,
        "Household_Price_EUR_per_KWH": 0.15416600447482148,
        "Industrial_Price_EUR_per_KWH": 0.0963006821349454
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 25510.0,
        "Household_Price_EUR_per_KWH": 0.14686866471892746,
        "Industrial_Price_EUR_per_KWH": 0.0834843780438184
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 26420.0,
        "Household_Price_EUR_per_KWH": 0.15521016903113988,
        "Industrial_Price_EUR_per_KWH": 0.08629816923373226
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 24020.0,
        "Household_Price_EUR_per_KWH": 0.16131554206234341,
        "Industrial_Price_EUR_per_KWH": 0.08920292892654892
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 19360.0,
        "Household_Price_EUR_per_KWH": 0.16288140047678398,
        "Industrial_Price_EUR_per_KWH": 0.09553833023477121
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 24150.0,
        "Household_Price_EUR_per_KWH": 0.17962962130514862,
        "Industrial_Price_EUR_per_KWH": 0.10560582301671134
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 24360.0,
        "Household_Price_EUR_per_KWH": 0.24115927334902984,
        "Industrial_Price_EUR_per_KWH": 0.19837665265849086
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 24000.0,
        "Household_Price_EUR_per_KWH": 0.2924031818181818,
        "Industrial_Price_EUR_per_KWH": 0.24249318181818183
      }
    ]
  },
  {
    "country": "United Kingdom",
    "data": [
      {
        "Period": 1990,
        "Nuclear_Generation_GWh": 65750.0,
        "Household_Price_EUR_per_KWH": 0.09331365836330535,
        "Industrial_Price_EUR_per_KWH": 0.05568041383597531
      },
      {
        "Period": 1991,
        "Nuclear_Generation_GWh": 70540.0,
        "Household_Price_EUR_per_KWH": 0.10475033672715355,
        "Industrial_Price_EUR_per_KWH": 0.058654480101989245
      },
      {
        "Period": 1992,
        "Nuclear_Generation_GWh": 76810.0,
        "Household_Price_EUR_per_KWH": 0.10469488044231866,
        "Industrial_Price_EUR_per_KWH": 0.058585736206064325
      },
      {
        "Period": 1993,
        "Nuclear_Generation_GWh": 89350.0,
        "Household_Price_EUR_per_KWH": 0.0986929524082351,
        "Industrial_Price_EUR_per_KWH": 0.05831856278668438
      },
      {
        "Period": 1994,
        "Nuclear_Generation_GWh": 88280.0,
        "Household_Price_EUR_per_KWH": 0.09679173230558265,
        "Industrial_Price_EUR_per_KWH": 0.05652637166646026
      },
      {
        "Period": 1995,
        "Nuclear_Generation_GWh": 88960.0,
        "Household_Price_EUR_per_KWH": 0.09005146466782388,
        "Industrial_Price_EUR_per_KWH": 0.052389189900583874
      },
      {
        "Period": 1996,
        "Nuclear_Generation_GWh": 94670.0,
        "Household_Price_EUR_per_KWH": 0.09146387102583313,
        "Industrial_Price_EUR_per_KWH": 0.05150989510729041
      },
      {
        "Period": 1997,
        "Nuclear_Generation_GWh": 98150.0,
        "Household_Price_EUR_per_KWH": 0.1031973145945946,
        "Industrial_Price_EUR_per_KWH": 0.057090951351351345
      },
      {
        "Period": 1998,
        "Nuclear_Generation_GWh": 99490.0,
        "Household_Price_EUR_per_KWH": 0.10280906097189609,
        "Industrial_Price_EUR_per_KWH": 0.05807082406481739
      },
      {
        "Period": 1999,
        "Nuclear_Generation_GWh": 95130.0,
        "Household_Price_EUR_per_KWH": 0.10416756898168492,
        "Industrial_Price_EUR_per_KWH": 0.05982802066878113
      },
      {
        "Period": 2000,
        "Nuclear_Generation_GWh": 85060.0,
        "Household_Price_EUR_per_KWH": 0.11022074601672784,
        "Industrial_Price_EUR_per_KWH": 0.06012040691821519
      },
      {
        "Period": 2001,
        "Nuclear_Generation_GWh": 90090.0,
        "Household_Price_EUR_per_KWH": 0.10711236357859383,
        "Industrial_Price_EUR_per_KWH": 0.05371701116403955
      },
      {
        "Period": 2002,
        "Nuclear_Generation_GWh": 87850.0,
        "Household_Price_EUR_per_KWH": 0.10649671037431552,
        "Industrial_Price_EUR_per_KWH": 0.05125850633860926
      },
      {
        "Period": 2003,
        "Nuclear_Generation_GWh": 88690.0,
        "Household_Price_EUR_per_KWH": 0.09758259289449836,
        "Industrial_Price_EUR_per_KWH": 0.045104842937901464
      },
      {
        "Period": 2004,
        "Nuclear_Generation_GWh": 80000.0,
        "Household_Price_EUR_per_KWH": 0.10559226360826761,
        "Industrial_Price_EUR_per_KWH": 0.0501415776910768
      },
      {
        "Period": 2005,
        "Nuclear_Generation_GWh": 81620.0,
        "Household_Price_EUR_per_KWH": 0.11525636287718587,
        "Industrial_Price_EUR_per_KWH": 0.06669657547207711
      },
      {
        "Period": 2006,
        "Nuclear_Generation_GWh": 75450.0,
        "Household_Price_EUR_per_KWH": 0.13597184424639613,
        "Industrial_Price_EUR_per_KWH": 0.0897291014435998
      },
      {
        "Period": 2007,
        "Nuclear_Generation_GWh": 63030.0,
        "Household_Price_EUR_per_KWH": 0.14221252251713237,
        "Industrial_Price_EUR_per_KWH": 0.09179716737666678
      },
      {
        "Period": 2008,
        "Nuclear_Generation_GWh": 52490.0,
        "Household_Price_EUR_per_KWH": 0.1419546491713831,
        "Industrial_Price_EUR_per_KWH": 0.09688411072706969
      },
      {
        "Period": 2009,
        "Nuclear_Generation_GWh": 69100.0,
        "Household_Price_EUR_per_KWH": 0.13106946617928616,
        "Industrial_Price_EUR_per_KWH": 0.09359940171280673
      },
      {
        "Period": 2010,
        "Nuclear_Generation_GWh": 62140.0,
        "Household_Price_EUR_per_KWH": 0.131646395888777,
        "Industrial_Price_EUR_per_KWH": 0.08831118712251919
      },
      {
        "Period": 2011,
        "Nuclear_Generation_GWh": 68980.0,
        "Household_Price_EUR_per_KWH": 0.14258441214542672,
        "Industrial_Price_EUR_per_KWH": 0.09005971792244102
      },
      {
        "Period": 2012,
        "Nuclear_Generation_GWh": 70410.0,
        "Household_Price_EUR_per_KWH": 0.16136900562650508,
        "Industrial_Price_EUR_per_KWH": 0.10120030773183072
      },
      {
        "Period": 2013,
        "Nuclear_Generation_GWh": 70610.0,
        "Household_Price_EUR_per_KWH": 0.164918765625,
        "Industrial_Price_EUR_per_KWH": 0.1017542912859375
      },
      {
        "Period": 2014,
        "Nuclear_Generation_GWh": 63750.0,
        "Household_Price_EUR_per_KWH": 0.18207795716639213,
        "Industrial_Price_EUR_per_KWH": 0.11340284962767712
      },
      {
        "Period": 2015,
        "Nuclear_Generation_GWh": 70340.0,
        "Household_Price_EUR_per_KWH": 0.19747605504587154,
        "Industrial_Price_EUR_per_KWH": 0.1274172184740061
      },
      {
        "Period": 2016,
        "Nuclear_Generation_GWh": 71730.0,
        "Household_Price_EUR_per_KWH": 0.1750051282051282,
        "Industrial_Price_EUR_per_KWH": 0.1090019800917679
      },
      {
        "Period": 2017,
        "Nuclear_Generation_GWh": 70340.0,
        "Household_Price_EUR_per_KWH": 0.17335138927305963,
        "Industrial_Price_EUR_per_KWH": 0.10728280876501883
      },
      {
        "Period": 2018,
        "Nuclear_Generation_GWh": 65060.0,
        "Household_Price_EUR_per_KWH": 0.1848137663625895,
        "Industrial_Price_EUR_per_KWH": 0.11332673806045146
      },
      {
        "Period": 2019,
        "Nuclear_Generation_GWh": 56180.0,
        "Household_Price_EUR_per_KWH": 0.19892622750456254,
        "Industrial_Price_EUR_per_KWH": 0.12483322358812361
      },
      {
        "Period": 2020,
        "Nuclear_Generation_GWh": 50240.0,
        "Household_Price_EUR_per_KWH": 0.19669804797693313,
        "Industrial_Price_EUR_per_KWH": 0.12846021374420355
      },
      {
        "Period": 2021,
        "Nuclear_Generation_GWh": 46100.0,
        "Household_Price_EUR_per_KWH": 0.22460812116391315,
        "Industrial_Price_EUR_per_KWH": 0.15178770099774477
      },
      {
        "Period": 2022,
        "Nuclear_Generation_GWh": 47400.0,
        "Household_Price_EUR_per_KWH": 0.3577530976675818,
        "Industrial_Price_EUR_per_KWH": 0.21176334982551284
      },
      {
        "Period": 2023,
        "Nuclear_Generation_GWh": 40600.0,
        "Household_Price_EUR_per_KWH": 0.3930231450992287,
        "Industrial_Price_EUR_per_KWH": 0.2926532904206838
      },
      {
        "Period": 2024,
        "Nuclear_Generation_GWh": 40590.0,
        "Household_Price_EUR_per_KWH": 0.3420394871794872,
        "Industrial_Price_EUR_per_KWH": 0.2937866666666667
      }
    ]
  }
];
