const pageElement = document.getElementById("page-name");
const page_name = pageElement.getAttribute("data-page-name");

const app = Vue.createApp({
	data() {
		return {
			// Customer
			customers: {},
			customer: {
				first_name: "",
				last_name: "",
				email: "",
				phone: "",
				phone2: "",
				addresse: "",
				postal_code: "",
				city: "",
				gender: "",
			},
			// Categorie
			categories: {},
			category: {
				name: "",
			},
			// Product
			products: {},
			product: {
				category: 0,
				name: "",
				brand: "",
				ref: "",
				vat: "",
				price: "",
				description: "",
			},
			// Inoives
			invoices: {},
			order: {
				customer: "",
				items: [
					{
						category: 0,
						products: [],
						product: "",
						quantity: 1,
						price_ht: 0,
					},
				],
			},
			selectedCategories: [],
			display_modal: false,
			// Searche
			searchQuery: "",
			// Error
			errors: {},
			on_success: false,
			on_bad_error: false,
			on_server_error: false,
			on_sending: false,
		};
	},
	delimiters: ["{", "}"],
	mounted() {
		this.load_page_list_data();
	},
	methods: {
		load_page_list_data() {
			switch (page_name) {
				case "customer":
					this.load_customers();
					break;
				case "category":
					this.load_categories();
					break;
				case "product":
					this.load_products();
					this.load_categories();
					break;
				case "invoice":
					this.load_invoices();
					this.load_customers();
					this.load_categories();
					break;
				default:
					console.log("Unknown fruit.");
					break;
			}
		},

		init() {
			this.product = {
				category: 0,
				name: "",
				brand: "",
				ref: "",
				vat: "",
				price: "",
				description: "",
			};

			this.customer = {
				first_name: "",
				last_name: "",
				email: "",
				phone: "",
				phone2: "",
				addresse: "",
				postal_code: "",
				city: "",
				gender: "",
			};

			this.order = {
				customer: "",
				items: [
					{
						category: 0,
						products: [],
						product: "",
						quantity: 1,
						price_ht: 0,
					},
				],
			};

			this.category = {
				name: "",
			};
		},

		post_request(url, data) {
			axios
				.post(url, data)
				.then((response) => {
					this.request_success();
					this.init();
				})
				.catch((error) => {
					this.on_success = false;
					this.request_error(error);
				});
		},
		add_new_customer() {
			this.post_request("/api/customer/", this.customer);
		},
		add_new_category() {
			this.post_request("/api/category/", this.category);
		},
		add_new_product() {
			this.post_request("/api/product/", this.product);
		},
		load_customers() {
			axios
				.get(`/api/customer/?search=${this.searchQuery}`)
				.then((response) => {
					this.customers = response.data;
				})
				.catch((err) => {
					this.customers = {};
				});
		},
		load_categories() {
			axios
				.get(`/api/category/?search=${this.searchQuery}`)
				.then((response) => {
					this.categories = response.data;
				})
				.catch((err) => {
					this.categories = {};
				});
		},
		load_products() {
			axios
				.get(`/api/product/?search=${this.searchQuery}`)
				.then((response) => {
					this.products = response.data;
				})
				.catch((err) => {
					this.products = {};
				});
		},
		load_invoices() {
			axios
				.get(`/api/order/?search=${this.searchQuery}`)
				.then((response) => {
					this.invoices = response.data;
				})
				.catch((err) => {
					this.invoices = {};
				});
		},
		load_products_by_category(item) {
			axios
				.get(`/api/product/?category=${item.category}`)
				.then((response) => {
					item.products = response.data;
					item.product = "";
					item.price_ht = 0;
				})
				.catch((err) => {
					item.products = [];
					item.product = "";
					item.price_ht = 0;
				});
		},
		//------- Search
		search_customers() {
			this.load_customers();
		},
		search_categories() {
			this.load_categories();
		},
		search_products() {
			this.load_products();
		},
		search_invoices() {
			this.load_invoices();
		},
		//------------ Invoices
		show_modal() {
			this.display_modal = true;
		},
		hide_modal() {
			this.display_modal = false;
		},
		clean_order_items_before_post() {
			let clened_order = { ...this.order };
			clened_order.items = this.order.items.map((item) => {
				const new_item = { ...item };
				delete new_item.oldCategory;
				delete new_item.products;
				return new_item;
			});

			return clened_order;
		},
		validate_invoice() {
			const cleanedOrder = this.clean_order_items_before_post();
			axios
				.post("/api/order/validate/", cleanedOrder)
				.then((response) => {
					this.show_modal();
				})
				.catch((error) => {
					this.on_success = false;
					this.request_error(error);
				});
		},
		generate_invoice() {
			const cleanedOrder = this.clean_order_items_before_post();
			this.on_sending = true;
			axios
				.post("/api/order/", cleanedOrder)
				.then((response) => {
					window.location.replace(response.data.pdf_url);
					this.on_sending = false;
				})
				.catch((error) => {
					this.on_success = false;
					this.on_sending = false;
					this.request_error(error);
				});
		},
		delete_order_item(index) {
			const removedCategory = this.order.items[index].category;
			if (removedCategory > 0) {
				this.selectedCategories = this.selectedCategories.filter(
					(cat) => cat.id !== removedCategory
				);
			}
			this.order.items.splice(index, 1);
		},
		add_order_item() {
			this.order.items.push({
				category: 0,
				product: "",
				products: [],
				quantity: 1,
				price_ht: 0,
				vat: 0,
			});
		},

		set_order_item_product_price(item, index) {
			let price = 0;
			if (item.product > 0) {
				price = item.products.results.filter(
					(product) => product.id === item.product
				)[0].price;
			}
			item.price_ht = price;
		},

		handleCategorySelection(item, index) {
			if (item.oldCategory) {
				this.selectedCategories = this.selectedCategories.filter(
					(cat) => cat.id !== item.oldCategory
				);
			}

			if (item.category) {
				let cat = this.categories.results.filter(
					(category) => category.id === item.category
				)[0];
				this.selectedCategories.push(cat);
				item.oldCategory = item.category;

				this.load_products_by_category(item, index);
			}
		},

		availableCategories(index) {
			return this.categories?.results?.filter(
				(category) =>
					!this.selectedCategories.some(
						(selectedCat) => selectedCat.id === category.id
					) ||
					(this.order.items[index].category &&
						this.order.items[index].category === category.id)
			);
		},

		// Error Message
		error_message(key) {
			return this.errors.hasOwnProperty(key) ? this.errors[key] : false;
		},
		item_error_message(index, key) {
			try {
				return this.errors.items[index].hasOwnProperty(key)
					? this.errors.items[index][key]
					: false;
			} catch (error) {
				return false;
			}
		},
		request_error(error) {
			if (error.response) {
				if (error.response.status == 400) {
					this.on_bad_error = true;
					this.errors = error.response.data;
				} else {
					this.on_server_error = true;
				}
			} else if (error.request) {
				console.log("Error request:", error.request);
			} else {
				console.log("Error message:", error.message);
			}
		},
		request_success() {
			this.on_success = true;
			this.on_bad_error = false;
			this.on_server_error = false;
			this.errors = {};
		},
	},
});

// Monter l'application Vue sur l'élément avec l'ID "app"
app.mount("#vue-app");
