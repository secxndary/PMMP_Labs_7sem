using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
namespace PMMP_Lab1;

public partial class Form1 : Form
{
    private Image<Bgr, byte>? _originalImage;

    public Form1()
    {
        InitializeComponent();
    }

    private void buttonOpenImage_Click(object sender, EventArgs e)
    {
        using var dialog = new OpenFileDialog();
        dialog.Title = "Open Image";
        dialog.Filter = "Image Files (*.bmp;*.jpg;*.jpeg,*.png)|*.BMP;*.JPG;*.JPEG;*.PNG";

        if (dialog.ShowDialog() == DialogResult.OK)
        {
            _originalImage = new Image<Bgr, byte>(dialog.FileName);
            SetPictureBoxImage(_originalImage.ToBitmap());
        }
    }

    private void buttonCvtColor_Click(object sender, EventArgs e)
    {
        if (_originalImage is null)
            return;

        var grayImage = _originalImage.Convert<Gray, byte>();
        SetPictureBoxImage(grayImage.ToBitmap());
    }

    private void buttonThreshold_Click(object sender, EventArgs e)
    {
        if (_originalImage is null)
            return;

        var grayImage = _originalImage.Convert<Gray, byte>();
        grayImage = grayImage.ThresholdBinary(new Gray(128), new Gray(255));

        SetPictureBoxImage(grayImage.ToBitmap());
    }

    private void buttonAdaptiveThreshold_Click(object sender, EventArgs e)
    {
        if (_originalImage is null)
            return;

        var grayImage = _originalImage.Convert<Gray, byte>();
        grayImage = grayImage.ThresholdAdaptive(new Gray(255), AdaptiveThresholdType.GaussianC,
            ThresholdType.Binary, 11, new Gray(2));

        SetPictureBoxImage(grayImage.ToBitmap());
    }

    private void buttonEqualizeHist_Click(object sender, EventArgs e)
    {
        if (_originalImage is null)
            return;

        var grayImage = _originalImage.Convert<Gray, byte>();
        grayImage._EqualizeHist();

        SetPictureBoxImage(grayImage.ToBitmap());
    }

    private void buttonSaveImage_Click(object sender, EventArgs e)
    {
        if (_originalImage is null)
            return;

        using var dialog = new SaveFileDialog();
        dialog.Title = "Save Image";
        dialog.Filter = "JPEG Image|*.jpg|Bitmap Image|*.bmp|PNG Image|*.png";

        if (dialog.ShowDialog() == DialogResult.OK)
            pictureBox.Image.Save(dialog.FileName);
    }

    private void buttonOpenOriginalImage_Click(object sender, EventArgs e)
    {
        if (_originalImage != null)
            SetPictureBoxImage(_originalImage.ToBitmap());
    }

    private void SetPictureBoxImage(Bitmap image)
    {
        pictureBox.Image = image;
        pictureBox.SizeMode = PictureBoxSizeMode.StretchImage;
    }
}
