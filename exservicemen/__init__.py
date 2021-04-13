# @login_required()
# @user_passes_test(wo_check)
# def reviewinfo(request):
#     email = request.session['email']
#     user = MyUser.objects.get(email=email)
#     return render(request, "exservicemen/officertemplates/wo_review_form.html")
