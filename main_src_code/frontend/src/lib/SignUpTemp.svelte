<script>
	import {
		TextInput,
		PasswordInput,
		Button,
		InlineNotification
	} from "carbon-components-svelte";

	let pass_re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
	let email_re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	let name_re = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/

	let n_val = "",n_vali = false;
	let n_war_state,n_war,n_inv_state,n_inv;

	let pas_val = "",pas_vali = false;
	let pas_war_state,pas_war,pas_inv,pas_inv_state;

	let e_val = "",e_vali = false;
	let e_war_state,e_war,e_inv,e_inv_state;

	$: b_dis = (e_vali && pas_vali && n_vali) ? false : true;
	let status = 0;

	let n_f = (e) => {
		if (n_val === ""){
			n_war = "Required!!";
			n_war_state = true;
			n_inv_state = false;
			n_vali = false;
		}
		else if (!name_re.test(n_val)) {
			n_war_state = false;
			n_inv_state = true;
			n_inv = "Invalid Name";
			n_vali = false;
		}
		else if (name_re.test(n_val)) {
			n_inv_state = false;
			n_war_state = false;
			n_vali = true;
		}		
	}

	let pas_f = (e) => {
		if (pas_val === ""){
			pas_war = "Required!!";
			pas_war_state = true;
			pas_inv_state = false;
			pas_vali = false;
		}
		else if (!pass_re.test(pas_val)) {
			pas_war_state = false;
			pas_inv_state = true;
			pas_inv = "Password must be min 8 letter, number and special char";
			pas_vali = false;
		}
		else if (pass_re.test(pas_val)) {
			pas_inv_state = false;
			pas_war_state = false;
			pas_vali = true;
		}
	}

	let e_f = (e) => {
		if (e_val === ""){
			e_war = "Required!!";
			e_war_state = true;
			e_inv_state = false;
			e_vali = false;
		}
		else if (!email_re.test(e_val)) {
			e_war_state = false;
			e_inv_state = true;
			e_inv = "Email Invalid!";
			e_vali = false;
		}
		else if (email_re.test(e_val)) {
			e_inv_state = false;
			e_war_state = false;
			e_vali = true;
		}
	}

	let b_click = (e) => {
		status = 0;
		fetch("/signup", {
			method: 'POST',
			headers: {
				'Content-Type': "application/json",
			},
			body: JSON.stringify({"name": n_val, "email": e_val, "password": pas_val}),
		}).then(resp => {
			status = resp["status"];
			e_val = "";
			n_val = "";
			pas_val = "";
			e_vali = false;
			pas_vali = false;
			n_vali = false;
		})
	}

</script>

<span>
	<h6 class="heading"> Sign Up </h6>
	<TextInput
	on:blur = {n_f}
	bind:value = {n_val}
	warn={n_war_state}
	warnText={n_war}
	invalid={n_inv_state}
	invalidText={n_inv}
	labelText = "Full Name"
	placeholder = "Enter your name..."
	/>
	<br />
	<TextInput
	on:blur = {e_f}
	bind:value = {e_val}
	warn={e_war_state}
	warnText={e_war}
	invalid={e_inv_state}
	invalidText={e_inv}
	labelText="Email ID" 
	placeholder="Enter reg email id..." 
	/>
	<br />
	<PasswordInput
	on:blur = {pas_f}
	bind:value = {pas_val}
	warn={pas_war_state}
	warnText={pas_war}
	invalid={pas_inv_state}
	invalidText={pas_inv}
	labelText="Password" 
	placeholder="Enter password..." 
	/>
	<br />
	<div class="but_align">
		<Button disabled={b_dis} on:click = {b_click}>Submit</Button>
	</div>
	{#if status === 201}
		<InlineNotification kind="success" title="Success:" subtitle="Registered Succesfully" />
	{:else if status === 202}
		<InlineNotification kind="warning" title="User Exists" subtitle="Use email to login" />
	{/if}
</span>