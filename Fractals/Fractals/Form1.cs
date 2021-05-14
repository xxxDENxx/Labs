using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace Fractals
{
    public partial class Form1 : Form
    {
        PointF[] start = new PointF[3];
        PointF[] Fr1 = new PointF[12];
        PointF[] Fr2 = new PointF[48];
        PointF[] Fr3 = new PointF[192];
        PointF[] Fr4 = new PointF[768];
        PointF[] Fr5 = new PointF[3072];
        PointF[] Fr6 = new PointF[12288];
        PointF[] Fr7 = new PointF[49152];
        public Form1()
        {
            InitializeComponent();
            start[0].X = (float)panel1.ClientSize.Width * 3 / 10;
            start[0].Y = (float)panel1.ClientSize.Height * 7 / 10;
            start[1].X = (float)panel1.ClientSize.Width * 7 / 10;
            start[1].Y = start[0].Y;
            start[2].X = (float)(start[0].X + start[1].X) / 2;
            var a = (float)start[1].X - start[0].X;
            var h = (float)Math.Sqrt(a * a - (a * a) / 4);
            start[2].Y = (float)start[0].Y - h;
            panel1.Invalidate();
        }
        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            if (numericUpDown1.Value == 0)
            { DrawLine(start, start, 0); }
            else if (numericUpDown1.Value == 1)
            { DrawLine(Fr1, start, 1); }
            else if (numericUpDown1.Value == 2)
            { DrawLine(Fr2, Fr1, 2); }
            else if (numericUpDown1.Value == 3)
            { DrawLine(Fr3, Fr2, 3); }
            else if (numericUpDown1.Value == 4)
            { DrawLine(Fr4, Fr3, 4); }
            else if (numericUpDown1.Value == 5)
            { DrawLine(Fr5, Fr4, 5); }
            else if (numericUpDown1.Value == 6)
            { DrawLine(Fr6, Fr5, 6); }
            else if (numericUpDown1.Value == 7)
            { DrawLine(Fr7, Fr6, 7); }
        }
        void DrawLine(PointF[] fractal, PointF[] polygon, int i)
        {
            if (i != 0)
            {
                var flen = fractal.Length;
                for (int j = 0; j < polygon.Length; j++)
                {
                    fractal[j * 4] = polygon[j];
                }
                for (int j = 0; j < fractal.Length; j += 4)
                {
                    var k = j + 1;
                    if (fractal[(j + 4) % flen].X > fractal[j].X && fractal[(j + 4) % flen].Y == fractal[j].Y)
                    {
                        fractal[k].Y = fractal[j].Y;
                        fractal[k + 2].Y = fractal[j].Y;
                        var b = (float)fractal[(j + 4) % flen].X - fractal[j].X;
                        fractal[k].X = (float)b / 3 + fractal[j].X;
                        fractal[k + 2].X = (float)b * 2 / 3 + fractal[j].X;
                        fractal[k + 1].X = (float)(fractal[k + 2].X + fractal[k].X) / 2;
                        var a = (float)fractal[k + 2].X - fractal[k].X;
                        var h = (float)Math.Sqrt(a * a - (a * a) / 4);
                        fractal[k + 1].Y = (float)fractal[j].Y + h;
                    }
                    else if (fractal[(j + 4) % flen].X < fractal[j].X && fractal[(j + 4) % flen].Y < fractal[j].Y)
                    {
                        var b = fractal[j].X - fractal[(j + 4) % flen].X;
                        var h = (float)Math.Sqrt(4 * b * b - b * b);
                        fractal[k].X = (float)fractal[(j + 4) % flen].X + 2 * b / 3;
                        fractal[k].Y = (float)fractal[(j + 4) % flen].Y + 2 * h / 3;
                        fractal[k + 2].X = (float)fractal[(j + 4) % flen].X + b / 3;
                        fractal[k + 2].Y = (float)fractal[(j + 4) % flen].Y + h / 3;
                        fractal[k + 1].X = fractal[j].X;
                        fractal[k + 1].Y = fractal[k + 2].Y;
                    }
                    else if (fractal[(j + 4) % flen].X < fractal[j].X && fractal[(j + 4) % flen].Y > fractal[j].Y)
                    {
                        var b = fractal[j].X - fractal[(j + 4) % flen].X;
                        var h = (float)Math.Sqrt(4 * b * b - b * b);
                        fractal[k].X = (float)fractal[(j + 4) % flen].X + 2 * b / 3;
                        fractal[k].Y = (float)fractal[(j + 4) % flen].Y - 2 * h / 3;
                        fractal[k + 2].X = (float)fractal[(j + 4) % flen].X + b / 3;
                        fractal[k + 2].Y = (float)fractal[(j + 4) % flen].Y - h / 3;
                        fractal[k + 1].X = fractal[(j + 4) % flen].X;
                        fractal[k + 1].Y = fractal[k].Y;
                    }
                    else if (fractal[(j + 4) % flen].X > fractal[j].X && fractal[(j + 4) % flen].Y > fractal[j].Y)
                    {
                        var b = fractal[(j + 4) % flen].X - fractal[j].X;
                        var h = (float)Math.Sqrt(4 * b * b - b * b);
                        fractal[k].X = (float)fractal[(j + 4) % flen].X - 2 * b / 3;
                        fractal[k].Y = (float)fractal[(j + 4) % flen].Y - 2 * h / 3;
                        fractal[k + 2].X = (float)fractal[(j + 4) % flen].X - b / 3;
                        fractal[k + 2].Y = (float)fractal[(j + 4) % flen].Y - h / 3;
                        fractal[k + 1].X = fractal[j].X;
                        fractal[k + 1].Y = fractal[k + 2].Y;
                    }
                    else if (fractal[(j + 4) % flen].X > fractal[j].X && fractal[(j + 4) % flen].Y < fractal[j].Y)
                    {
                        var b = fractal[(j + 4) % flen].X - fractal[j].X;
                        var h = (float)Math.Sqrt(4 * b * b - b * b);
                        fractal[k].X = (float)fractal[(j + 4) % flen].X - 2 * b / 3;
                        fractal[k].Y = (float)fractal[(j + 4) % flen].Y + 2 * h / 3;
                        fractal[k + 2].X = (float)fractal[(j + 4) % flen].X - b / 3;
                        fractal[k + 2].Y = (float)fractal[(j + 4) % flen].Y + h / 3;
                        fractal[k + 1].X = fractal[(j + 4) % flen].X;
                        fractal[k + 1].Y = fractal[k].Y;
                    }
                    else if (fractal[(j + 4) % flen].X < fractal[j].X && fractal[(j + 4) % flen].Y == fractal[j].Y)
                    {
                        fractal[k].Y = fractal[j].Y;
                        fractal[k + 2].Y = fractal[j].Y;
                        var b = (float)fractal[j].X - fractal[(j + 4) % flen].X;
                        fractal[k].X = (float)fractal[j].X - b / 3;
                        fractal[k + 2].X = (float)fractal[j].X - b * 2 / 3;
                        fractal[k + 1].X = (float)(fractal[k + 2].X + fractal[k].X) / 2;
                        var a = (float)fractal[k].X - fractal[k + 2].X;
                        var h = (float)Math.Sqrt(a * a - (a * a) / 4);
                        fractal[k + 1].Y = (float)fractal[j].Y - h;
                    }
                }
            }
            Graphics formGraphics;
            formGraphics = this.panel1.CreateGraphics();
            Pen pen = new Pen(Color.Blue, 2);
            for (int j = 0; j < fractal.Length; j++)
            {
                formGraphics.DrawLine(pen, fractal[j], fractal[(j + 1) % fractal.Length]);
            }
        }
        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            panel1.Invalidate();
        }
    }
}
