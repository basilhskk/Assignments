using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Globalization;

namespace bookstore
{
    public partial class Eshop : Form
    {
        string path = "books.txt";
        int numberofbooks = 0;
        double total = 0;
        string newtotal = "";

        string bookname = "";
        string price = "";

        public Eshop()
        {
            InitializeComponent();
        }

        private void Eshop_Load(object sender, EventArgs e)
        {
            listView2.View = View.Details;
            listView2.FullRowSelect = true;

            listView2.Columns.Add("Book name");
            listView2.Columns.Add("Price");

            for (int i = 0; i < listView2.Columns.Count; i++)
            {
                listView2.Columns[i].Width = -2;
            }

            deletebutton.Visible = false;
            
            listView1.View = View.Details;
            listView1.FullRowSelect = true;

            listView1.Columns.Add("ID");
            listView1.Columns.Add("Book name");
            listView1.Columns.Add("Author");
            listView1.Columns.Add("Publish date");
            listView1.Columns.Add("Country");
            listView1.Columns.Add("Language");
            listView1.Columns.Add("Price");

            for (int i = 0; i < listView1.Columns.Count; i++)
            {
                listView1.Columns[i].Width = -2;
            }

            var fileLines = File.ReadAllLines(path);

            for (int i = 0; i + 6 < fileLines.Length; i += 7)
            {
                listView1.Items.Add(new ListViewItem(new[]
                {
                    fileLines[i],
                    fileLines[i + 1],
                    fileLines[i + 2],
                    fileLines[i + 3],
                    fileLines[i + 4],
                    fileLines[i + 5],
                    fileLines[i + 6]
                }));
            }

            for (int i = 0; i < listView1.Columns.Count; i++)
            {
                listView1.Columns[i].Width = -2;
            }
            numberofbooks = listView1.Items.Count;
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count > 0)
            {
                ListViewItem item = listView1.SelectedItems[0];
                bookname = item.SubItems[1].Text;
                price = item.SubItems[6].Text;
            }
        }

        private void listView1_ColumnWidthChanging(object sender, ColumnWidthChangingEventArgs e)
        {
            e.Cancel = true;
            e.NewWidth = listView1.Columns[e.ColumnIndex].Width;
        }

        private void listView2_ColumnWidthChanging(object sender, ColumnWidthChangingEventArgs e)
        {
            e.Cancel = true;
            e.NewWidth = listView2.Columns[e.ColumnIndex].Width;
        }

        private void searchbutton_Click(object sender, EventArgs e)
        {
            listView1.SelectedItems.Clear();

            if (txtsearch.Text != "")
            {
                for (int i = listView1.Items.Count - 1; i >= 0; i--)
                {
                    var item = listView1.Items[i];
                    if ((item.SubItems[1].Text.ToLower() == txtsearch.Text.ToLower()) || (item.SubItems[2].Text.ToLower() == txtsearch.Text.ToLower()))
                    {
                        item.Selected = true;
                        break;
                    }
                    else
                    {
                        item.Selected = false;
                    }
                }
                if (listView1.SelectedItems.Count == 1)
                {
                    listView1.Focus();

                    listView1.SelectedItems[0].EnsureVisible();

                    ListViewItem item = listView1.SelectedItems[0];

                    bookname = item.SubItems[1].Text;
                    price = item.SubItems[6].Text;
                }
                else
                {
                    MessageBox.Show("No records found!", "Search");
                }
            }
            else
            {
                MessageBox.Show("Type something in the box to search it!", "Search");
            }
        }

        private void addbutton_Click(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count == 1)
            {
                listView2.Items.Add(new ListViewItem(new[] {bookname,price}));

                for (int i = 0; i < listView2.Columns.Count; i++)
                {
                    listView2.Columns[i].Width = -2;
                }
                listView1.SelectedItems.Clear();

                deletebutton.Visible = true;

                double newprice = Convert.ToDouble(price);
                total = total + newprice;
                newtotal = total.ToString("0:##.");
                newtotal = newtotal.Replace(":", ",");
                totallabel.Text = newtotal + " $";
            }
            else
            {
                MessageBox.Show("Select a book to add it!", "Cart");
            }
        }

        private void deletebutton_Click(object sender, EventArgs e)
        {
            if (listView2.SelectedItems.Count == 1)
            {
                foreach (ListViewItem item in listView2.Items)
                {
                    if (item.Selected)
                    {
                       double newprice = Convert.ToDouble(item.SubItems[1].Text);
                       total = total - newprice;
                       newtotal = total.ToString("0:##.");
                       newtotal = newtotal.Replace(":", ",");
                       totallabel.Text = newtotal + " $";
                       listView2.Items.Remove(item);
                    }
                }
            }
            else
            {
                MessageBox.Show("Select a book from the cart to delete it!", "Cart");
            }
        }

        private void paybutton_Click(object sender, EventArgs e)
        {
            if (total != 0)
            {
                Pay pay = new Pay(newtotal);
                pay.ShowDialog();
            }
            else
            {
                MessageBox.Show("Select at least one book to continue!", "Error");
            }
        }

        private void backbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
