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
    public partial class Pay : Form
    {
        public Pay(string billtotal)
        {
            InitializeComponent();

            dateTimePicker1.Format = DateTimePickerFormat.Custom;
            dateTimePicker1.CustomFormat = "MM / yyyy";
            dateTimePicker1.ShowUpDown = true;
            dateTimePicker1.MaxDate = DateTime.Now;

            textBox2.MaxLength = 16;
            textBox4.MaxLength = 3;
            totallabel.Text = billtotal + " $";
        }

        private void textBox2_KeyPress(object sender, KeyPressEventArgs e)
        {
            char ch = e.KeyChar;
            if (!char.IsDigit(ch) && ch != 8 && ch != 46)
            {
                e.Handled = true;
            }
        }
        
        private void textBox4_KeyPress(object sender, KeyPressEventArgs e)
        {
            char ch = e.KeyChar;
            if(!char.IsDigit(ch) && ch != 8 && ch != 46 )
            {
                e.Handled = true;
            }
        }

        private void paybutton_Click(object sender, EventArgs e)
        {
            if(textBox1.Text.All(char.IsLetter) && (textBox1.Text != ""))
                if ((textBox2.Text.Length == 16) && (textBox2.Text.All(char.IsDigit)))
                    if ((textBox4.Text.Length == 3) && (textBox4.Text.All(char.IsDigit)))
                    {
                        System.Threading.Thread.Sleep(900);
                        MessageBox.Show("Payment completed successfully!" + Environment.NewLine + Environment.NewLine + "Thank you!!", "Success!");

                        System.Windows.Forms.Form f1 = System.Windows.Forms.Application.OpenForms["order"];
                        if (((Order)f1) != null)
                        {
                            Application.OpenForms["order"].Close();
                        }
                        System.Windows.Forms.Form f2 = System.Windows.Forms.Application.OpenForms["eshop"];
                        if (((Eshop)f2) != null)
                        {
                            Application.OpenForms["eshop"].Close();
                        }
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show("CVV must be 3 digits", "Error");
                    }
                else
                {
                    MessageBox.Show("Card number must be 16 digits", "Error");
                }
            else
            {
                MessageBox.Show("Cardholder name must be only characters", "Error");
            }
        }

        private void backbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
