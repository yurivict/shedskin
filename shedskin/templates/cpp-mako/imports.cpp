## imports -> using

% for child, child_module in imports:
    <%
        mod_name = child_module.full_path()
    %>

% for n in child.names:
    <%
        name = n.name
        pseudo = n.asname or n.name
    %>

% if name == '*':

    % for func in child_module.mv.funcs.values() | selectattr("cp"):
    using ${mod_name}::${cpp_name(func)};
    % endfor


    % for cl in child_module.mv.classes.values():
    using ${ mod_name }::${cpp_name(cl)};
    % endfor

% elif pseudo not in module.mv.globals:

    % if name in child_module.mv.funcs:
        <%
            func = child_module.mv.funcs[name]
        %>

        % if func.cp:
        using ${mod_name}::${cpp_name(cl)};
        % endif

    % else:
    using ${mod_name }::${namer.nokeywords(name)};
    % endif

% endif

% endfor
% endfor
