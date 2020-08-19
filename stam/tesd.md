# 계리모형론 문제 풀이

## 42회

----------

1.  

$$ 
    mle(\lambda) = ~? 
    \newline
    data = \{ 1,1,1,1+,4+,5,7,8,10,10+,12+,16+,16+,16+ \}
    \newline
    exp(\lambda)  = \lambda e^{-\lambda x}
    \newline
    n = 14
    \newline
    \displaystyle\prod_{k=1}^{n} f(x_{i}|\lambda)
    \newline
    f(x_{i}|\lambda ) = \lambda e^{-\lambda x_{i}} ~ if ~ not ~ censored
    \newline
    f(x_{i}|\lambda ) = \int_{x_{i}}^{\infty} \lambda e^{-\lambda x} dx ~ if ~ censored
    \newline
    = \int_{x_{i}}^{\infty} \lambda e^{-\lambda x} dx
    \newline
    = e^{-\lambda x_{i}}
    \newline
    n_{1} = 7 (number ~ of ~ complete)
    \newline
    n_{2} = 7 (number ~ of ~ censored)
    \newline
    \displaystyle\prod_{k=1}^{14} f(x_{i}|\lambda) = 
    \newline
    = \lambda^7 e^{-\lambda(\sum_{k=1}^{14} x_{i})} 
    \newline
    \sum_{k=1}^{14} x_{i} = 108
    \newline
    L(\lambda) = \lambda^7 e^{-108 \lambda}
    \newline
    L'(\lambda) = 7 \lambda^6 e^{-108 \lambda} - 108 \lambda^7 e^{-108 \lambda}
    \newline
    = \lambda^6 e^{-108 \lambda} (7 - 108 \lambda)
    \newline
    \lambda = \frac{7}{108} = 0.064815 \approx 0.065
    
$$

2. 

$$



$$


## 40 회


---------------

5. (1)
   
   베이지안 보험료 구하기

   (2)
   
   벨만 보험료 구하기

6. 