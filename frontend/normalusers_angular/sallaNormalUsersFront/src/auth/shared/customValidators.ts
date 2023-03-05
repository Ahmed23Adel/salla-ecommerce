import { AbstractControl } from "@angular/forms";

export function confirmPasswordValidtor(contol: AbstractControl){
    const password = contol.get("password");
    const confirmPassword = contol.get("confirmPassword");
    if (password?.pristine || confirmPassword?.pristine){
        return null;
    }
    console.log("Confirm Password")
    return password && confirmPassword && password.value !== confirmPassword.value?{'mismatch':true}:null;
}

export function requirePhoneOnAuth(control: AbstractControl){
    const authPhone = control.get('TwoStepVerficationMobile');
    const phone = control.get('mobilePhone')
    if (authPhone?.value == true){
        console.log("phone")
        if (!/\d{11}/.test(phone?.value)){
            console.log("phone2")
            return {'phonerequired':true}
        }
    }
    return null
}