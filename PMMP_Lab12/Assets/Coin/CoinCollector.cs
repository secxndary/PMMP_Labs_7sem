using UnityEngine;

public class CoinCollector : MonoBehaviour
{
    void OnTriggerEnter(Collider other)
    {
        print(other.gameObject.tag);
        if(other.gameObject.tag == "Player")
        {
            var coinStore = other.gameObject.GetComponent<CoinStore>();
            coinStore.AddCoins(1);
            Destroy(gameObject);
        }
    }
}
