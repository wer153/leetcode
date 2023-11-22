from itertools import accumulate

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # solution1
        # 1 m, mo, mou, mous, ... 와 같은 규칙으로 문자를 누적시키며 순회한다.
        # 2 현재의 문자열로 시작하는 products만 필터링하고 사전순으로 정렬한다.
        answers = []
        products.sort()
        for prefix in accumulate(searchWord):
            # if all(product.startswith(prefix) for product in products[:3]):
            #     answers.append(products[:3])
            # else:
                products = [product for product in products if product.startswith(prefix)]
                answers.append(products[:3])
        return answers
                
                
        