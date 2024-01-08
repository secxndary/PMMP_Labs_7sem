namespace PMMP_Lab1;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        buttonOpenImage = new Button();
        buttonCvtColor = new Button();
        buttonThreshold = new Button();
        buttonAdaptiveThreshold = new Button();
        buttonSaveImage = new Button();
        buttonOpenOriginalImage = new Button();
        buttonEqualizeHist = new Button();
        pictureBox = new PictureBox();
        ((System.ComponentModel.ISupportInitialize)pictureBox).BeginInit();
        SuspendLayout();
        // 
        // buttonOpenImage
        // 
        buttonOpenImage.Location = new Point(276, 120);
        buttonOpenImage.Name = "buttonOpenImage";
        buttonOpenImage.Size = new Size(165, 55);
        buttonOpenImage.TabIndex = 0;
        buttonOpenImage.Text = "Открыть фото с диска";
        buttonOpenImage.UseVisualStyleBackColor = true;
        buttonOpenImage.Click += buttonOpenImage_Click;
        // 
        // buttonCvtColor
        // 
        buttonCvtColor.Location = new Point(60, 86);
        buttonCvtColor.Name = "buttonCvtColor";
        buttonCvtColor.Size = new Size(165, 55);
        buttonCvtColor.TabIndex = 2;
        buttonCvtColor.Text = "Одноканальное изображение";
        buttonCvtColor.UseVisualStyleBackColor = true;
        buttonCvtColor.Click += buttonCvtColor_Click;
        // 
        // buttonThreshold
        // 
        buttonThreshold.Location = new Point(60, 161);
        buttonThreshold.Name = "buttonThreshold";
        buttonThreshold.Size = new Size(165, 55);
        buttonThreshold.TabIndex = 3;
        buttonThreshold.Text = "Бинарное методом отсечения порога";
        buttonThreshold.UseVisualStyleBackColor = true;
        buttonThreshold.Click += buttonThreshold_Click;
        // 
        // buttonAdaptiveThreshold
        // 
        buttonAdaptiveThreshold.Location = new Point(60, 238);
        buttonAdaptiveThreshold.Name = "buttonAdaptiveThreshold";
        buttonAdaptiveThreshold.Size = new Size(165, 55);
        buttonAdaptiveThreshold.TabIndex = 4;
        buttonAdaptiveThreshold.Text = "Адаптивная бинаризация";
        buttonAdaptiveThreshold.UseVisualStyleBackColor = true;
        buttonAdaptiveThreshold.Click += buttonAdaptiveThreshold_Click;
        // 
        // buttonSaveImage
        // 
        buttonSaveImage.Location = new Point(276, 195);
        buttonSaveImage.Name = "buttonSaveImage";
        buttonSaveImage.Size = new Size(165, 55);
        buttonSaveImage.TabIndex = 5;
        buttonSaveImage.Text = "Сохранить на диск";
        buttonSaveImage.UseVisualStyleBackColor = true;
        buttonSaveImage.Click += buttonSaveImage_Click;
        // 
        // buttonOpenOriginalImage
        // 
        buttonOpenOriginalImage.Location = new Point(276, 272);
        buttonOpenOriginalImage.Name = "buttonOpenOriginalImage";
        buttonOpenOriginalImage.Size = new Size(165, 55);
        buttonOpenOriginalImage.TabIndex = 6;
        buttonOpenOriginalImage.Text = "Открыть изначальное фото";
        buttonOpenOriginalImage.UseVisualStyleBackColor = true;
        buttonOpenOriginalImage.Click += buttonOpenOriginalImage_Click;
        // 
        // buttonEqualizeHist
        // 
        buttonEqualizeHist.Location = new Point(60, 320);
        buttonEqualizeHist.Name = "buttonEqualizeHist";
        buttonEqualizeHist.Size = new Size(165, 55);
        buttonEqualizeHist.TabIndex = 7;
        buttonEqualizeHist.Text = "Нормализовать гистограмму";
        buttonEqualizeHist.UseVisualStyleBackColor = true;
        buttonEqualizeHist.Click += buttonEqualizeHist_Click;
        // 
        // pictureBox
        // 
        pictureBox.Location = new Point(515, 106);
        pictureBox.Name = "pictureBox";
        pictureBox.Size = new Size(255, 255);
        pictureBox.TabIndex = 8;
        pictureBox.TabStop = false;
        // 
        // Form1
        // 
        AutoScaleDimensions = new SizeF(9F, 21F);
        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(832, 441);
        Controls.Add(pictureBox);
        Controls.Add(buttonEqualizeHist);
        Controls.Add(buttonOpenOriginalImage);
        Controls.Add(buttonSaveImage);
        Controls.Add(buttonAdaptiveThreshold);
        Controls.Add(buttonThreshold);
        Controls.Add(buttonCvtColor);
        Controls.Add(buttonOpenImage);
        Name = "Form1";
        StartPosition = FormStartPosition.CenterScreen;
        Text = "Form1";
        ((System.ComponentModel.ISupportInitialize)pictureBox).EndInit();
        ResumeLayout(false);
    }

    #endregion

    private Button buttonOpenImage;
    private Button buttonCvtColor;
    private Button buttonThreshold;
    private Button buttonAdaptiveThreshold;
    private Button buttonSaveImage;
    private Button buttonOpenOriginalImage;
    private Button buttonEqualizeHist;
    private PictureBox pictureBox;
}
