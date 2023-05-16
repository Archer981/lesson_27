from courses.models import Course
from django.http import JsonResponse


def courses(request):
    courses_list = Course.objects.all()
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)


def new_courses(request):
    if request.method == 'GET':
        # TODO напишите здесь view-функцию (задание new_courses)
        course_list = Course.objects.all().filter(status='new')
        # course_list = course_list.filter(status='new')
        result = []
        for course in course_list:
            # if course.status == 'new':
            result.append({
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            })
        return JsonResponse(result, safe=False)


def get_course(request, slug):
    if request.method == 'GET':
        # TODO напишите здесь view-функцию (задание find_by_name)
        course_list = Course.objects.all().filter(slug=slug)
        result = []
        for course in course_list:
            # if course.status == 'new':
            result.append({
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            })
        return JsonResponse(result, safe=False)


def get_course_empty(request):
    return JsonResponse({'Error': 'Empty slug'}, status=200)


def search(request):
    # TODO напишите здесь view-функцию (задание who's author)
    author = request.GET.get('author', None)
    if author:
        course_list = Course.objects.all().filter(author=author)
        result = []
        for course in course_list:
            result.append({
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            })
        return JsonResponse(result, safe=False)
    return JsonResponse({'Error': 'Author not found'}, 404)
