from django.shortcuts import render

def links_list(request):
    systems = [
        {"name": "Jira", "url": "https://grupomateus.atlassian.net/servicedesk/customer/portals"},
        {"name": "GM Suite", "url": "https://erp.gmsuite.com.br/"},
        {"name": "Maestro Web", "url": "https://maestro.grupomateus.com.br/home"},
        {"name": "Maxipos", "url": "http://pdv.mateus/maxipos_backoffice/app"},
        {"name": "Cloud Prix", "url": "https://monitor.cloudprix.com.br/Monitor"},
        {"name": "Sitef", "url": "https://oauth.softwareexpress.com.br/auth/realms/sitefconciliacao/protocol/openid-connect/auth?response_type=code&client_id=sitefweb&redirect_uri=https%3A%2F%2Fsitefconciliacao.softwareexpress.com.br%2Fsitefweb%2Fsso%2Flogin&state=8563e0a0-647e-4cad-b87d-7b725f905af3&login=true&scope=openid"},
        {"name": "GM Social", "url": "https://gmsocial.grupomateus.com.br/gmsocial/"},
        {"name": "Trilogo", "url": "https://grupomateus.trilogo.app/"},
        {"name": "Zimbra", "url": "https://email.grupomateus.com.br/"},
        {"name": "Mateus Mais", "url": "https://mateusmais.com.br/#/?utm_source=google&utm_medium=search&utm_campaign=appmateusmais"},
        {"name": "Down Detector", "url": "https://downdetector.com.br/"},
    ]
    return render(request, 'links_list.html', {'systems': systems})
