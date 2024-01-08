using System.Threading.Tasks;
using Unity.VisualScripting;
using UnityEngine;

public class GreenCapsule : MonoBehaviour
{
    public bool IsDestroyed = false;

    // Start is called before the first frame update
    async void Start()
    {
        await Task.Delay(5000);
        if(!IsDestroyed && gameObject != null)
            Destroy(gameObject);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
