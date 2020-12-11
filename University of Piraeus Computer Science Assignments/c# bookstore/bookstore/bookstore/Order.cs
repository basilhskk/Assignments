using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace bookstore
{
    public partial class Order : Form
    {
        public Order()
        {
            InitializeComponent();
        }

        double price1 = 0;
        double price2 = 0;
        double price3 = 0;
        double price4 = 0;
        double price5 = 0;
        double price6 = 0;
        double price7 = 0;
        double price8 = 0;
        double total = 0;

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown1.Value);
            price1 = Convert.ToDouble((1.00) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown2.Value);
            price2 = Convert.ToDouble((1.20) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown3_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown3.Value);
            price3 = Convert.ToDouble((1.50) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown4_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown4.Value);
            price4 = Convert.ToDouble((1.40) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown5_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown5.Value);
            price5 = Convert.ToDouble((1.60) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown6_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown6.Value);
            price6 = Convert.ToDouble((1.80) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown7_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown7.Value);
            price7 = Convert.ToDouble((1.80) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void numericUpDown8_ValueChanged(object sender, EventArgs e)
        {
            int number = Convert.ToInt32(numericUpDown8.Value);
            price8 = Convert.ToDouble((1.80) * number);
            label10.Text = "Your total is " + (price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8).ToString() + " $";
        }

        private void continuebutton_Click(object sender, EventArgs e)
        {
            total = price1 + price2 + price3 + price4 + price5 + price6 + price7 + price8;
            if (total != 0)
            {
                Pay pay = new Pay(total.ToString());
                pay.ShowDialog();
            }
            else
            {
                MessageBox.Show("Select at least one coffee to continue!", "Error");
            }
        }

        private void backbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
