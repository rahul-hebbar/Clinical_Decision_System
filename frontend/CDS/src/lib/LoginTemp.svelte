<script>
	import {
		TextInput,
		PasswordInput,
		Button,
		InlineNotification
	} from "carbon-components-svelte";
	import {navigate} from "svelte-routing";
	import { user, token } from "./store";

	let pass_re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
	let email_re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

	let pas_val = "",pas_vali = false;
	let pas_war_state,pas_war,pas_inv,pas_inv_state;

	let e_val = "",e_vali = false;
	let e_war_state,e_war,e_inv,e_inv_state;

	let status = "";
	
	$: b_dis = (e_vali && pas_vali) ? false : true;

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
		fetch("/login", {
			method: 'POST',
			headers: {
				'Content-Type': "application/json",
			},
			body: JSON.stringify({"email": e_val, "password": pas_val}),
		}).then(resp => resp.json())
		.then(data => {
			status = data["msg"];
			if (status === "Success"){
				$user = data["user"];
				$token = data["token"];
				navigate("/dashboard", {replace: true} );
			}
			else {
				e_val = "";
				pas_val = "";
				e_vali = false;
				pas_vali = false;
			}
		})
		.catch((error) => console.log(error));
	}

</script>

<span>
	<h6 class=heading> Login </h6>
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
		<Button disabled={b_dis} on:click={b_click}>Submit</Button>
	</div>
	{#if status === "No account"}
		<InlineNotification kind="error" title="Error:" subtitle="No Account with email id registered" />
	{:else if status === "Wrong password"}
		<InlineNotification kind="error" title="Error:" subtitle="Wrong Password" />
	{/if}
</span>
